import pandas as pd
import argparse


def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to JSON and save to file
    df.to_json(json_file_path, orient='records', indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV file to JSON")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("json_file", help="Path to the output JSON file")

    args = parser.parse_args()

    csv_to_json(args.csv_file, args.json_file)
