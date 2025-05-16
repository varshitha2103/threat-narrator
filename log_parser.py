import pandas as pd

def load_logs(filepath):
    df = pd.read_csv(filepath)
    df.fillna("Unknown", inplace=True)
    return df.to_dict(orient="records")
