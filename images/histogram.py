import argparse
import matplotlib.pyplot as plt
from PIL import Image


# Histogram generator function
def generate_histogram(input_path, output_path=None):
    with Image.open(input_path) as img:
        # Generate the histogram
        histogram = img.histogram()

        # Separate the histogram into red, green, and blue channels
        r_hist = histogram[0:256]
        g_hist = histogram[256:512]
        b_hist = histogram[512:768]

        # Plot the histograms
        plt.figure(figsize=(10, 5))

        plt.subplot(2, 2, 1)
        plt.title("Grayscale Image")
        plt.imshow(img, cmap="gray")
        plt.axis("off")

        plt.subplot(2, 2, 2)
        plt.title("Histogram")
        plt.plot(histogram, color='black')
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")

        plt.subplot(2, 2, 3)
        plt.title("Red Histogram")
        plt.plot(r_hist, color='red')
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")

        plt.subplot(2, 2, 4)
        plt.title("Green Histogram")
        plt.plot(g_hist, color='green')
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")

        if output_path:
            plt.savefig(output_path)
        else:
            plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate histogram for images.")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("--output", help="Output file path for the histogram plot")

    args = parser.parse_args()

    generate_histogram(args.input, args.output)
