# -*- coding: utf-8 -*-
"""EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10aqYRsEGIw19NI37wEDLC6RTSYQxk0fi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/cleaned_smartphone_dataset.csv')

#brand(top 10)
df['brand'].value_counts().head(10).plot(kind='bar')

df['brand'].value_counts().head(10).plot(kind='pie',autopct='%0.1f%%')

df['os'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['os'].value_counts().head().plot(kind='bar',figsize=(10,5))

df

df['has_5G'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['has_NFC'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df.drop('has_IR_Blaster',axis=1,inplace=True)

df

df['processor_brand'].value_counts().plot(kind='pie',autopct='%0.1f%%')

# top 10 processor brand
df['processor_brand'].value_counts().head(10).plot(kind='bar')

#1 - yes
#0 - no
df['extended_memory_available'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['price'].describe()

sns.distplot(df['price'])

sns.boxplot(df['price'])

# here are some phone who have gold plating that's why thier price is very high
#  they will not contribute in pridiction of price(427,887)
df[df['price'] > 200000]

df['rating'].describe()

df[df['rating'].isnull()]['brand'].value_counts()

df['rating'].plot(kind='box')

sns.distplot(df['rating'])

df['rating'].skew()

df['Ram'].describe()

df['Ram'].plot(kind='box')

df['Ram'].plot(kind='kde')

df['Ram'].skew()

df['internal_storage'].describe()

df['internal_storage'].plot(kind='box')

df['internal_storage'].plot(kind='kde')

df['internal_storage'].skew()

#battery_capacity
df['battery_capacity'].describe()

df['battery_capacity'].plot(kind='box')

df[df['battery_capacity'] > 7000]

df['battery_capacity'].plot(kind='kde')

df['battery_capacity'].skew()

# bivariate analysis
#price vs brand name
x=df.groupby('brand').count()['model']

x[x>10].index

temp_df=df[df['brand'].isin(x[x>10].index)]

plt.figure(figsize=(15,8))
sns.barplot(x='brand',y='price',data=temp_df)

sns.scatterplot(x='rating',y='price',data=df)

sns.scatterplot(x='Ram',y='price',data=df)

sns.scatterplot(x='internal_storage',y='price',data=df)

sns.barplot(x='os',y='price',data=df,estimator=np.median)

sns.barplot(x='has_5G',y='price',data=df,estimator=np.median)

sns.barplot(x='has_NFC',y='price',data=df,estimator=np.median)

sns.scatterplot(x='processor_speed',y='price',data=df)

sns.barplot(x='num_core',y='price',data=df,estimator=np.median)

sns.scatterplot(x='battery_capacity',y='price',data=df)

sns.scatterplot(x='fast_charging',y='price',data=df)

sns.scatterplot(x='screen_size',y='price',data=df)

sns.barplot(x='num_rear_camera',y='price',data=df)

a=df.corr(numeric_only=True)['price'].reset_index()

x_df=df.select_dtypes(exclude='object').drop('price',axis=1)

from sklearn.impute import KNNImputer

imputer=KNNImputer(n_neighbors=5)

x_df_values=imputer.fit_transform(x_df)

x_df=pd.DataFrame(x_df_values,columns=x_df.columns)

x_df['price']=df['price']

b=x_df.corr()['price'].reset_index()

a

a.merge(b,on='index')

c=df.corr(numeric_only=True)

sns.heatmap(c)