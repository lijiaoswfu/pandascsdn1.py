import pandas as pd

books = pd.read_excel('c:/Temp/books.xlsx',index_col='ID')
books['Price'] = books['ListPrice'] * books['Discount']
print(books)