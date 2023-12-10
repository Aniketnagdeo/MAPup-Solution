#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[16]:


def generate_car_matrix(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Pivot the DataFrame to create the matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    car_matrix.values[[range(car_matrix.shape[0])]*2] = 0

    return car_matrix


# In[17]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-1.csv"
generate_car_matrix(file_path)


# In[20]:


def get_type_count(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Create a new categorical column 'car_type' based on values of the 'car' column
    conditions = [
        (df['car'] <= 15),
        ((df['car'] > 15) & (df['car'] <= 25)),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = np.select(conditions, choices, default='unknown')

    # Calculate the count of occurrences for each car_type category
    type_count = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_count = dict(sorted(type_count.items()))

    return type_count




# In[21]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-1.csv"
get_type_count(file_path)


# In[22]:


def get_bus_indexes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes


# In[23]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-1.csv"
get_bus_indexes(file_path)


# In[24]:


def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter routes based on the average of 'truck' column
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    # Sort the list of routes in ascending order
    filtered_routes.sort()

    return filtered_routes


# In[26]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-1.csv"
filter_routes(file_path)


# In[40]:


def multiply_matrix(Data_Frame):
    # Copy the original DataFrame to avoid modifying the original data
    modified_matrix = Data_Frame.copy()

    # Apply the specified logic to modify the values
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


# In[41]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-1.csv"
Data_Frame = generate_car_matrix(file_path)
multiply_matrix(Data_Frame) 


# In[ ]:




