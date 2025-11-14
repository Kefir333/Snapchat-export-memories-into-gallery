Snapchat Memories EXIF Fixer
Overview

This Python script updates the EXIF DateTimeOriginal of images exported from Snapchat Memories so that your photos will appear chronologically in your phone's gallery. Videos (MP4s) retain the correct timestamps.

Prerequisites
1. Install Python

Download Python 3.14 or newer from https://www.python.org/downloads/

During installation, check "Add Python to PATH"

To Verify installation, open PowerShell and paste this:

python --version
2. Install pip

If pip is missing, paste this line by line into PowerShell:

python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install piexif mutagen
Prepare Your Snapchat Export

Put all jpgs, mp4s, or raw data (file format as it was in my case) into one folder.

Extract any images inside ZIPs (with stickers/text) into the samefolder.

Ensure you have memories_history.json (or your JSON export) in the same folder, you can find it in the other download which is not the pictures and videos.

Prepare the Script

Open a text editor (Notepad, VS Code, etc.)

Paste the Python script below.

Save as set_snapchat_dates.py in the folder with your images and JSON.

Run the Script

Open PowerShell and navigate to your folder:

cd D:\path\to\your\folder

Run the script:

& "C:\path\to\python.exe" "D:\path\to\folder\set_snapchat_dates.py"

Finalized images will appear in an out/ folder which the script creates with correct EXIF timestamps.

Example Folder Structure
snapchat-fixer/
├── set_snapchat_dates.py
├── memories_history.json
├── out/                 # created by script
├── example_image1.jpg
└── example_image2
Notes

Only images present in both the folder and JSON are processed.

EXIF timestamps include the day aswell as the time so everything is in true chronological order.

MP4s are copied with correct timestamps without modification (atleast in my case, so i left them out in all this).
