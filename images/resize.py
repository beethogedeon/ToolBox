from PIL import Image
import os
import argparse


# Resizing function
def resize_images(input_folder, output_folder, target_size=(640, 640)):

    # The output folder will be created if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # We get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Check if the file is an image
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Define the full file paths
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            # Open the image using Image module from PIL
            img = Image.open(input_path)

            # Resize the image
            resized_img = img.resize(target_size)

            # Save the resized image
            resized_img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images from input folder to output folder")
    parser.add_argument("input_folder", help="Path to the input folder containing images.")
    parser.add_argument("output_folder", help="Path to the output folder for resized images.")
    parser.add_argument("--width", type=int, default=640, help="Target width for resizing (default: 640).")
    parser.add_argument("--height", type=int, default=640, help="Target height for resizing (default: 640).")

    args = parser.parse_args()

    # Set the target size for resizing
    target_size = (args.width, args.height)

    # Resize images and save them to the output folder
    resize_images(args.input_folder, args.output_folder, target_size)
