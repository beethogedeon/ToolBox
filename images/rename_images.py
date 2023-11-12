import os
import random
import string
import shutil
import argparse


def generate_random_name(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def rename_images(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all files in the source folder
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for image_file in image_files:
        # Generate a random name
        new_name = generate_random_name() + os.path.splitext(image_file)[1]
        # Build the full path for source and destination
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(destination_folder, new_name)
        # Rename and copy the file
        shutil.copy(source_path, destination_path)


def main():
    parser = argparse.ArgumentParser(description="Rename images in a folder with random names.")
    parser.add_argument("source_folder", help="Path to the source folder containing images.")
    parser.add_argument("destination_folder", help="Path to the destination folder to save renamed images.")
    args = parser.parse_args()

    rename_images(args.source_folder, args.destination_folder)


if __name__ == "__main__":
    main()
