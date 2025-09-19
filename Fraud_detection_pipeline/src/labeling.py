# src/labeling.py
import pandas as pd

def label_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure fraud labels are numeric (0/1).
    """
    df = df.copy()  # prevent SettingWithCopyWarning
    df["is_fraud"] = df["is_fraud"].astype(int)
    return df
