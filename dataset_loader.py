import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'googleplaystore.csv')  # مسیر و اسم دقیق فایل

def load_dataset():
    try:
        print(f"Loading dataset from: {DATA_PATH}")
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
