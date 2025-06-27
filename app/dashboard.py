import pandas as pd

LOG_PATH = "data/presence_log.csv"

def load_data():
    try:
        return pd.read_csv(LOG_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Emotion", "Timestamp"])
