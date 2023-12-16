import pandas as pd
import os
from pathlib import Path

LABELED_CSV_PATH = os.path.join(os.getcwd(), 'secret_stuff', 'labeled_mapped.csv')

def main(labeled_csv_path):
    df = pd.read_csv(labeled_csv_path)
    print(df['label'].value_counts())

if __name__ == '__main__':
    main(LABELED_CSV_PATH)

