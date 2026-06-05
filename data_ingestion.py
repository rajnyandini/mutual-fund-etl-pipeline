import pandas as pd
import os

folder = "data/raw/ ABC_MF_Datasets"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n" + "="*50)
        print(file)
        print("Shape:", df.shape)
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())