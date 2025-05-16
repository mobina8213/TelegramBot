import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, 'dataset')

def load_dataset():
    # فقط فایل googleplaystore.csv رو بارگذاری کن و برگردون
    file_path = os.path.join(DATA_FOLDER, 'googleplaystore.csv')
    try:
        print(f"Loading dataset from: {file_path}")
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def load_csv_files():
    csv_files = [
        'googleplaystore.csv',
        'googleplaystore_user_reviews.csv'
    ]
    dataframes = {}
    for filename in csv_files:
        file_path = os.path.join(DATA_FOLDER, filename)
        try:
            print(f"Loading CSV file: {filename}")
            df = pd.read_csv(file_path)
            dataframes[filename] = df
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    return dataframes

def load_license():
    license_path = os.path.join(DATA_FOLDER, 'license.txt')
    try:
        print(f"Loading license file")
        with open(license_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error loading license.txt: {e}")
        return None
