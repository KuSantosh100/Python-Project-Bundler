import os

# Path to the folder where your files are stored
folder_path = "./Projects"  # change to your target directory

for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename[0].isdigit():
        # Original filename: "1. Dice Rolling Simulator.py"
        name_part = filename[:-3]  # remove ".py"
        extension = ".py"
        
        # Step 1: Remove space after number-dot
        if ". " in name_part:
            number, title = name_part.split(". ", 1)
            new_title = title.replace(" ", "-")
            new_filename = f"{number}.{new_title}{extension}"

            # Rename the file
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} → {new_filename}")