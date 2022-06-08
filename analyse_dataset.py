import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data 
data = pd.read_csv('datasets/ourdata/final_dataset.csv')

def visualize_results(df):
    total_plots = 6

    # create columns indicating activity labels for activity plot
    for activity in df['activity'].unique():
        df[activity] = np.where(df.activity == activity, 1, None)

    # plot accelerometer data
    plt.subplot(total_plots,1,1)
    plt.plot(df.time, df.x_Accelerometer,label='x_acc')
    plt.plot(df.time, df.y_Accelerometer,label='y_acc')
    plt.plot(df.time, df.z_Accelerometer,label='z_acc')
    plt.legend(bbox_to_anchor=(1.1, 0.8))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot gyroscope data
    plt.subplot(total_plots,1,2)
    plt.plot(df.time, df.x_Gyroscope,label='x_gyr')
    plt.plot(df.time, df.y_Gyroscope,label='y_gyr')
    plt.plot(df.time, df.z_Gyroscope,label='z_gyr')
    plt.legend(bbox_to_anchor=(1.1, 0.8)) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot linear acceleration data
    plt.subplot(total_plots,1,3)
    plt.plot(df.time, df.x_LinearAcceleration,label='x_lin')
    plt.plot(df.time, df.y_LinearAcceleration,label='y_lin')
    plt.plot(df.time, df.z_LinearAcceleration,label='z_lin')
    plt.legend(bbox_to_anchor=(1.1, 0.8)) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot magnetometer data
    plt.subplot(total_plots,1,4)
    plt.plot(df.time, df.x_Magnetometer,label='x_mag')
    plt.plot(df.time, df.y_Magnetometer,label='y_mag')
    plt.plot(df.time, df.z_Magnetometer,label='z_mag')
    plt.legend(bbox_to_anchor=(1.1, 0.8)) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot illuminance data
    plt.subplot(total_plots,1,5)
    plt.plot(df.time, df.Illuminance,label='lum')
    plt.legend(bbox_to_anchor=(1.1, 0.8)) 
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # plot activities
    plt.subplot(total_plots,1,6)
    plt.scatter(df.time, df.fietsen, label='fietsen')
    plt.scatter(df.time, df.liggen, label='liggen')
    plt.scatter(df.time, df.staan, label='staan')
    plt.scatter(df.time, df.lopen_1, label='lopen 1')
    plt.scatter(df.time, df.lopen_2, label='lopen 2')
    plt.scatter(df.time, df.trap_op, label='trap op')
    plt.scatter(df.time, df.bureau, label='bureau')
    plt.legend(bbox_to_anchor=(1.1, 1.1))    
    plt.xlabel('time in seconds')
    # MANUALLY ADD NEW COLUMNS HERE! 

    plt.show() 

# transform granularity of the data: set downgrading factor  
downgrade_factor = 600 # 600 for dT of 1 min 
# take average of every group of rows 
data_transformed = data.groupby(np.arange(len(data))//downgrade_factor).mean()
# manually add the activities column again 
data_transformed['activity'] = np.array(data.iloc[int(downgrade_factor/2)::downgrade_factor]['activity'])

# visualize results for original data and for transformed data
visualize_results(data)
visualize_results(data_transformed)
