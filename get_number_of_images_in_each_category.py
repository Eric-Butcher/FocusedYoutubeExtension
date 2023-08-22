import pandas as pd
from pathlib import Path

LABELED_CSV_PATH = Path.cwd() / 'labeled_mapped.csv'

def main(labeled_csv_path):
    df = pd.read_csv(labeled_csv_path)
    print(df['label'].value_counts())

if __name__ == '__main__':
    main(LABELED_CSV_PATH)

