import pandas as pd #type: ignore
from pandas import DataFrame,Series #type: ignore

df:DataFrame = pd.read_csv("Ergebnissammlung_Härte.csv")

parametersets:list[str] = ["2000","2100","2200","4000","2001", "2101", "2201", "4001"]

df_sample_results:DataFrame = pd.DataFrame(columns=["Sample","Mean","negYerr","posYerr","Min", "Max"])
for colum in df.columns:
    if df[colum].isnull().all():
        continue
    mean = df[colum].mean()
    max_value = df[colum].max()
    min_value = df[colum].min()
    posYerr = max_value - mean
    negYerr = mean - min_value
    storage_series = pd.Series([colum, mean, negYerr, posYerr, min_value, max_value], index = df_sample_results.columns)
    df_sample_results = pd.concat([df_sample_results, storage_series.to_frame().T])
    
df_sample_results.to_csv("Ergebnissammlung_Härte_Auswertung_Proben.csv", index=False)

df_parameterset_results:DataFrame = pd.DataFrame(columns=["Index","Parameterset","Mean","StDeviation","Min", "Max"]).set_index("Index")

for parameterset in parametersets:
    filtered_data :Series = df.filter(like=parameterset, axis=1).stack().reset_index(drop=True)
    if filtered_data.empty:
        continue
    mean = filtered_data.mean()
    stdev = filtered_data.std()
    max_value = filtered_data.max()
    min_value = filtered_data.min()
    storage_series = pd.Series([parameterset, mean, stdev, min_value, max_value], index = df_parameterset_results.columns)
    df_parameterset_results = pd.concat([df_parameterset_results, storage_series.to_frame().T])    

df_parameterset_results.to_csv("Ergebnissammlung_Härte_Auswertung_Parameterset.csv", index=False)