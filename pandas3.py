import pandas as pd

books =pd.read_excel('c:/Temp/books.xlsx',index_col='ID')

for i in books.index:
    books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]
    
print(books)
