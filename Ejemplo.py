# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:57:10 2020

@author: Marelly
"""
import pandas as pd 
import matplotlib.pyplot as plt

datos=pd.read_csv("https://raw.githubusercontent.com/marelly1/pandas/master/ArtJan2018resumido.csv",encoding="Latin-1")
df=pd.DataFrame(datos)

#  01/30/18 11:37 PM es el formato que se ve en el archivo original
df["fecha"]=df["pubDate"].str.extract("(../../..)",expand=True)
print(df["fecha"])

#esto es mostrando un gráfico
datos=pd.read_csv("https://raw.githubusercontent.com/marelly1/pandas/master/Ejemplo.csv")
df=pd.DataFrame(datos)

df["hora"]=df["fecha"].str.extract("(..:..:..)",expand=True)
print(df["hora"])

df["hora"]=pd.to_datetime(df["hora"])
df["hora 1"]=pd.to_datetime(df["hora 1"])
df["diferencia"]=df["hora"]-df["hora 1"]
print(df["diferencia"])

plt.plot(df["hora"],df["valor 2"],"-")
# .xticks() esto va hacer que el valor de las horas saldrá ladeado para que se vea mejor
_=plt.xticks(rotation=45)
plt.show()

