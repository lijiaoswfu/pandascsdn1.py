import numpy as np
import pandas as pd
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
df['city']=df['city'].str.lower()
print(df) # 大小写转换 upper(小转大)，lower(大转小)
print(df['price'].astype('int'))  # 更改数据格式

print(df.rename(columns={'category': 'category-size'}))  # 更改列名称：
print(df['city'].drop_duplicates())  #删除后出现的重复值
print(df['city'].replace('sh','shanghai')) # 数据替换

'''
concat合并：

pd.concat(objs, axis=0, join=‘outer’, join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False)
参数：

objs: series，dataframe或者是panel构成的序列lsit。
axis： 需要合并链接的轴，0是行，1是列，默认为axis=0。
join：连接的方式 inner，或者outer，默认为join=‘outer’
keys：合并的同时增加分区。
ignore_index：忽略索引，默认为False，当为True时，合并的两表就按列字段对齐。

merge合并：

pandas的merge方法提供了一种类似于SQL的内存链接操作，官网文档提到它的性能会比其他开源语言的数据操作（例如R）要高效。

pd.merge(left, right, how=‘inner’, on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True,
suffixes=(’_x’, ‘_y’), copy=True, indicator=False,validate=None)

merge的参数：

left/right：两个不同的DataFrame
on：指的是用于连接的列索引名称。必须存在右右两个DataFrame对象中，如果没有指定且其他参数也未指定则以两个DataFrame的列名交集做为连接键
left_on：左则DataFrame中用作连接键的列名;这个参数中左右列名不相同，但代表的含义相同时非常有用。right_on：右则DataFrame中用作 连接键的列名。
left_index：使用左则DataFrame中的行索引做为连接键。
right_index：使用右则DataFrame中的行索引做为连接键。
how：指的是合并(连接)的方式有inner(内连接),left(左外连接),right(右外连接),outer(全外连接);默认为inner。
sort：根据DataFrame合并的keys按字典顺序排序，默认是True，如果置false可以提高表现。
suffixes：字符串值组成的元组，用于指定当左右DataFrame存在相同列名时在列名后面附加的后缀名称，默认为(’_x’,’_y’)
copy：默认为True,总是将数据复制到数据结构中；大多数情况下设置为False可以提高性能
indicator：在 0.17.0中还增加了一个显示合并数据中来源情况；如只来自于左边(left_only)、两者(both)。

merge的默认合并方法：merge用于表内部基于 index-on-index 和 index-on-column(s) 的合并，但默认是基于index来合并。

join连接：主要用于索引上的合并

join(self, other, on=None, how=‘left’, lsuffix=’’, rsuffix=’’,sort=False)

其中参数的意义与merge方法基本相同,只是join方法默认为左外连接how=left

1.默认按索引合并，可以合并相同或相似的索引，不管他们有没有重叠列。
2.可以连接多个DataFrame
3.可以连接除索引外的其他列
4.连接方式用参数how控制
5.通过lsuffix=’’, rsuffix=’’ 区分相同列名的列
'''

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'],'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']},index=[0, 1, 2, 3])  
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7'],'C': ['C4', 'C5', 'C6', 'C7'],'D': ['D4', 'D5', 'D6', 'D7']},index=[4, 5, 6, 7])  
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],'B': ['B8', 'B9', 'B10', 'B11'],'C': ['C8', 'C9', 'C10', 'C11'],'D': ['D8', 'D9', 'D10', 'D11']},index=[8, 9, 10, 11])  
df1

# 数据预处理

result = pd.concat([df1,df2,df3])  
print(result)
# 使用concat进行合并

result1 = pd.concat([df1,df2,df3], keys=['x', 'y', 'z'])  
print(result1)
# 将df1,df2,df3进行合并，并将合并后的数据帧进行分区为keys=[‘x’,‘y’,‘z’]

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],'D': ['D2', 'D3', 'D6', 'D7'],'F': ['F2', 'F3', 'F6', 'F7']},index=[2, 3, 6, 7])  
result2=pd.concat([df1,df4],axis=1)  
print(result2) 
# 新建一个数据帧df4，将df1与df4进行列项合并，axis=1。

result3=pd.concat([df1,df4],axis=1,join='inner')  
print(result3)
# df1与df4进行列项合并axis=1，合并方式为内部合并join=‘inner’

result5=pd.concat([df1,df4],ignore_index=True)  
print(result5)  
# 将df1与df4合并，忽略行索引ignore_index=True

