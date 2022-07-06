import pandas as pd
import datetime

import matplotlib.pyplot as plt


#parametros de graficacion:
# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

#Cargar dataset:
df_bikes1 = pd.read_csv("bikes_dirty.csv",  #ruta del archivo plano
                         encoding="latin1", #juego de caracteres del archivo
                         sep=";",           #caracter usado como separador
                         parse_dates=['Fecha'],
                         dayfirst=True
                         )   

df_bikes1['Fecha'] = pd.to_datetime(df_bikes1['Fecha'], infer_datetime_format=True)
#ver info del dataset:
print(df_bikes1.info)

#ver dataset:
print(df_bikes1)

#limpiar dataset
#datos nulos
df_bikes1.dropna(axis=1,        #"axis" indica el eje en el cual se examinan los valores nulos: 0 = por columna, 1 = por fila
                 inplace=True,  #"inplace" indica que el cambio se aplica al propio dataframe
                 how='all')     #"how" indica el criterio para eliminar los datos. "all", elimina si todos los datos en el eje son nulos,
                                # "any", si encuentra al menos un valor nulo

#datos atípicos


# datos duplicados                                
                
                
#mostrar dataset limpio:
print(df_bikes1)

print(df_bikes1.index)

#establecer indice a la fecha
df_bikes1 = df_bikes1.set_index(['Fecha'])
print(df_bikes1)



#df_bikes1['Calle 9a (66-39)'].plot(kind='line')
#plt.suptitle="Calle 9a"
#plt.show()

df_bikes1_9a = df_bikes1[['Calle 9a (66-39)']].copy()#
print(df_bikes1_9a)

#print(df_bikes1.index)
print(df_bikes1_9a.index)

#df_bikes1_9a.loc[:'DiaSemana'] = df_bikes1_9a.index.weekday
#df_bikes1_9a['DiaSemana'] = df_bikes1_9a['Fecha'].dt.day_name()

df_bikes_9a_cnt = df_bikes1_9a.groupby(['Fecha']).aggregate(sum)
#print(df_bikes1_9a['Fecha'])
print(df_bikes_9a_cnt)
