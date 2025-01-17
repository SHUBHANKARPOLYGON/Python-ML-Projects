from imutils import paths
import cv2
import os
import shutil
import hashlib

def file_hash(file_path, hash_algo="sha256", chunk_size=8192):
    """
    Compute the hash of a file using the specified hashing algorithm.
    Default is SHA-256.
    """
    hash_func = hashlib.new(hash_algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Path to the folder containing files
input_folder = 'Dataset'
output_folder = 'Duplicate_Files'

# Create the duplicate folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder (recursively)
file_paths = list(paths.list_files(input_folder))
hashes = {}

# Compute the hash for each file
for file_path in file_paths:
    if not os.path.isfile(file_path):
        continue  # Skip non-files like directories
    try:
        file_hash_value = file_hash(file_path)
        # Group files by hash
        p = hashes.get(file_hash_value, [])
        p.append(file_path)
        hashes[file_hash_value] = p
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Check for duplicates and move them to the duplicate folder
for (hash_value, hashed_paths) in hashes.items():
    if len(hashed_paths) > 1:  # If there are duplicates
        # Keep the first file, move the rest to the duplicate folder
        for duplicate_path in hashed_paths[1:]:
            filename = os.path.basename(duplicate_path)
            destination = os.path.join(output_folder, filename)

            # Ensure unique file names in the duplicate folder
            counter = 1
            while os.path.exists(destination):
                filename, ext = os.path.splitext(os.path.basename(duplicate_path))
                destination = os.path.join(output_folder, f"{filename}_{counter}{ext}")
                counter += 1

            print(f"Moving {duplicate_path} to {destination}")
            shutil.move(duplicate_path, destination)
