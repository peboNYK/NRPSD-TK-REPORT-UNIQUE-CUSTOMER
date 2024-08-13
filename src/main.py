import pandas as pd
import hashlib
import os
from time import process_time

# Function to mask the data with an sha256 hash
def mask_with_sha256(data):
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()


# start time
print("start processing")
start_time = process_time() 
data_path ='data'
masked_data_path = 'masked_data'

for filename in os.listdir(data_path):
    print(filename)
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(data_path + '/' + filename, quoting=3, escapechar='\\')   
    #  Clean the column names
    df.columns = df.columns.str.strip('"')
    # Apply the masking function to the "R.principal" column
    df['R.principal'] = df['R.principal'].apply(mask_with_sha256)
    # Save the modified DataFrame back to a new CSV file
    df.to_csv(masked_data_path + '/' + 'masked_'+ filename , index=False, quoting=3, escapechar='\\')

# stop time
stop_time = process_time()
print("processing done: ", stop_time - start_time ,"seconds")


