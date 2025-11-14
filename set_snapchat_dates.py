#!/usr/bin/env python3
import os, json, shutil
from pathlib import Path
import piexif

SRC_DIR = Path('.')
OUT_DIR = SRC_DIR / 'out'
JSON_FILE = SRC_DIR / 'memories_history.json'  # Make sure this matches your JSON filename
OUT_DIR.mkdir(exist_ok=True)

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    metadata = json.load(f)["Saved Media"]

# Only image entries
image_entries = [entry for entry in metadata if entry['Media Type'].lower() == 'image']

# Gather local JPG files
jpg_files = [f for f in SRC_DIR.iterdir() if f.is_file() and f.suffix.lower() in ('.jpg', '.jpeg')]

# Reverse JSON order if needed (oldest first)
image_entries.reverse()

for jpg_file, entry in zip(sorted(jpg_files), image_entries):
    dst_path = OUT_DIR / jpg_file.name
    shutil.copy2(jpg_file, dst_path)
    exif_dict = piexif.load(str(dst_path))
    date_part, time_part = entry['Date'].split(' ')[0:2]
    dt_value = date_part.replace('-', ':') + ' ' + time_part
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = dt_value.encode('utf-8')
    piexif.insert(piexif.dump(exif_dict), str(dst_path))
    print(f"[JPEG] {jpg_file.name} → out/{dst_path.name} (DateTimeOriginal={dt_value})")
