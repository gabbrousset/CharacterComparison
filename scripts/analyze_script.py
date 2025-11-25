import pandas as pd
import sys
import os
import argparse


INPUT_FILE = 'data/processed/cleaned_dialogue.csv'


def get_word_count(text):
    return len(str(text).split())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min_words', type=int, default=5,
                        help='min word count for meaningful lines')
    parser.add_argument('-n', '--limit', type=int, default=0,
                        help='number of characters to display (0 for all)')

    args = parser.parse_args()

    min_words = args.min_words

    if not os.path.exists(INPUT_FILE):
        sys.exit(f'missing cleaned_dialogue.csv, run prep_data first')

    df = pd.read_csv(INPUT_FILE)

    # annotate lines with word count
    df['word_count'] = df['Dialogue'].apply(get_word_count)

    total_counts = df['Character Name'].value_counts().reset_index()
    total_counts.columns = ['Character', 'Total_Lines']

    df_meaningful = df[df['word_count'] >= min_words]
    meaningful_counts = df_meaningful['Character Name'].value_counts().reset_index()
    meaningful_counts.columns = ['Character', 'Meaningful_Lines']

    stats = pd.merge(total_counts, meaningful_counts, on='Character', how='left')
    stats = stats.fillna(0)  # for characters with no lines if they even exist ig

    if args.limit > 0:
        stats = stats.head(args.limit)

    stats['Meaningful_Lines'] = stats['Meaningful_Lines'].astype(int)  # idk why they were floats before

    print(f'character | total lines | more than {min_words} words ')
    print('-' * 20)

    for _, row in stats.iterrows():
        name = row['Character']
        total = row['Total_Lines']
        meaningful = row['Meaningful_Lines']

        print(f'{name} | {total} | {meaningful}')


if __name__ == '__main__':
    main()
