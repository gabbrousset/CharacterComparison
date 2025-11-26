import pandas as pd
import sys
import os
import argparse


INPUT_FILE = 'data/processed/cleaned_dialogue.csv'
STAGING_DIR = 'data/staging'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('character_name', help='name of character in quotes (eg "Cedric Diggory")')
    args = parser.parse_args()

    if not os.path.exists(INPUT_FILE):
        sys.exit(f'{INPUT_FILE} not found, run prep_data.py first')

    df = pd.read_csv(INPUT_FILE)

    target = args.character_name
    subset = df[df['Character Name'].str.lower() == target.lower()]

    if subset.empty:
        print(f'character {target} not found')
        sys.exit(1)

    os.makedirs(STAGING_DIR, exist_ok=True)

    output_df = subset[['Dialogue ID', 'Dialogue', 'Character Name']].copy()

    output_file = os.path.join(STAGING_DIR, f'{target.replace(' ', '_')}_all.csv')

    output_df.to_csv(output_file, index=False)

    print(f'found {len(output_df)}')


if __name__ == '__main__':
    main()
