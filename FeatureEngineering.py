# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

# Please change the file location as needed
file_location = "./data.csv"
data = pd.read_csv(file_location)
# Please change the label to match dataset
label = 'label'


# %%
# Rearrage the dataset columns
cols = data.columns.tolist()
colIdx = data.columns.get_loc(label)
cols


# %%
# Do nothing if the label is in the 0th position
# Otherwise, change the order of columns to move label to 0th position
if colIdx != 0:
    cols = cols[colIdx:colIdx+1] + cols[0:colIdx] + cols[colIdx+1:]
# Change the order of data so that label is in the 0th column
modified_data = data[cols]
modified_data


# %%
tmpCol = modified_data[label].astype('category')
dict_encoding = { label: dict(enumerate(tmpCol.cat.categories))}
dict_encoding


# %%
modified_data[label] = tmpCol.cat.codes
modified_data


# %%
unknown_columns = ["filename"]
dataset = modified_data.drop(unknown_columns, axis=1)
dataset


# %%
from sklearn.model_selection import train_test_split
train, test = train_test_split(dataset, test_size=0.2, random_state=42)
train.to_csv('train1.csv', index=False, header=False)
test.to_csv('test1.csv', index=False, header=False)


# %%



# %%



