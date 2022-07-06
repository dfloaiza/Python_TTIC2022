import pandas as pd

#cargar el data frame tal como viene:
df_v1 = pd.read_csv("bikes_dirty.csv", 
                    sep=';', 
                    encoding='latin1', 
                    infer_datetime_format=True,
                    dayfirst=True,
                    parse_dates=['Fecha'])

#ver información previa del dataset                    
print(df_v1.info())

df_v1.dropna(inplace=True,
             axis=1,
             how='all' #all, any
)
print(df_v1.info())

#datos atipicos:
rows = df_v1.shape[0]
print(rows)

c6_st_dev = df_v1['Cra. 1'].std(axis=0)

print(c6_st_dev)
c6_mean = df_v1['Cra. 1'].mean()

#outliers y formato erróneo
for i in range(0, rows):
    if df_v1.iloc[i,7] >= 2*c6_st_dev:
        df_v1.iloc[i,7] = c6_mean
    #df_v1.iloc[i,0] = pd.to_datetime(df_v1.iloc[i,0], infer_datetime_format=True)

df_v1['Fecha'] = pd.to_datetime(df_v1['Fecha'])

#duplicados   
print("Duplicados:")
print(df_v1.duplicated())

df_v1.drop_duplicates(inplace=True)

df_v1 = df_v1.set_index(['Fecha'])

df_v1_9a = df_v1[ ['Calle 9a (66-39)'] ].copy()

print("Datos de la 9a:")
print(df_v1_9a)
 
print(df_v1.info())
