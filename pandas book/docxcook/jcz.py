import pandas as pd
import os



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



basicData = pd.read_csv('./Data/2019.csv',encoding='utf-8-sig')
shp = pd.read_excel('./Data/ceshi.xlsx',encoding='utf-8-sig')
shp.rename(columns = {"xinxuhao": "序号", "MIAN_JI":"面积"}, inplace=True)
shp['现勘时间'].astype('str')
mega = basicData[['序号','镇镇（街道','村（居委）','社（林班）','林地权属','地类','林种','起源','森林类别','公益林事权','国家公益林','优势树种','林地保护等']]
shpMerge = pd.merge(shp,mega,how='left',on=['序号'])
# print(shpMerge.head())
shpMerge.to_excel('test.xlsx',encoding='utf-8-sig')
shpMergeunique = shpMerge['项目名称'].unique() # 获取项目不重复值
'''
for coluName in shpMergeunique:
    os.makedirs('./'+coluName, exist_ok=True)  # 建立对应的项目文件
'''
shpMergegroupby = shpMerge.groupby('占地属性',as_index=False)['面积'].sum()  # 根据地类统计面积,同时取消按条件索引
shpMergegroupby = shpMergegroupby.rename(columns={'占地属性':'镇镇（街道'}) # 修改列名，以便让两个表列名贴合

# sMgsum = shpMergegroupby.to_frame()
# sMgsum['index']= range(1,len(sMgsum)+1)
# sMgsum.set_index('index',inplace = True)
DF = pd.concat([shpMerge,shpMergegroupby])




