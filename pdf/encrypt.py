from PyPDF2 import PdfReader, PdfWriter
import argparse


def encrypt_pdf(input_file, output_file, password):
    with open(input_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_file, 'wb') as output:
            pdf_writer.write(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt a PDF file with a password.')
    parser.add_argument('input', help='Input PDF file path')
    parser.add_argument('output', help='Output PDF file path')
    parser.add_argument('password', help='Password for encryption')

    args = parser.parse_args()

    encrypt_pdf(args.input, args.output, args.password)
