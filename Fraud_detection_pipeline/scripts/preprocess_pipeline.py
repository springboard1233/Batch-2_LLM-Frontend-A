# scripts/preprocess_pipeline.py
import os
from src.ingestion import load_transactions
from src.cleaning import clean_transactions
from src.labeling import label_transactions
from src.features import add_features
from src.utils import split_dataset

RAW_DATA_PATH = "data/raw/transactions.csv"
PROCESSED_PATH = "data/processed/"

def run_pipeline():
    print("🚀 Starting preprocessing pipeline...")

    # Step 0: Ensure processed directory exists
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Step 1: Load
    df_raw = load_transactions(RAW_DATA_PATH)
    print(f"Loaded {len(df_raw)} rows")

    # Step 2: Clean
    df_clean = clean_transactions(df_raw)
    print(f"After cleaning: {len(df_clean)} rows")

    # Step 3: Label
    df_labeled = label_transactions(df_clean)

    # Step 4: Feature Engineering
    df_features = add_features(df_labeled)

    # Step 5: Split
    train_df, val_df, test_df = split_dataset(df_features)

    # Step 6: Save processed datasets
    train_df.to_csv(os.path.join(PROCESSED_PATH, "train.csv"), index=False)
    val_df.to_csv(os.path.join(PROCESSED_PATH, "val.csv"), index=False)
    test_df.to_csv(os.path.join(PROCESSED_PATH, "test.csv"), index=False)

    print("✅ Preprocessing completed. Files saved in data/processed/")

if __name__ == "__main__":
    run_pipeline()