s1=pd.Series(['X0', 'X1', 'X2', 'X3'],name='X')  
result6=pd.concat([df1,s1],axis=1)  
print(result6)
# 创建一个名为s1的Series值为[‘X0’, ‘X1’, ‘X2’, ‘X3’]，name=‘X’，将df1与s1进行列项合并

result=pd.concat([df1,s1],axis=1,ignore_index=True)  
print(df1,s1,result) 
# 将df1与s1进行列项合并，忽略索引 ignore_index=True

s2 = pd.Series([0, 1, 2, 3], name='foo')  
s3 = pd.Series([0, 1, 2, 3])  
s4 = pd.Series([0, 1, 4, 5])  
pd.concat([s2,s3,s4],axis=1,keys=['red','blue','yellow'])  
# 创建三个Series分别为s2,s3,s4，将三个Series进行合并，使用keys=[‘red’,‘blue’,‘yellow’]对合并后数据帧的列改名

pieces={'x':df1,'y':df2,'z':df3}  
result = pd.concat(pieces, keys=['z', 'y'])  
pieces
result
# 将df1,df2,df3,作为值，x,y,z作为键构建名为pieces的字典，然后对pieces使用concat进行合并，并令参数keys=[‘z’,‘y’]

df1.append(df2)  
# 使用append方法将df1与df2合并

df1.append(df4)
# 使用append方法将df1与df4合并

df1.append([df2,df3])  
# 使用append方法将df1与df2、df3合并

result=df1.append(df4,ignore_index=True)  
result
# 将df1与df4进行合并，忽略索引ignore_index=True

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})  
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})  
result = pd.merge(left, right, on='key')  
print( left,right,result)  
# 创建两个数据帧left、right，使用merge函数按key列将left与right进行连接

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'],'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']})  
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],'key2': ['K0', 'K0', 'K0', 'K0'],'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']})  
result = pd.merge(left, right, on=['key1', 'key2'])  
print( left,right,result)  
# 创建两个数据帧left、right，使用merge函数按[key1，key2]列将left与right进行连接(复合key的合并方法，使用merge的时候可以选择多个key作为复合可以来对齐合并)

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'],'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']})  
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],'key2': ['K0', 'K0', 'K0', 'K0'],'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']})  
result = pd.merge(left, right, how='left', on=['key1', 'key2'])  
print( left,right,result)  
# 使用merge函数按[key1，key2]列将left与right进行左表连接

result = pd.merge(left, right, how='right', on=['key1', 'key2'])  
print(result) 
# 使用merge函数按[key1，key2]列将left与right进行右表连接

result = pd.merge(left, right, how='outer', on=['key1', 'key2'])  
print(result)  
# 使用merge函数按[key1，key2]列将left与right进行外表连接

left = pd.DataFrame({'A' : [1,2], 'B' : [2, 2]})  
right = pd.DataFrame({'A' : [4,5,6], 'B': [2,2,2]})  
result = pd.merge(left, right, on='B', how='outer')  
print(result)
# 创建两个都只有A、B两列的数据帧left,right，使用merge函数按B列将left与right进行外表连接，可以看到除连接列B以外的列名相同时，会在列名后加上区分的后缀

df1 = pd.DataFrame({'col1': [0, 1], 'col_left':['a', 'b']})  
df2 = pd.DataFrame({'col1': [1, 2, 2],'col_right':[2, 2, 2]})  
pd.merge(df1, df2, on='col1', how='outer', indicator=True) 
# 创建两个数据帧df1、df2，使用merge函数按col1列将df1与df2进行外表连接，并使用参数indicator显示出每列值在合并列中是否出现

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],'B': ['B0', 'B1', 'B2']},index=['K0', 'K1', 'K2'])  
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],'D': ['D0', 'D2', 'D3']},index=['K0', 'K2', 'K3'])  
result = left.join(right)  
print(left,'\n',right,'\n',result)  
# 创建两个数据帧left、right，使用join方法将left与right连接

result = left.join(right, how='outer')  
print(left,'\n',right,'\n',result)  
# 使用join方法将left与right进行外表连接

result = left.join(right, how='inner')  
print(left,'\n',right,'\n',result)  
# 使用join方法将left与right进行内表连接

