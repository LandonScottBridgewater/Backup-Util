import os
import shutil

main_folder = input("Enter a folder path to back up: ").strip()
backup_folder = input("Enter a folder to store the backup: ").strip()
clear_backup_excess = input(
    "Enter 1 to remove all files in the backup folder that aren't also in the main folder, "
    "or enter 2 to let those paths remain: "
).strip() == "1"

for root, dirs, files in os.walk(main_folder):
    rel_path = os.path.relpath(root, main_folder)
    dest_dir = os.path.join(backup_folder, rel_path)
    os.makedirs(dest_dir, exist_ok=True)
    
    for f in files:
        src_file = os.path.join(root, f)
        dest_file = os.path.join(dest_dir, f)
        if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
            print(f"Copied to {dest_file}")
            shutil.copy2(src_file, dest_file)

if clear_backup_excess:
    for root, dirs, files in os.walk(backup_folder, topdown=False):
        rel_path = os.path.relpath(root, backup_folder)
        src_dir = os.path.join(main_folder, rel_path)
        
        for f in files:
            backup_file = os.path.join(root, f)
            main_file = os.path.join(src_dir, f)
            if not os.path.exists(main_file):
                print(f"Deleted {backup_file}")
                os.remove(backup_file)
        
        if not os.listdir(root):
            os.rmdir(root)

print("Backup complete!")
