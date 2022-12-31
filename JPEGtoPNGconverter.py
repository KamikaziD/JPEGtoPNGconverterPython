import sys
import os
import glob
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]


def check_output_dir(folder):
    """Check if the output folder exists otherwise create folder"""
    base_path = f'./{input_folder}'
    if not os.path.exists(f'{base_path}{folder}'):
        os.makedirs(f'{base_path}{folder}')
        print(f'Created {base_path}{folder}')


def process_files(path):
    """Loop though input folder and convert to PNG, Save to Output Folder"""
    check_output_dir(output_folder)
    os.chdir(path)
    for file in glob.glob("*.jpg"):
        img = Image.open(file)
        new_filename = os.path.splitext(file)[0]
        print(f'Processing file: {new_filename}')
        img.save(f'./{output_folder}{new_filename}_new.png', 'png')


if __name__ == "__main__":
    process_files(input_folder)