result = pd.merge(left, right, left_index=True, right_index=True, how='outer')  
print(left,'\n',right,'\n',result)  
# 使用merge函数按左右表索引将left与right进行外表连接

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3'], 'key': ['K0', 'K1', 'K0', 'K1']})  
right = pd.DataFrame({'C': ['C0', 'C1'],'D': ['D0', 'D1']},index=['K0', 'K1'])  
result = left.join(right, on='key')  
print(left,'\n',right,'\n',result)  
# 创建两个数据帧left、right，使用join方法按key列将left与right连接

result = pd.merge(left, right, left_on='key', right_index=True,how='left', sort=False)  
print(left,'\n',right,'\n',result)  



df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008], 
"gender":['male','female','male','female','male','female','male','female'],
"pay":['Y','N','Y','Y','N','Y','N','Y',],
"m-point":[10,12,20,40,40,40,30,20]})
# 数据预处理

df_inner=pd.merge(df,df1,how='inner')  # 匹配合并，交集
df_left=pd.merge(df,df1,how='left')        #
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')  #并集
# 表格合并

df_inner.set_index('id')
# 设置索引列

df_inner.sort_values(by=['age'])
# 按照特定列的值排序

df_inner.sort_index()
# 按照索引列排序

df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
print(df_inner)
# 如果prince列的值>3000，group列显示high，否则显示low

df_inner['city'].astype('str')
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1
print(df_inner)
# 对复合多个条件的数据进行分组标记(有问题)

split = pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size'])
split
# 对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size

df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)
df_inner
# 将完成分裂后的数据表和原df_inner数据表进行匹配

df_inner.loc[3]
# 按索引提取单行的数值

df_inner.iloc[0:5]
# 按索引提取区域行数值

df_inner.reset_index()
# 重设索引

df_inner=df_inner.set_index('date') 
df_inner[:'2013-01-04']
#  设置日期为索引,提取4日之前的所有数据

df_inner.iloc[:3,:2] #冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。
# 使用iloc按位置区域提取数据

df_inner.iloc[[0,2,5],[4,5]] #提取第0、2、5行，4、5列
# 适应iloc按位置单独提起数据

df_inner.ix[:'2013-01-03',:4] #2013-01-03号之前，前四列数据
# 使用ix按索引标签和位置混合提取数据

df_inner['city'].map(str.strip)
df_inner['city'].astype('str')
df_inner['city'].isin(['guangzhou'])
# 判断city列的值是否为北京(有问题)

df_inner.loc[df_inner['city'].isin(['beijing','shanghai','shenzhen'])] 
# 判断city列里是否包含beijing和shanghai，然后将符合条件的数据提取出来,beijing和guangzhou始终是bug

categ1 = pd.DataFrame(df_inner['category'].str[:3])
print(categ1)
# 提取前三个字符，并生成数据表

df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'sh'), ['id','city','age','category','gender']]
# 使用“与”进行筛选

df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'sh'), ['id','city','age','category','gender']].sort_values(['age']) 
# 使用“或”进行筛选

df_inner.loc[(df_inner['city'] != 'sh'), ['id','city','age','category','gender']].sort_values(['id']) 
# 使用“非”条件进行筛选

df_inner.loc[(df_inner['city'] != 'sh'), ['id','city','age','category','gender']].sort_values(['id']).city.count()
# 对筛选后的数据按city列进行计数

df_inner.query('city == ["shenzhen", "shanghai"]')
# 使用query函数进行筛选

df_inner.query('city == ["shenzhen", "shanghai"]').price.sum()
# 对筛选后的结果按prince进行求和

df_inner.groupby('city').count()
# 对所有的列进行计数汇总

df_inner.groupby('city')['id'].count()
# 按城市对id字段进行计数

df_inner.groupby(['city','size_x'])['id'].count()
# 对两个字段进行汇总计数

df_inner.groupby('city')['price'].agg([len,np.sum, np.mean]) 
# 对city字段进行汇总，并分别计算prince的合计和均值

df_inner.sample(n=3) 
# 简单的数据采样(随机)

weights = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights) 
# 手动设置采样权重(指定权重采样)

df_inner.sample(n=6, replace=False) 
# 采样后不放回（replace=False），True放回

df_inner.describe().round(2).T #round函数设置显示小数位，T表示转置
# 数据表描述性统计

df_inner['price'].std()
# 计算列的标准差

df_inner['price'].cov(df_inner['m-point']) 
# 计算两个字段间的协方差

df_inner.cov()
# 数据表中所有字段间的协方差

df_inner['price'].corr(df_inner['m-point']) #相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关
# 两个字段的相关性分析

df_inner.corr()
# 数据表的相关性分析











