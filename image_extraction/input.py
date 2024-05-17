import sys
import os

# Input: img_path, output_path, width, height
def get_input_data() -> list:
    data = sys.argv
    
    if len(data) != 5:
        print(f'\nInvalid input!')
        print(f'Should be: python3 {data[0]} img_path output_path output_file_width output_file_height')
        print(f'Data Types: python3 {data[0]} str str int int\n')
        os._exit(0)

    img_path = data[1]
    output_path = data[2]
    width = data[3]
    height = data[4]

    return img_path, output_path, width, height