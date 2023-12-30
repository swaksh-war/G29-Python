import pandas as pd
import numpy as np

class DataTransformer : 
    def __init__(self, dataset : pd.DataFrame = None, ignore_columns_to_transform : list[str] = None):
        self.ignored_cols = ignore_columns_to_transform
        self.data = dataset
        self.numerical_cols, self.categorical_cols = self.get_num_cat_cols()
        self.min_max_values = self.get_min_max_values()
        self.label_map = self.get_label_map()
    

    def get_num_cat_cols(self):
        cat_cols = []
        num_cols = []
        for column in self.data.columns:
            if self.data[column].dtype == object:
                cat_cols.append(column)
            else: 
                num_cols.append(column)
        return num_cols, cat_cols
    
    def get_min_max_values(self):
        temp_dict = {}

        for col in self.numerical_cols:
            col_min = self.data[col].min()
            col_max = self.data[col].max()
            temp_dict[col] = [col_min, col_max]
        return temp_dict
    
    def get_label_map(self):
        temp_label_map = {}
        for col in self.categorical_cols:
            unique_values = self.data[col].unique().tolist()
            k = 1
            col_label_map = {}
            for val in unique_values:
                col_label_map[val] = k
                k += 1
            
            temp_label_map[col] = col_label_map
        return temp_label_map

    def scale(self, col_name, x):
        min_val = self.min_max_values[col_name][0]
        max_val = self.min_max_values[col_name][1]
        scaled_x = (x - min_val) / (max_val - min_val)
        return scaled_x

    def encode(self, col_name, x):
        encoder_dict = self.label_map[col_name]
        return encoder_dict[x]

    def fit_transform(self):
        for col in self.numerical_cols:
            if col not in self.ignored_cols:
                self.data[col] = self.data[col].apply(lambda x: self.scale(col, x))
        
        for col in self.categorical_cols:
            if col not in self.ignored_cols:
                self.data[col] = self.data[col].apply(lambda x: self.encode(col, x))

        
    
