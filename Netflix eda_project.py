import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("netflix_titles.csv")
""" print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
 print(df.describe())
print(df.isnull().sum()) """
""" df["director"]=df["director"].fillna(df["director"].mode()[0])
df["cast"]=df["cast"].fillna(df["cast"].mode()[0])
df["country"]=df["country"].fillna(df["country"].mode()[0])
df["date_added"]=df["date_added"].fillna(df["date_added"].mode()[0])
df["rating"]=df["rating"].fillna(df["rating"].mode()[0])
df["duration"]=df["duration"].fillna(df["duration"].mode()[0])
print(df.isnull().sum()) """
print(df.info())
sns.countplot(x="rating",data=df)
plt.title("Countent Rating Distribution")
plt.show() # 
sns.countplot(x="type",data=df)
plt.title("Movies vs TV Shows Count" )
plt.show() # 
sns.countplot(x="release_year",data=df)
plt.title("Countent Released Each Year" )
plt.xticks(rotation=90)
plt.show() #
sns.countplot(x="rating",hue="type",data=df)
plt.title("Rate Distribution by Type " )
plt.xticks(rotation=90)
plt.show() #
title_year=df.groupby("title")["release_year"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=title_year.index,y=title_year.values)
plt.title("Top 10 Titles by Release Year" )
plt.xticks(rotation=90)
plt.show() #
type_year=df.groupby("listed_in")["release_year"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=type_year.index,y=type_year.values)
plt.title("Top 10 Genres by Release Year" )
plt.xticks(rotation=90)
plt.show() #
sns.barplot(x="type",y="release_year",data=df)
plt.title("Average Release Year by Type" )
plt.show() #
sns.barplot(x="rating",y="release_year",data=df)
plt.title("Average Release Year by Rating" )
plt.show() #
sns.histplot(x="release_year",data=df)
plt.title("Distribution of Release Year" )
plt.show() #
sns.boxplot(y="release_year",data=df)
plt.title("Spread of Release Year" )
plt.show() #
sns.scatterplot(df["release_year"])
plt.title("Release Year Scatter plot " )
plt.show() #
numeric_df=df.select_dtypes(include=np.number)
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(),annot=True,cmap="coolwarm")
plt.title("correlation Heatmap")
plt.show() #