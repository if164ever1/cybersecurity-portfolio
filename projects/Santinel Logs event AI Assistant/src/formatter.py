import pandas as pd
import os
import config

def save_to_csv_file(df, file_name=config.LOG_FILE_PATH):
    file_exist = os.path.isfile(file_name)
    
    df.to_csv(file_name, mode='a', index=False, header=not file_exist)
    print(f"Saved {len(df)} records into the {file_name}")

def create_frame(event_list):
    df = pd.DataFrame(event_list)
    print("--- Current log statistic ---")
    print(df['type'].value_counts())
    print("-" * 35)
    print(f"Processed {len(df)} new events")
    df['time'] = pd.to_datetime(df['time'])
    df['hour'] = df['time'].dt.hour
    df['day_of_week'] = df['time'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x>= 5 else 0)
    save_to_csv_file(df)


def get_last_record(file_name=config.LOG_FILE_PATH):
    file_exist = os.path.exists(file_name)
    if not file_exist:
        return 0
    else:
        try:
            df_temp = pd.read_csv(file_name, nrows=1)
            return int(df_temp.iloc[0]["record_no"])
        except Exception:
            return 0
        
        