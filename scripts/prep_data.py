import pandas as pd
import os
import sys


RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'

DIALOGUE_PATH = os.path.join(RAW_DIR, 'Dialogue.csv')
CHARACTERS_PATH = os.path.join(RAW_DIR, 'Characters.csv')
OUTPUT_PATH = os.path.join(PROCESSED_DIR, 'cleaned_dialogue.csv')


def main():
    if not os.path.exists(DIALOGUE_PATH) or not os.path.exists(CHARACTERS_PATH):
        sys.exit(f'missing Dialogue.csv and/or Characters.csv in data/raw')

    try:
        # load data
        df_dialogue = pd.read_csv(DIALOGUE_PATH)
        df_chars = pd.read_csv(CHARACTERS_PATH)

        # 'inner' to remove dialogue from characters not in list
        df_merged = pd.merge(df_dialogue, df_chars, on='Character ID', how='inner')

        # only need 2 columns
        df_clean = df_merged[['Character Name', 'Dialogue']].copy()

        # basic cleaning
        # empty rows
        df_clean.dropna(subset=['Dialogue'], inplace=True)
        # strip whitespace
        df_clean['Dialogue'] = df_clean['Dialogue'].astype(str).str.strip()

        # save to CSV
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        df_clean.to_csv(OUTPUT_PATH)

    except Exception as e:
        sys.exit(f'error: {e}')


if __name__ == '__main__':
    main()
