import pandas as pd #type: ignore
from pandas import DataFrame #type: ignore

df:DataFrame = pd.read_csv("Ergebnisssammlung_Härte.csv")

parametersets:list[str] = ["2000","2100","2200","4000","2001", "2101", "2201", "4001"]

df_sample_results:DataFrame = pd.DataFrame(columns=["Sample","Mean","negYerr","posYerr","Min", "Max"])

for colum in df.columns():
    mean = df[colum].mean()
    max = df[colum].max()
    min = df[colum].min()
    posYerr = max - mean
    negYerr = mean - min
    storage_series = pd.Series([colum, mean, negYerr, posYerr, min, max], index = df_sample_results.columns)
    df_sample_results = pd.concat([df_sample_results, storage_series], axis=1)
    
df_sample_results.to_csv("Ergebnisssammlung_Härte_Auswertung_Proben.csv", index=False)

df_parameterset_results:DataFrame = pd.DataFrame(columns=["Parameterset","Mean","StDeviation","Min", "Max"])

for parameterset in parametersets:
    df_filter = df.filter(like=parameterset, axis=1)
    if df_filter.empty:
        continue
    mean = df_filter.mean()
    stdev = df_filter.std()
    max = df_filter.max()
    min = df_filter.min()
    storage_series = pd.Series([parameterset, mean, stdev, min, max], index = df_parameterset_results.columns)
    df_parameterset_results = pd.concat([df_parameterset_results, storage_series], axis=1)    

df_parameterset_results.to_csv("Ergebnisssammlung_Härte_Auswertung_Parameterset.csv", index=False)