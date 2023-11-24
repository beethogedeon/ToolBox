import argparse
from PIL import Image


# Rotation function
def rotate_image(input_path, output_path, degrees):
    with Image.open(input_path) as img:
        rotated_img = img.rotate(degrees)
        rotated_img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rotate an image by a defined degree")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    parser.add_argument("--degrees", type=float, default=90, help="Degrees to rotate the image")

    args = parser.parse_args()

    rotate_image(args.input, args.output, args.degrees)
