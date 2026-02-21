from sklearn.preprocessing import LabelEncoder
import pandas as pd
import config

def prepare_for_ml():
    df = pd.read_csv(config.LOG_FILE_PATH)
    
    ml_df = df.copy()
    
    le = LabelEncoder()
    print("S")
    ml_df['source'] = le.fit_transform(ml_df['source'])
    ml_df['type'] = le.fit_transform(ml_df['type'])
    
    print(ml_df)