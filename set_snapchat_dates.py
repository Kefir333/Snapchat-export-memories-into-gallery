#!/usr/bin/env python3
import os
import json
import shutil
from pathlib import Path
import piexif


# --- Configuration ---
SRC_DIR = Path('.') # folder containing your images and JSON
OUT_DIR = SRC_DIR / 'out' # destination folder
JSON_FILE = SRC_DIR / 'memories_history.json' # your JSON file


# Create output directory if it doesn't exist
OUT_DIR.mkdir(exist_ok=True)


# Load JSON
txt = JSON_FILE.read_text(encoding='utf-8')
metadata = json.loads(txt)["Saved Media"]


# Filter only images (ignore videos/stories)
image_entries = [entry for entry in metadata if entry['Media Type'].lower() == 'image']


# Snapchat JSON lists newest → oldest, so reverse to oldest → newest
image_entries.reverse()


# Collect actual image files (.jpg OR raw files with no extension)
all_files = sorted([
f for f in SRC_DIR.iterdir()
if f.is_file() and (f.suffix.lower() == '.jpg' or f.suffix == '')
])


# Warn if counts mismatch
if len(all_files) != len(image_entries):
print(f"Warning: {len(all_files)} files and {len(image_entries)} JSON entries do not match.")


# Process each file in order
for file_path, entry in zip(all_files, image_entries):
# Keep original filename; add .jpg if no extension
out_name = file_path.name
if file_path.suffix == '':
out_name += '.jpg'


dst_path = OUT_DIR / out_name
shutil.copy2(file_path, dst_path)


# Load EXIF
exif_dict = piexif.load(str(dst_path))


# Convert timestamp to EXIF format
date_part, time_part = entry['Date'].split(' ')[0:2]
dt_value = date_part.replace('-', ':') + ' ' + time_part # YYYY:MM:DD HH:MM:SS


exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = dt_value.encode('utf-8')


# Insert updated EXIF
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, str(dst_path))


print(f"[IMAGE] {file_path.name} → out/{out_name} (DateTimeOriginal={dt_value})")
