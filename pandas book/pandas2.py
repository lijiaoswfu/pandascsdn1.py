import pandas as pd

data = pd.Series(5,index=[0,1,2])
data2 = pd.Series(3,index=['a','b','c'])
print(data)
print(data2)
# 通过数值创建序列