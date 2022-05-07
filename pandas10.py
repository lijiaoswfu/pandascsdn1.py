from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='2017',inplace=True,ascending=False)
print(students)
students.plot.bar(x='Field',y=['2016','2017'],color = ['orange','red'])
plt.title('InterNational students',fontsize = 18,fontweight = 'bold')
plt.xlabel('Field',fontweight = 'bold')
plt.ylabel('Number',fontweight = 'bold')
ax = plt.gca()  # 轴的控制点
ax.set_xticklabels(students['Field'],rotation = '45',ha = 'right') # ha旋转中心点
f = plt.gcf()  # 图形的控制点
f.subplots_adjust(left=0.2,bottom=0.42) #左边留出20%，下面留出42%
# plt.tight_layout()
plt.show()
