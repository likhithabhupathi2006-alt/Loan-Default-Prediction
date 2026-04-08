import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Fill missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    print("Preprocessing completed")
    return df
