import pandas as pd
import numpy as np

initdata = np.array(['hello','world','pyton'])
data = pd.Series(initdata,index=[1,2,3])
print(data)
# 通过Numpy数组创建序列