# pandas 操作Excel
## pandas读取任意位置数据
```python
books = pd.read_excel('c:/Temp/Books.xlsx',skiprows=3,usecols="C:F")
print(books)
```
