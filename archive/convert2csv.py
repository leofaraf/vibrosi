import pandas as pd

projects_df = pd.read_excel("Проектные_данные_bnMAPpro.xlsx")
projects_df.to_csv("Проектные_данные_bnMAPpro.csv", index=False)

deals_df = pd.read_excel("Сделки_bnMAPpro.xlsx")
deals_df.to_csv("Сделки_bnMAPpro.csv", index=False)
