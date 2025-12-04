import pandas as pd
import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='CSV file with annotations')
    parser.add_argument('col', help='name of the column with 1/0 flag')
    parser.add_argument('-r', '--rev', action='store_true', help='get items with 0 instead of 1')
    parser.add_argument('-o', '--output', help='save shuffled file path/name (default: filtered.csv)')

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        sys.exit(f'error: file {args.input_file} not found')

    df = pd.read_csv(args.input_file)

    # check if column exists
    if args.col not in df.columns:
        print(f'error: column {args.col} not found in CSV')
        print(f'available columns: {list(df.columns)}')
        sys.exit(1)

    # filter, keep only rows where value is 1 or '1' or 0 when rev flag is passed
    condition = '1'
    if args.rev:
        condition = '0'
    df_filtered = df[df[args.col].astype(str).str.strip() == condition]

    output_path = 'filtered.csv'
    if args.output:
        output_path = args.output
    df_filtered.to_csv(output_path, index=False)

    print(f'original lines: {len(df)}, new lines: {len(df_filtered)}')
    print(f'saved as: {output_path}')


if __name__ == '__main__':
    main()
