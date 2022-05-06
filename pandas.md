# pandas 操作Excel
## 1、pandas读取任意位置数据
```python
books = pd.read_excel('c:/Temp/Books.xlsx',skiprows=3,usecols="C:F")
print(books)
```
## 2、pandas自定义填充序列号
```python
books = pd.read_excel('c:/Temp/Books.xlsx',skiprows=3,usecols="C:F",index_col=None,dtype={'ID':str})
for i in books.index:
    books['ID'].at[i] = i+1
print(books)
```
特别注意：Nan默认为float浮点数，需要将其转换为str字符串类型，不然ID不能取整。
## 3、日期累加计算
### 年
```python
 books['Date'].at[i] = date(start.year + i,start.month,start.day)
```
### 月
```python
 def add_month(d,md):
  yd = md // 12
  m = d.month + md % 12
  if m != 12:
      yd += m // 12
      m = m % 12
  return date(d.year + yd,m,d.day)
# 计算月份算法
 books['Date'].at[i] = add_month(start,i)
```
### 日
```python
books['Date'].at[i] = start + timedelta(days = i)
```
