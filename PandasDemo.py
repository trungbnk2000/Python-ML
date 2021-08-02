import pandas as pd
import numpy as np
from IPython.display import display

# data = pd.read_csv('Advertising.csv')

# arr = pd.Series([1, 2, 4, 5])

area_dict = {'Ha Noi': 2001, 'TP.HCM': 1312, 'Da Nang': 1234, 'Nha Trang': np.nan}
population_dict = {'Ha Noi': 9012, 'TP.HCM': 5912, 'Da Nang': np.nan, 'Nha Trang': 1021}

area = pd.Series(area_dict)
population = pd.Series(population_dict)

print(area)
# Tao Dataframe tu dictionary
df = pd.DataFrame({'Dan so': population, 'Dien tich': area})

print(df)
# Dataframe giong nhu mang hai chieu
print(df.index)
print(df.columns)
print('Dan so cua Ha Noi la :', df['Dan so']['Ha Noi'])

df['Mat do'] = df['Dan so'] / df['Dien tich']

df = df.fillna(axis=0, method='ffill')
display(df)
