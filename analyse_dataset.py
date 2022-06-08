import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('final_dataset.csv')
df_test = df.groupby(np.arange(len(df))//600).mean()
print(df.shape)
print(df_test.shape)
print(df.isna().sum())

plt.subplot(2,1,1)
plt.plot(df.x_Accelerometer,label='x_acc')
plt.plot(df.y_Accelerometer,label='y_acc')
plt.plot(df.z_Accelerometer,label='z_acc')
plt.legend()
plt.subplot(2,1,2)
plt.plot(df_test.x_Accelerometer,label='x_acc')
plt.plot(df_test.y_Accelerometer,label='y_acc')
plt.plot(df_test.z_Accelerometer,label='z_acc')
plt.legend()
plt.show()
