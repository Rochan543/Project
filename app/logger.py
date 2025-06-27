import pandas as pd
from datetime import datetime
import os

LOG_PATH = "data/presence_log.csv"

def log_data(name, emotion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([[name, emotion, timestamp]], columns=["Name", "Emotion", "Timestamp"])

    os.makedirs("data", exist_ok=True)
    if os.path.exists(LOG_PATH):
        df.to_csv(LOG_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(LOG_PATH, index=False)