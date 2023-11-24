import argparse
from PIL import Image


# Cropping function
def crop_image(input_path, output_path, left, top, right, bottom):
    with Image.open(input_path) as img:
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop images.")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    parser.add_argument("--left", type=int, default=0, help="Left coordinate of the crop box")
    parser.add_argument("--top", type=int, default=0, help="Top coordinate of the crop box")
    parser.add_argument("--right", type=int, help="Right coordinate of the crop box")
    parser.add_argument("--bottom", type=int, help="Bottom coordinate of the crop box")

    args = parser.parse_args()

    crop_image(args.input, args.output, args.left, args.top, args.right, args.bottom)
