import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


plt.switch_backend('Tkagg')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#通过下面这行解决中文乱码问题
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})

basicData = pd.read_csv('./Data/2019.csv',encoding='utf-8-sig')
shp = pd.read_excel('./Data/baohu.xlsx',encoding='utf-8-sig')
shp.rename(columns = {"xinxuhao": "序号", "MIAN_JI":"面积"}, inplace=True)
shp['现勘时间'].astype('str')
mega = basicData[['序号','镇镇（街道','村（居委）','社（林班）','林地权属','地类','林种','起源','森林类别','公益林事权','国家公益林','优势树种','林地保护等']]
shpMerge = pd.merge(shp,mega,how='left',on=['序号'])
# print(shpMerge.head())
shpMerge.to_excel('test.xlsx',encoding='utf-8-sig')
shpMergeunique = shpMerge['项目名称'].unique() # 获取项目不重复值
for coluName in shpMergeunique:
    os.makedirs('./'+coluName, exist_ok=True)  # 建立对应的项目文件





shpMerge.plot.barh(x='项目名称',y='面积',stacked = True)

plt.ylabel('项目名称')
plt.xlabel('面积')
plt.title('自然保护地项目占用面积',fontsize =18,fontweight ='bold')
plt.tight_layout()
plt.show()


# sns.relplot(y="面积",x="项目名称",data=shpMerge)