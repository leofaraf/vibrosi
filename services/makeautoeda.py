import pandas as pd
from ydata_profiling import ProfileReport

# Example: load data
df = pd.read_csv("Сделки_bnMAPpro.csv")

# Create the profile (the auto EDA report)
profile = ProfileReport(
    df,
    title="Сделки_bnMAPpro AutoEDA",
    explorative=True  # adds more advanced analyses & plots
)

profile.to_file("Сделки_bnMAPpro_auto_eda_report.html")
print("Report saved to auto_eda_report.html")

# Example: load data
df = pd.read_csv("Проектные_данные_bnMAPpro.csv")

# Create the profile (the auto EDA report)
profile = ProfileReport(
    df,
    title="Проектные_данные_bnMAPpro AutoEDA",
    explorative=True  # adds more advanced analyses & plots
)

profile.to_file("Проектные_данные_bnMAPpro_auto_eda_report.html")
print("Report saved to auto_eda_report.html")