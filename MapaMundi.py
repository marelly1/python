# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:55:20 2020

@author: Marelly
"""

%load_ext google.colab.data_table
import pandas as pd
url="https://raw.githubusercontent.com/marelly1/pandas/master/totalescv.csv"

df=pd.read_csv(url)
df=df.T
df=df.drop(["date"])
df=df.reset_index()
df=df.rename({"index":"Paises",53:"Total"},axis=1)
print(list(df))

!pip install pycountry
