import numpy as np
import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")
Geograpgy = df.Geography
Geograpgy=pd.get_dummies(Geograpgy)
Geograpgy=Geograpgy.drop(columns=['Germany'])
extracted_col = Geograpgy['France']
extracted_col2 = Geograpgy['Spain']
df=df.drop(columns=['Geography'])
df.insert(4,'France',extracted_col)
df.insert(5,'Spain',extracted_col2)
df.to_csv('plik.csv',sep=',')



print(df['France'])

# w katalogu tworzony jest folder zawierajacy poprawione kolumny
