# src/ingestion.py
import pandas as pd
from pathlib import Path

def load_transactions(file_path: str) -> pd.DataFrame:
    """
    Load raw transactions CSV into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the raw transactions.csv file.
    
    Returns:
        pd.DataFrame: Raw transactions dataset.
    """
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"{file_path} not found!")
    
    df = pd.read_csv(file_path)
    return df
