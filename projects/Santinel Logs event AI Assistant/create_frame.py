import pandas as pd
import os

def save_to_csv_file(df, file_name="system_logs_dataset.csv"):
    file_exist = os.path.isfile(file_name)
    
    df.to_csv(file_name, mode='a', index=False, header=not file_exist)
    print(f"Saved {len(df)} records into the {file_name}")

def create_frame(event_list):
    df = pd.DataFrame(event_list)
    print("--- Current log statistic ---")
    print(df['type'].value_counts())
    print("-" * 35)
    print(f"Processed {len(df)} new events")
    save_to_csv_file(df)

def get_last_record(file_name="system_logs_dataset.csv"):
    file_exist = os.path.exists(file_name)
    if not file_exist:
        return 0
    else:
        try:
            df_temp = pd.read_csv(file_name, nrows=1)
            return int(df_temp.iloc[0]["record_no"])
        except Exception:
            return 0
        