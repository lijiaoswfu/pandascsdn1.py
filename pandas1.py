import pandas as pd

books = pd.read_excel('c:/Temp/Books.xlsx',skiprows=3,usecols="C:F")
print(books)

