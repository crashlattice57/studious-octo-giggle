# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:00:27 2023

@author: damia
"""

from stop_words import stop_words
import pandas as pd
df = pd.read_csv("../cyber-operations-incidents.csv")

#remove targeting of from Title column
df["Title"] = df["Title"].apply(lambda x: x.replace("Targeting of","").strip())

#parse Date column and separate into multiple columns of Day, Month, Year

df[["Month", "Day", "Year"]] = df["Date"].str.split("/", expand = True)
df["Date"] = pd.to_datetime(df["Date"])

#Explode the category column to split column seperated features

df = df.assign(Category=df["Category"].str.split(",")).explode("Category")
df["Category"] = df["Category"].apply(lambda x: str(x).strip())


#Remove stop words and additional words from the Affiliations column using stop_words file
df['Affiliations'] = df['Affiliations'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stop_words)]))


#Merge the 3 Sources Columns into 1 single column named Sources

df = df.melt(id_vars=["Title","Date", "Affiliations", "Description", "Response", "Victims", "Sponsor", "Type", "Category", "Month", "Day", "Year"], value_vars=["Sources_1", "Sources_2", "Sources_3"], var_name="Value", value_name="Sources")
df.drop("Value",axis=1,inplace=True)