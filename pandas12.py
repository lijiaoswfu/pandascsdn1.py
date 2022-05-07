import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx',index_col='From')
# students.sort_values(by='2017',inplace=True,ascending = True) # 排序从小到大
print(students)  
# students['2017'].plot.pie(fontsize = 8,startangle=-270)  # 饼图里面的小文字,startangle=-270定义起始点角度
students['2017'].plot.pie(fontsize = 8,counterclock=False,startangle=-270) #可以不用排序，直接生成需要的图，第二种办法
plt.title('Source of InterNationl Students',fontsize=18,fontweight='bold')
plt.ylabel('2017year',fontsize = 12,fontweight= 'bold')  # Ylabel重写格式

plt.show()