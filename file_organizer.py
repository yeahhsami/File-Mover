import os
import shutil

def move_files(source_dir, destination_dir):
    file_types = {
        'M': ['.mp3', '.wav', '.flac'],
        'I': ['.jpg', '.jpeg', '.png', '.gif'],
        'T': ['.txt', '.docx', '.pdf'],
        'C': ['.sql']
        # Add more file types and corresponding keys as needed
    }

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]

            for key, extensions in file_types.items():
                if file_extension.lower() in extensions:
                    destination_folder = os.path.join(destination_dir, key)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, destination_folder)
                    break