import pandas as pd

def create_frame(event_list):
    df = pd.DataFrame(event_list)
    print("--- Поточна статистика пачки логів ---")
    print(df['type'].value_counts())
    print("-" * 35)