import pandas as pd

projects_df = pd.read_excel("services/Проектные данные_2025-11-25.xlsx")
projects_df.to_csv("projects.csv", index=False)

deals_df = pd.read_excel("services/Сделки_2025-11-25.xlsx")
deals_df.to_csv("offers.csv", index=False)
