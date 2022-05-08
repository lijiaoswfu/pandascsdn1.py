import numpy as np
import pandas as pd
from sqlalchemy import true
# 添加引用

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006], 
 "date":pd.date_range('20130102', periods=6),
  "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
 "age":[23,44,54,32,34,32],
 "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
  "price":[1200,np.nan,2133,5433,np.nan,4432]},
  columns =['id','date','city','category','age','price'])
# 创建数据帧
print(df)
print(df.shape)  # 维度查看
print(df.info()) # 数据表基本信息（维度、列名称、数据格式、所占空间等）：
print(df.dtypes) # 每一列数据的格式
print(df['city'].dtype) # 某一列格式
print(df.isnull())  # 是否是空值
print(df['city'].isnull())  # 查看某一列是否空值
print(df['city'].unique()) # 查看某一列唯一值
print(df.values) # 查看数据表的值
print(df.columns)  # 查看列名
print(df.head())  # 查看前五行数据
print(df.tail())  # 查看后五行数据
print(df.fillna(value=0,inplace=True)) # 对空值用0填充,切记加上inplace=True，不然无法原地修改
print(df.fillna(df['price'].mean(),inplace=True))  # 使用列prince的均值对NA进行填充，,切记加上inplace=True，不然无法原地修改
print(df['city'].map(str.strip))  # 清除city字段的字符空格
df['city']=df['city'].str.upper()
print(df) # 大小写转换 upper(小转大)，lower(大转小)
print(df['price'].astype('int'))  # 更改数据格式
