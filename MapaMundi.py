# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:55:20 2020

@author: Marelly
"""

%load_ext google.colab.data_table
import pandas as pd
url="https://raw.githubusercontent.com/marelly1/pandas/master/totalescv.csv"

import pandas as pd
url="https://raw.githubusercontent.com/marelly1/pandas/master/totalescv.csv"

df=pd.read_csv(url)
df=df.T
df=df.drop(["date"])
df=df.reset_index()
df=df.rename({"index":"Paises",53:"Total"},axis=1)
print(list(df))

#se debe instalar por el cmd de windows
#pip install pycountry

import pycountry
def get_alph_3(location):
  try:
    return pycountry.countries.get(name=location).alpha_3
  except:
    return None

df["Code"]=df["Paises"].apply(lambda x: get_alph_3(x))
print(df.head(6))

import plotly.express as px
fig = px.choropleth(df,locations="Code",color="Total",hover_name="Paises",color_continuous_scale=px.colors.sequential.Plasma)
fig.show()