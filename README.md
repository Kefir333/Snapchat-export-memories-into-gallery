# Snapchat Memories EXIF Fixer

DISCLAIMER: PLEASE MAKE A BACKUP OF ALL FILES YOU WILL WANT TO EDIT: THIS IS UNTESTED AS I HAD TO USE A EDITED VERSION OF THIS WHOLE THING BUT YOU GET THE GIST. IF YOU ENCOUNTER PROBLEMS ASK GPT, YOU WILL COME OUT WITH EVERYTHING WORKING EVENTUALLY
## Overview

This Python script updates the EXIF `DateTimeOriginal` of images exported from Snapchat Memories so that your photos will appear chronologically in your phone's gallery. Videos (MP4s) retain the correct timestamps.

---

## Prerequisites

### 1. Install Python

1. Download Python 3.14 or newer from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. During installation, check **"Add Python to PATH"**
3. To Verify installation, open PowerShell and paste this:
   ```powershell
   python --version
   ```

### 2. Install pip

If pip is missing, paste this line by line into PowerShell:

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install piexif mutagen
```

---

## Prepare Your Snapchat Export

1. Put all jpgs, mp4s, or raw data (file format as it was in my case) into one folder.
2. Extract any images inside ZIPs (with stickers/text) into the samefolder.
3. Ensure you have `memories_history.json` (or your JSON export) in the same folder, you can find it in the other download which is not the pictures and videos.

---

## Prepare the Script

1. Open a text editor (Notepad, VS Code, etc.)
2. Paste the Python script in the .py file I attached.
3. Save as `set_snapchat_dates.py` in the folder with your images and JSON.

---

## Example Folder Structure

```
snapchat-fixer/
├── set_snapchat_dates.py
├── memories_history.json
├── out/                 # created by script
├── example_image1.jpg
└── example_image2
```

---

## Run the Script

1. Open PowerShell and navigate to your folder:
   ```powershell
   cd D:\path\to\your\folder
   ```
2. Run the script:
   ```powershell
   & "C:\path\to\python.exe" "D:\path\to\folder\set_snapchat_dates.py"
   ```
3. Finalized images will appear in an `out/` folder which the script creates with correct EXIF timestamps.

---

## Notes

- Only images present in both the folder and JSON are processed.
- EXIF timestamps include the day aswell as the time so everything is in true chronological order.
- MP4s are copied with correct timestamps without modification (atleast in my case, so i left them out in all this).
