import pandas as pd

def create_frame(event_list):
    df = pd.DataFrame(event_list)
    print("--- Current log statistic ---")
    print(df['type'].value_counts())
    print("-" * 35)
    print(f"Processed {len(df)} new events")