# src/features.py
import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering on transactions.
    """
    df = df.copy()  # prevent SettingWithCopyWarning

    # Extract datetime features
    df["year"] = df["timestamp"].dt.year
    df["month"] = df["timestamp"].dt.month
    df["day"] = df["timestamp"].dt.day
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    # One-hot encode channel
    df = pd.get_dummies(df, columns=["channel"], prefix="channel")

    return df
