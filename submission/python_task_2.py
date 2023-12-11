#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[5]:


def calculate_distance_matrix(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Create a dictionary to store cumulative distances
    distance_dict = {}

    # Iterate through the rows of the DataFrame to calculate cumulative distances
    for index, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']

        # Bidirectional distances (A to B is equal to B to A)
        distance_dict[(start_id, end_id)] = distance_dict.get((start_id, end_id), 0) + distance
        distance_dict[(end_id, start_id)] = distance_dict.get((end_id, start_id), 0) + distance

    # Convert the dictionary to a DataFrame
    distance_matrix = pd.DataFrame(distance_dict.values(), index=pd.MultiIndex.from_tuples(distance_dict.keys())).unstack()

    # Replace NaN values with 0 (for locations without direct connections)
    distance_matrix = distance_matrix.fillna(0)

    # Set diagonal values to 0
    distance_matrix.values[[range(distance_matrix.shape[0])]*2] = 0

    return distance_matrix


# In[6]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-3.csv"
calculate_distance_matrix(file_path)


# In[7]:


def unroll_distance_matrix(Data_Frame):
    # Extract index and column names from the input DataFrame
    id_start = Data_Frame.index.tolist()
    id_end = Data_Frame.columns.tolist()

    # Create a DataFrame to store unrolled distances
    unrolled_distances = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    # Iterate through the rows and columns of the input DataFrame
    for start_id in id_start:
        for end_id in id_end:
            # Skip diagonal values (same id_start to id_end)
            if start_id != end_id:
                distance = data_Frame.loc[start_id, end_id]
                unrolled_distances = unrolled_distances.append({'id_start': start_id, 'id_end': end_id, 'distance': distance}, ignore_index=True)

    return unrolled_distances


# In[11]:


file_path="C:\\Users\\anagdeo\\Downloads\\dataset-3.csv"
Data_Frame = calculate_distance_matrix(file_path)
unroll_distance_matrix(Data_Frame)


# In[15]:


def calculate_toll_rate(distance_df):
    # Define rate coefficients for each vehicle type
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    # Iterate through the rate coefficients and calculate toll rates for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = f'{vehicle_type}_rate'
        distance_df[column_name] = distance_df['distance'] * rate_coefficient

    return distance_df


# In[16]:


distance_df = unroll_distance_matrix(Data_Frame)
calculate_toll_rate(distance_df)

