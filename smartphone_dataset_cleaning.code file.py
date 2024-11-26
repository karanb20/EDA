# -*- coding: utf-8 -*-
"""smartphone dataset cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zmgeHlMukG4yL69R0I54mUEfXQOIZyM6
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/smartphones - smartphones.csv')
df

#make a copy
df1=df.copy()

# price column manipulation
df1['price'] =df1['price'].str.replace('₹','').str.replace(',','').astype(int)
df1

df1=df1.reset_index()

# making our indexs same as excel file
df1['index'] = df1['index'] + 2

processor_row=set((642, 647, 649, 659, 667, 701, 750, 759, 819, 859, 883, 884, 919, 927, 929, 932, 1002))
ram_rows=set((441, 485, 534, 553, 584, 610, 613, 642, 647, 649, 659, 667, 701, 750, 759, 819, 859, 884, 919, 927, 929, 932, 990, 1002))
display_rows=set((378, 441, 450, 553, 584, 610, 613, 630, 642, 647, 649, 659, 667, 701, 750, 759, 764, 819, 859, 884, 915, 916, 927, 929, 932, 990, 1002))
battery_rows=set((113, 151, 309, 365, 378, 441, 450, 553, 584, 610, 613, 630, 642, 647, 649, 659, 667, 701, 750, 756, 759, 764, 819, 855, 859, 884, 915, 916, 927, 929, 932, 990, 1002))
camera_rows=set((100, 113, 151, 157, 161, 238, 273, 308, 309, 323, 324, 365, 367, 378, 394, 441, 450, 484, 506, 534, 553, 571, 572, 575, 584, 610, 613, 615, 630, 642, 647, 649, 659, 667, 684, 687, 705, 711, 723, 728, 750, 759, 764, 792, 819, 846, 854, 855, 858, 859, 883, 884, 886, 915, 916, 927, 929, 932, 945, 956, 990, 995, 1002, 1016))

# we saw that some of the phones are not smartphone by doing union of all the problmatic rows and then by finding the mean of price we saw that phones below price 3400 are not smartphone so we have no use of them
df1=df1[df1['price']>3400]

df1[df1['index'].isin(processor_row)]

df1.drop([645,857,882,925],inplace=True)

df1[df1['index'].isin(ram_rows)]

df1.drop(582,inplace=True)

df1[df1['index'].isin(battery_rows)]

df1.drop([376,754],inplace=True)

temp_df=df1[df1['index'].isin(battery_rows)]

x=temp_df.iloc[:,7:].shift(1,axis=1).values
x

temp_df.iloc[:,7:]=x

df1.loc[temp_df.index,temp_df.columns[7:]]=x

df1[df1['index'].isin(camera_rows)]

df1.drop([155,271],inplace=True)

temp_df=df1[df1['index'].isin(camera_rows)]

temp_df=temp_df[~temp_df['camera'].str.contains('MP')]

df1.loc[temp_df.index,'camera']=temp_df['card'].values

df1['card'].value_counts()

temp_df=df1[df1['card'].str.contains('MP')]

df1.loc[temp_df.index,'card']= "Memory Card Not Supported"

temp_df= df1[~df1['card'].str.contains('Memory Card')]

df1.loc[temp_df.index,'os']=temp_df['card'].values

df1.loc[temp_df.index,'card']= "Memory Card Not Supported"

temp_df=df1[df1['os'].str.contains('upto')]

temp_df['card'] = temp_df['os'].shift()
temp_df['os']= np.nan

df1.loc[temp_df.index,'card']=temp_df['card'].values

(df1[df1['os'].str.contains('upto')])['os']= np.nan

df1['os'].value_counts()

temp_df=df1[df1['os'].str.contains('Memory Card')]

df1.loc[temp_df.index,'os']= np.nan

temp_df= df1[df1['os']=='Bluetooth']

df1.loc[temp_df.index,'os']= np.nan

df1['model'].value_counts()

temp_df=df1['model'].str.lower()

df1['brand']=temp_df.str.split(' ').str[0]

a=df1['sim'].str.split(',')

temp_df=df1.copy()

temp_df['has_5G'].value_counts()

temp_df['has_5G'] = temp_df['sim'].isin(a)

def check(a):
  if '5G' in a:
    return True
  else:
    return False
temp_df['has_5G']=temp_df['sim'].apply(check)

def check(a):
  if '5G' in a:
    return True
  else:
    return False
df1['has_5G']=df1['sim'].apply(check)

def check(a):
  if 'NFC' in a:
    return True
  else:
    return False
df1['has_NFC']=df1['sim'].apply(check)

def check(a):
  if 'IR Blaster ' in a:
    return True
  else:
    return False
df1['has_IR_Blaster']=df1['sim'].apply(check)

temp_df.drop('sim',axis=1,inplace=True)

df1.drop('sim',axis=1,inplace=True)

a=temp_df['processor'].str.split(' ').str[0]

df1['processor_brand']=a

a=df1['processor'].str.split(',').str[0].value_counts()
a.sum()

df1.shape

df1['ram'].value_counts()

df1[df1['ram']=='512 MB RAM, 4 GB inbuilt']

df1[df1['ram']== '64 MB RAM, 128 MB inbuilt']

df1.drop(627,inplace=True)

df1['ram'] = df1['ram'].str.strip()

df1.loc[483,'ram']='12 GB RAM , 512 GB inbuilt'
df1.loc[439,'ram']='4 GB RAM , 64 GB inbuilt'
df1.loc[762,'ram']='8 GB RAM , 64 GB inbuilt'

df1[df1['ram']== '6 GB RAM, 1 TB inbuilt']

df1.loc[290,'ram']='6 GB RAM , 1000 GB inbuilt'
df1.loc[781,'ram']='6 GB RAM , 1000 GB inbuilt'
df1.loc[814,'ram']='6 GB RAM , 1000 GB inbuilt'
df1.loc[961,'ram']='6 GB RAM , 1000 GB inbuilt'

df1[df1['ram']== '12 GB RAM, 1 TB inbuilt']

df1.loc[943,'ram']='12 GB RAM , 1000 GB inbuilt'

df1['Ram'] = df1['ram'].str.split(',').str[0].str.extract('(\d+)', expand=False)

df1['Ram'].value_counts()

df1['internal_storage'] = df1['ram'].str.split(',').str[1].str.extract('(\d+)', expand=False)

df1['internal_storage'].value_counts()

df1.drop(486,inplace=True)

df1['Ram'].astype(float)

df1['internal_storage'].astype(float)

df1['processor'].str.split(',').str[1].value_counts()

a=df1['processor'].str.split(',')

def num(a):
  if 'Octa' in a:
    return '8'
  if 'Hexa' in a:
    return '6'
  if 'Quad' in a:
    return '4'
  if 'Dual' in a:
    return '2'
  else:
    return np.nan
df1['num_core']=df1['processor'].apply(num)

df1['num_core'].value_counts().sum()

df1['processor_speed']=df1['processor'].str.split(',').str.get(2).str.split(' ').str.get(1).str.replace('GHz','').astype(float)

df1.loc[143,'processor_speed']= '1.4'
df1.loc[188,'processor_speed']= '1.6'
df1.loc[201,'processor_speed']= '2'
df1.loc[309,'processor_speed']= '2'
df1.loc[315,'processor_speed']= '1.3'
df1.loc[587,'processor_speed']= '2'
df1.loc[758,'processor_speed']= '1.6'
df1.loc[778,'processor_speed']= '2.2'
df1.loc[794,'processor_speed']= '1.3'
df1.loc[991,'processor_speed']= '1.8'
df1.loc[1005,'processor_speed']= '1.3'

df1['num_core'].astype('float')
df1['processor_speed'].astype('float')

df1['battery_capacity']=df1['battery'].str.split(' ').str.get(0).str.replace('mAh','').astype(float)

a=df1['battery'].str.split(' ')
a

# Extract both integer and decimal Wattage values
df1['fast_charging'] = df1['battery'].str.extract(r'(\d+\.?\d*W)', expand=False)

df1['fast_charging'].str.replace('W','').astype(float)

df1['screen_size']=df1['display'].str.split(',').str.get(0).str.split(' ').str.get(0).astype(float)

df1['resolution']=df1['display'].str.split(',').str.get(1).str.split(' ').str.get(1)

a=df1['camera'].str.split(' ')
a

def check(a):
  if 'Triple' in a:
    return '3'
  if 'Quad' in a:
    return '4'
  if 'Dual' in a:
    return '2'
  else:
    return '1'
df1['num_rear_camera']=df1['camera'].apply(check)

df1['num_rear_camera']=df1['num_rear_camera'].astype(float)

df1['primary_rear_camera']=df1['camera'].str.split(',').str.get(0).str.split(' ').str.get(0).str.replace('MP','')

df1.loc[69,'primary_rear_camera']= '50'
df1.loc[894,'primary_rear_camera']= '64'

df1['primary_rear_camera']=df1['primary_rear_camera'].astype(float)

df1.loc[894,'camera']= '64 MP + 16 MP + 8 MP Triple Rear Camera & 32 MP Front Camera'
df1.loc[69,'camera']= '50 MP + 16 MP + 8 MP Triple Rear Camera & 32 MP Front Camera'

df1['primary_front_camera']=df1['camera'].str.split('&').str.get(1).str.split(' ').str.get(1).str.replace('MP','')

df1.loc[613,'primary_front_camera']= '20'

df1['primary_front_camera']=df1['primary_front_camera'].astype(float)

df1

df1['fast_charging']=df1['fast_charging'].str.replace('W','').astype(float)

df1['os']=df1['os'].str.split(' ').str.get(0)

df1['os']=df1['os'].str.replace('HarmonyOS','Harmony')

df1['os'].value_counts()

a=df1['card'].str.split(' ')

def check(a):
  # Handle None values explicitly
  if a is None:
    return '0'  # Or any other suitable value for None cases
  if 'upto' in a:
    return '1'
  else:
    return '0'

df1['extended_memory_available'] = df1['card'].apply(check)

df1['extended_memory_available'].value_counts()

pd.set_option('display.max_rows', None)

a

df1['extended_upto']=df1['card'].str.extract(r'(\d+)', expand=False)

# Ensure the column values are converted to numeric where possible, errors will result in NaN
df1['extended_upto'] = pd.to_numeric(df1['extended_upto'], errors='coerce')

# Replace all occurrences of 1 with 1024
df1['extended_upto'] = df1['extended_upto'].replace(1, 1024)
df1['extended_upto'] = df1['extended_upto'].replace(2, 2048)

# Display the updated DataFrame

df1

df1.drop(columns=['index','processor','ram','battery','display','camera','card'],inplace=True)

df1.to_csv('cleaned_dataset.csv', index=True)  # Save the file without including the index

from google.colab import files
files.download('cleaned_dataset.csv')  # Initiate download