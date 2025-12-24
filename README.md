# Backup Util

This is a minimal script to backup your local files.

## Requirements

Python 3

## Usage Examples

### Linux/MacOS
```
python3 ./app.py
Enter a folder path to back up: /home/fakeuser1/
Enter a folder to store the backup: /home/fakeuser2/
Enter 1 to remove all files in the backup folder that aren't also in the main folder, or enter 2 to let those paths remain:
1
Copied to /home/fakeuser/downloads/fakefile1.mp4
Copied to /home/fakeuser/downloads/fakefile2.mp4
Deleted /home/fake/fakeuser/documents/fakefile3.docx
Backup complete!
```
```
python3 ./app.py
Enter a folder path to back up: /home/fakeuser1/
Enter a folder to store the backup: /home/fakeuser2/
Enter 1 to remove all files in the backup folder that aren't also in the main folder, or enter 2 to let those paths remain:
2
Copied to /home/fakeuser/downloads/fakefile1.mp4
Copied to /home/fakeuser/downloads/fakefile2.mp4
Backup complete!
```
### Windows
```
python app.py
Enter a folder path to back up: /home/fakeuser1/
Enter a folder to store the backup: /home/fakeuser2/
Enter 1 to remove all files in the backup folder that aren't also in the main folder, or enter 2 to let those paths remain:
1
Copied to /home/fakeuser/downloads/fakefile1.mp4
Copied to /home/fakeuser/downloads/fakefile2.mp4
Deleted /home/fake/fakeuser/documents/fakefile3.docx
Backup complete!
```
```
python app.py
Enter a folder path to back up: /home/fakeuser1/
Enter a folder to store the backup: /home/fakeuser2/
Enter 1 to remove all files in the backup folder that aren't also in the main folder, or enter 2 to let those paths remain:
2
Copied to /home/fakeuser/downloads/fakefile1.mp4
Copied to /home/fakeuser/downloads/fakefile2.mp4
Backup complete!
```
