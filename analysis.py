import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("project_cricket/cricket.csv")
print(df.head())
df_sorted=df[['Player','Runs']].sort_values(by='Runs',ascending=False).head()
print(df_sorted)

df['average']=df['Runs']/df['Inns']
print(df[['Player','Runs','Inns','average']].head())
df_average=df[['Player','Runs','Inns','average']].sort_values(by="average",ascending=False).head()
print(df_average)
print(df[['Player','Runs','Inns','average','SR']].sort_values(by="SR",ascending=False).head())
print("highest run scoreer:")
print(df.iloc[0][['Player','Runs']])
print("highest average means consistent batter:")
print(df_average.iloc[0][['Player','average']])

avg_mean=df['average'].mean()
sr_mean=df['SR'].mean()
plt.scatter(df['average'],df['SR'],color='red',label='Player')
plt.axvline(avg_mean,linestyle='--',label='red')
plt.axhline(sr_mean,linestyle='--',label='red')
plt.text(avg_mean+1,sr_mean+1,'consistent and aggressive',fontsize=10,color='green')
plt.text(avg_mean-8,sr_mean+1,'consistent but slow',fontsize=10,color='blue')
plt.text(avg_mean+1,sr_mean-10,'aggressive',fontsize=10,color='orange')
plt.text(avg_mean-8,sr_mean-10,'needs imporvement ',fontsize=10,color='gray')
plt.xlabel('average')
plt.ylabel('SR')
plt.title('average vs strike rate')
plt.show()


