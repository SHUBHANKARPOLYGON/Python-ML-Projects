# File Duplicacy Finder

This Python script identifies duplicate files in a specified folder and moves them to a separate folder for easy management. The script uses hashing to ensure accuracy and works with files of any extension.

### Features
- Identifies duplicate files based on their hash values (default: SHA-256).
- Works with files of any type or extension.
- Moves duplicates to a specified folder, ensuring unique filenames.
- Recursively processes files in subdirectories.

## Prerequisites
### Python Libraries

- ```imutils```: For listing files in directories recursively.
- ```OpenCV (cv2)```: Required if you use image-based processing; not directly utilized in this script.
- ```hashlib```: For computing file hashes.
- ```shutil```: For moving files.

You can install required libraries using pip:

```bash
pip install imutils
```

### Installation
1. Clone this repository or download the script.

2. Install the required Python libraries as listed above.

3. Update the ```input_folder``` and ```output_folder``` variables in the script to point to your desired folders.

### Usage
1. Place the files you want to check for duplicates in the input_folder.

2. Run the script:
```bash
python app.py
```
Duplicate files will be moved to the ```output_folder``` with unique filenames if necessary.

### How It Works

1. Hash Computation:
- The script calculates the hash value of each file in the ```input_folder``` using the ```file_hash``` function. The default hashing algorithm is SHA-256.

2. Duplicate Detection:
- Files with identical hash values are identified as duplicates.

3. File Management:
- The first instance of a file is retained in its original location.

- All duplicate files are moved to the ```output_folder```. If a file with the same name already exists in the output folder, a unique name is generated.

### Example
Given the following folder structure:

```bash
Dataset/
  file1.txt
  file2.txt
  file3.txt
  file1_duplicate.txt
```
After running the script, the duplicate file (```file1_duplicate.txt```) will be moved to the ```Duplicate_Files``` folder:

```bash
Dataset/
  file1.txt
  file2.txt
  file3.txt
Duplicate_Files/
  file1_duplicate.txt
```

### Customization
- **Hashing Algorithm**: Modify the ```hash_algo``` parameter in the ```file_hash``` function to use a different algorithm, such as MD5 or SHA-1.

- **Chunk Size**: Adjust the ```chunk_size``` parameter in the ```file_hash``` function for performance optimization with large files.

### Limitations

- The script skips non-file items like directories.

- Files with the same content but different names are considered duplicates and will be processed accordingly.

### Contributions
Feel free to fork the repository and submit pull requests with improvements or bug fixes. Suggestions are always welcome!
