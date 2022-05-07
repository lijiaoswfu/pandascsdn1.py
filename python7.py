import pandas as pd

products = pd.read_excel('C:/Temp/List.xlsx',index_col='ID')
products.sort_values(by =['Worthy','Price'],inplace = True,ascending = [True,False])
print(products)