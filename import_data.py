import pandas as pd
pd.options.mode.chained_assignment = None
import os.path #To check that the file exists

def import_data():
    df = pd.DataFrame()
    while len(df)==0:
        data_path = input("Please enter the full location of your data on your device: ") 
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            if "Unnamed: 0" in df.columns:
                df = df.drop('Unnamed: 0', axis=1)
            print("Thank you, this is the first 5 rows of the dataframe you have loaded.")
            print(df.head())
        else:
            print("There is no readable file in this location. Please try again.")
    df=df.astype(str)
    return df