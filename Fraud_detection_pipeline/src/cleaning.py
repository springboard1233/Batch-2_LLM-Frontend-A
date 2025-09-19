# src/cleaning.py
import pandas as pd

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize transaction dataset.
    """
    df = df.copy()  # prevent SettingWithCopyWarning

    # Standardize KYC
    df["kyc_verified"] = df["kyc_verified"].map({"Yes": 1, "No": 0})

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", dayfirst=True)

    # Drop rows with essential missing values
    df = df.dropna(subset=["transaction_id", "customer_id", "timestamp"])

    # Fill numeric nulls with 0
    df["account_age_days"] = df["account_age_days"].fillna(0)
    df["transaction_amount"] = df["transaction_amount"].fillna(0)

    return df
