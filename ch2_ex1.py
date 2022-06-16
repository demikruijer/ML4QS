import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data 
data = pd.read_csv('datasets/ourdata/final_dataset.csv')

def generalize_activity_names(dataset):
    # replace activity labels in data set with one type for every activity
    dataset = dataset.replace(['staan_2','lopen_1','lopen_2','fietsen_2' ,'liggen_2' ,'liggen_3','trap_op_2' ,'trap_af_2'],
        ['staan','lopen','lopen','fietsen','liggen','liggen','trap_op','trap_af'])
    return dataset

def visualize_results(df):
    total_plots = 5
    number_size = 15
    letter_size = 12

    # create columns indicating activity labels for activity plot
    for activity in df['activity'].unique():
        df[activity] = np.where(df.activity == activity, 1, None)

    # plot gyroscope data
    plt.subplot(total_plots,1,1)
    plt.plot(df.time, df.x_Gyroscope,label='x_gyr')
    plt.plot(df.time, df.y_Gyroscope,label='y_gyr')
    plt.plot(df.time, df.z_Gyroscope,label='z_gyr')
    plt.legend(bbox_to_anchor=(1.1, 0.8), fontsize=letter_size)    
    plt.yticks(fontsize=number_size) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot linear acceleration data
    plt.subplot(total_plots,1,2)
    plt.plot(df.time, df.x_LinearAcceleration,label='x_lin')
    plt.plot(df.time, df.y_LinearAcceleration,label='y_lin')
    plt.plot(df.time, df.z_LinearAcceleration,label='z_lin')
    plt.legend(bbox_to_anchor=(1.1, 0.8), fontsize=letter_size)    
    plt.yticks(fontsize=number_size) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot magnetometer data
    plt.subplot(total_plots,1,3)
    plt.plot(df.time, df.x_Magnetometer,label='x_mag')
    plt.plot(df.time, df.y_Magnetometer,label='y_mag')
    plt.plot(df.time, df.z_Magnetometer,label='z_mag')
    plt.legend(bbox_to_anchor=(1.1, 0.8), fontsize=letter_size)    
    plt.yticks(fontsize=number_size) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot illuminance data
    plt.subplot(total_plots,1,4)
    plt.plot(df.time, df.Illuminance,label='lum')
    plt.legend(bbox_to_anchor=(1.1, 0.8), fontsize=letter_size)    
    plt.yticks(fontsize=number_size) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot activities
    plt.subplot(total_plots,1,5)
    plt.scatter(df.time, df.fietsen, label='biking')
    plt.scatter(df.time, df.liggen, label='laying')
    plt.scatter(df.time, df.staan, label='standing')
    plt.scatter(df.time, df.lopen, label='walking')
    plt.scatter(df.time, df.trap_op, label='stairs up')
    plt.scatter(df.time, df.trap_af, label='stairs down')
    plt.scatter(df.time, df.rennen, label='running')
    plt.scatter(df.time, df.bureau, label='on desk')
    plt.legend(bbox_to_anchor=(1.1, 1.1), fontsize=letter_size)    
    plt.xlabel('time in seconds', fontsize=letter_size)
    plt.xticks(fontsize=number_size) 
    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.show() 


# generalize names of activities in data set 
data = generalize_activity_names(data)
# visualize results for original data
visualize_results(data)

# transform granularity of the data: set downgrading factor  
downgrade_factor = 600 # 600 for dT of 1 min 
# take average of every group of rows 
data_transformed = data.groupby(np.arange(len(data))//downgrade_factor).mean()
# manually add the activities column again 
data_transformed['activity'] = np.array(data.iloc[::downgrade_factor]['activity'])
# visualize results for transformed data 
#visualize_results(data_transformed)

# transform granularity to 1 sec
downgrade_factor = 10 # 600 for dT of 1 min 
data_transformed1 = data.groupby(np.arange(len(data))//downgrade_factor).mean()
data_transformed1['activity'] = np.array(data.iloc[::downgrade_factor]['activity'])
#visualize_results(data_transformed1)

# transform granularity to 10 sec
downgrade_factor = 100 # 600 for dT of 1 min 
data_transformed10 = data.groupby(np.arange(len(data))//downgrade_factor).mean()
data_transformed10['activity'] = np.array(data.iloc[::downgrade_factor]['activity'])
#visualize_results(data_transformed10) 

# visualize granularity differences
plt.plot(data.time, data.x_Magnetometer,label='0.1 sec')
plt.plot(data_transformed1.time, data_transformed1.x_Magnetometer,label='1 sec')
plt.plot(data_transformed10.time, data_transformed10.x_Magnetometer,label='10 sec')
plt.plot(data_transformed.time, data_transformed.x_Magnetometer,label='1 min')
plt.legend(bbox_to_anchor=(1.1, 0.8), fontsize=12)    
plt.xlabel('Magnetometer x for different granularities', fontsize=15)
plt.yticks(fontsize=15) 
plt.xlabel('time in seconds', fontsize=12)
plt.xticks(fontsize=15) 
plt.show()