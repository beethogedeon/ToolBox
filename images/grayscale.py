import os
from PIL import Image
import argparse


# Grayscaling function
def convert_to_grayscale(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            # Open the image file
            image = Image.open(input_path)

            # Convert the image to grayscale
            grayscale_image = image.convert('L')

            # Save the grayscale image to the output folder
            grayscale_image.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images in a folder to grayscale and save in another folder.")
    parser.add_argument("input_folder", help="Path to the folder containing images")
    parser.add_argument("output_folder", help="Path to the folder where grayscale images will be saved")

    args = parser.parse_args()

    convert_to_grayscale(args.input_folder, args.output_folder)
