import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('C:/Temp/Users.xlsx')

users['Total'] = users['Oct']+users['Nov']+users['Dec']
users.sort_values(by='Total',inplace=True,ascending=True)
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked = True)  # stacked = True条状图，users.plot.barh横状图
plt.title('HandSome Lijiao',fontsize =18,fontweight ='bold')
plt.tight_layout()

print(users)
plt.show()
