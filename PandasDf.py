import pandas as pd
import numpy as np

pd.set_option('max_colwidth', 40)
pd.set_option('precision', 5)
pd.set_option('max_rows', 10)
pd.set_option('max_columns', 30)

df = pd.read_csv("https://raw.githubusercontent.com/phamdinhkhanh/datasets/master/Churn_Modelling.csv", sep=",",
                 header=0,
                 index_col=None)
print('Data được lấy từ file csv\n', df)

print('Chỉ số trung bình cho từng cột\n')
avg_dict = {"RowNumber": df['RowNumber'].mean(), "CreditScore": df['CreditScore'].mean(), "Age": df['Age'].mean(), "EstimatedSalary": df['EstimatedSalary'].mean()}
print(pd.Series(avg_dict),'\n')

df_group = df.groupby('Geography')['CreditScore'].mean()
print('Average credit score group by Geography\n', df_group)
