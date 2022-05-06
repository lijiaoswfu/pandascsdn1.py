import pandas as pd

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[2,3,4],name='C')

df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)