import pandas as pd
import numpy as np
from CustomDataTransformer import DataTransformer

data =pd.read_csv('newData.csv')

cdt = DataTransformer(data, ignore_columns_to_transform=['Price', 'Seats', 'Unnamed: 0'])


print(cdt.categorical_cols, cdt.numerical_cols)
print('\n\n\n\n\n')
print(cdt.min_max_values)
print('\n\n\n\n')
print(cdt.label_map)
cdt.fit_transform()
print(cdt.data.head())