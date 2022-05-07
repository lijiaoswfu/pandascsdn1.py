from tkinter import font
from turtle import color
from numpy import tile
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='Number',inplace=True,ascending=False)  #排序并修改原始DF
print(students)
# students.plot.bar(x='Field',y='Number',color='orange',title='HandSome Lijiao')  # 按照字段绘制图形(控制颜色)
plt.bar(students.Field,students.Number,color='orange')
plt.xticks(students.Field,rotation = '90')
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('HandSome Lijiao',fontsize = 16)
plt.tight_layout()  # 紧凑型布局
plt.show()