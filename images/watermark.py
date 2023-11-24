import argparse
from PIL import Image, ImageDraw, ImageFont


# Watermarking function
def add_watermark(input_path, output_path, watermark_text, position="bottom-right", font_size=20, opacity=128):
    with Image.open(input_path) as img:
        # Create a copy of the image to add the watermark
        watermarked_img = img.copy()

        # Get the width and height of the image
        img_width, img_height = img.size

        # Create a drawing object
        draw = ImageDraw.Draw(watermarked_img)

        # Choose a font (adjust the path to a font file on your system)
        font = ImageFont.load_default()

        # Calculate the position to place the watermark
        if "top" in position:
            y = 0
        elif "bottom" in position:
            y = img_height - font_size
        else:
            y = (img_height - font_size) // 2

        if "left" in position:
            x = 0
        elif "right" in position:
            x = img_width - draw.textsize(watermark_text, font)[0]
        else:
            x = (img_width - draw.textsize(watermark_text, font)[0]) // 2

        # Add the watermark text to the image
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

        # Save the watermarked image
        watermarked_img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add watermark to images.")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output image file path")
    parser.add_argument("watermark_text", help="Text for the watermark")
    parser.add_argument("--position",
                        choices=["top-left", "top-center", "top-right", "center-left", "center", "center-right",
                                 "bottom-left", "bottom-center", "bottom-right"], default="bottom-right",
                        help="Position of the watermark on the image")
    parser.add_argument("--font_size", type=int, default=50, help="Font size of the watermark text")
    parser.add_argument("--opacity", type=int, default=128, help="Opacity of the watermark (0-255)")

    args = parser.parse_args()

    add_watermark(args.input, args.output, args.watermark_text, args.position, args.font_size, args.opacity)
