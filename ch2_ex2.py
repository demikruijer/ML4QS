import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data 
our_data = pd.read_csv('datasets/ourdata/final_dataset.csv')
their_data = pd.read_csv('intermediate_datafiles/chapter2_result.csv')

def add_seconds_column(dataset):
    dataset.rename(columns = {'Unnamed: 0':'date'}, inplace = True)

    # convert date column to seconds MANUALLY (huilen)
    dataset['seconds'] = pd.Series([(float(val[11:13])*60*60+float(val[14:16])*60+float(val[17:])) 
        for val in dataset['date']])
    dataset['time'] = dataset['seconds']-dataset['seconds'][0]
    return dataset

def select_activity(dataset,col,activity):
    subset = dataset[dataset[col]==activity]
    return subset

def generalize_activity_names(dataset):
    # replace activity labels in data set with one type for every activity
    dataset = dataset.replace(['staan_2','lopen_1','lopen_2','fietsen_2' ,'liggen_2' ,'liggen_3','trap_op_2' ,'trap_af_2'],
        ['staan','lopen','lopen','fietsen','liggen','liggen','trap_op','trap_af'])
    return dataset

def add_cont_time(dataset,stepsize):
    # add column with time steps based on sampling frequency translated to stepsize
    dataset['cont_time'] = np.arange(0,len(dataset)*stepsize,stepsize)
    return dataset

def change_granularity(dataset, downgrade_factor):
    transformed_dataset = dataset.groupby(np.arange(len(dataset))//downgrade_factor).mean()
    return transformed_dataset

def select_time_domain(dataset, endtime):
    new_dataset = dataset[dataset['cont_time'] < endtime]
    return new_dataset

def add_normalized_col(dataset, col):
    dataset[col+'_norm'] = dataset[col]-dataset[col].mean()
    return dataset

# add seconds column to their data set
their_data = add_seconds_column(their_data)

# generalize activity names for our data set
our_data = generalize_activity_names(our_data)

# select activity walking for both data sets
their_data = select_activity(their_data,'labelWalking',1)
our_data = select_activity(our_data,'activity','lopen')

# add continuous time column 
their_data = add_cont_time(their_data,0.25)
our_data = add_cont_time(our_data,0.1)

# change granularity to 1 sec for both data sets
our_data = change_granularity(our_data,10)
their_data = change_granularity(their_data,4)

# select time range of 900 sec (15 minutes) for both data sets 
timerange = 900 
our_data = select_time_domain(our_data, timerange)
their_data = select_time_domain(their_data, timerange)

# add a normalized column of the measurement data you want to consider
our_data = add_normalized_col(our_data, 'x_Accelerometer')
their_data = add_normalized_col(their_data,'acc_phone_x')

# plot the two data sets in one plot
plt.plot(our_data.cont_time, our_data.x_Accelerometer_norm,label='our data')
plt.plot(their_data.cont_time, their_data.acc_phone_x_norm,label='their data')
plt.legend(fontsize=12)
plt.title('Comparison of accelerometer x', fontsize=15)
plt.yticks(fontsize=12) 
plt.xlabel('time in seconds', fontsize=12)
plt.xticks(fontsize=12) 
plt.show()
