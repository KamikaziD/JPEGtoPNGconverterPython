import sys
import os
import glob
from PIL import Image

# grab the first & second argument with sys argv
input_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if output/ exists otherwise create folder
def check_output_dir(folder):
    """Check if the output folder exists"""
    base_path = f'./{input_folder}'
    if os.path.isdir(f'{base_path}{folder}'):
        return True
    else:
        os.mkdir(f'{base_path}{folder}')
        print(f'Created {base_path}{folder}')
        return False


# loop through input folder and convert images to png, save to output/ folder
def files_loop(path):
    """Loop though input folder and convert to PNG, Save to Output Folder"""
    check_output_dir(output_folder)
    os.chdir(path)
    for file in glob.glob("*.jpg"):
        img = Image.open(file)
        new_filename = os.path.splitext(file)[0]
        print(f'Processing file: {new_filename}')
        img.save(f'./{output_folder}{new_filename}_new.png', 'png')


files_loop(input_folder)
