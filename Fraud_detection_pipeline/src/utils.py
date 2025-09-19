# src/utils.py
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(df: pd.DataFrame, test_size: float = 0.2, val_size: float = 0.1, random_state: int = 42):
    """
    Split dataset into train, validation, and test sets.
    """
    df = df.copy()  # safe copy
    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df["is_fraud"]
    )
    train_df, val_df = train_test_split(
        train_df, test_size=val_size, random_state=random_state, stratify=train_df["is_fraud"]
    )
    return train_df, val_df, test_df
