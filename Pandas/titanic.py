import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df.head()
df.info()
df.query('Survived == 1').count()
df.columns
df.isna().sum()

df.drop(columns='Cabin', inplace=True)
df.info()
age_sans_na = df.dropna(axis=0, subset='Age')
age_sans_na.info()
df['Age'].fillna(df['Age'].mean())
df['Age'].mean()
# Visualisation de la survie par sexe
sns.catplot(x="Sex", kind="count", hue="Survived", data=df)
plt.title('Survie sur le Titanic par Sexe')
plt.show()
# Survie par classe de passager
sns.catplot(x="Pclass", y="Survived", kind="bar", data=df)
plt.title('Survie sur le Titanic par Classe de Passager')
plt.show()
# Distribution de l'âge en fonction de la survie
sns.violinplot(x="Survived", y="Age", data=age_sans_na)
plt.title('Distribution de l’Âge des Survivants et des Non-Survivants')
plt.show()
sns.scatterplot(data=age_sans_na, x='Age', y='Fare', hue='Survived')
plt.title('Chance de Survie en Fonction de l’Âge')
plt.xlabel('Âge')
plt.ylabel('Tarif')
plt.show()
sns.catplot(x="Embarked", kind="count", hue="Survived", data=df)
plt.title('Survie sur le Titanic par Port d’Embarquement')
plt.show()