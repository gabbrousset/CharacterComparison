import pandas as pd
import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='CSV file to shuffle')
    parser.add_argument('-o', '--output', help='save shuffled file path/name (default: shuffled.csv)')
    parser.add_argument('-s', '--seed', type=int, default=42, help='random seed')

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        sys.exit(f'error: file {args.input_file} not found')

    df = pd.read_csv(args.input_file)

    df_shuffled = df.sample(frac=1, random_state=args.seed).reset_index(drop=True)

    output_path = 'shuffled.csv'
    if args.output:
        output_path = args.output

    df_shuffled.to_csv(output_path, index=False)

    print(f'saved as: {output_path}')


if __name__ == '__main__':
    main()
