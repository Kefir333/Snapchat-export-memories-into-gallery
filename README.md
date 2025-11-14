# Snapchat EXIF Fixer

This Python script fixes exported Snapchat Memories images so they have the correct timestamps in EXIF.

## Prerequisites
1. Install Python 3.14+ from https://www.python.org/downloads/
2. Ensure pip is installed:
   "D:\Programme\Python\python.exe" -m ensurepip --upgrade
   "D:\Programme\Python\python.exe" -m pip install --upgrade pip
3. Install required packages:
   "D:\Programme\Python\python.exe" -m pip install piexif mutagen

## Usage
1. Export Snapchat Memories JSON and unzip any zipped photos.
2. Place .jpg files and JSON in the same folder as set_snapchat_dates.py.
3. Run the script:
   & "D:\Programme\Python\python.exe" "D:\Path\To\set_snapchat_dates.py"
Processed images will appear in the `out/` folder.
