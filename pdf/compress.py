from PyPDF2 import PdfReader, PdfWriter
import argparse
import os


# Compress function
def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.compress_content_streams()
            pdf_writer.add_page(page)

        pdf_writer.write(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress PDF files.")
    parser.add_argument('input', help="Input PDF file path")
    parser.add_argument('-o', '--output', help="Output PDF file path (default: compressed_input.pdf)",
                        default='compressed.pdf')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    compression_quality = args.quality

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Error: Input file '{input_path}' not found.")

    compress_pdf(input_path, output_path)
