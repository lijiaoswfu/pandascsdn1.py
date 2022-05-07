# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import arcpy
import pandas as pd
import xlwings as xw

app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add(unicode('新工作表'))

xz = unicode('乡镇街')
cz = unicode('村')
sz = unicode('社')
xbh = unicode('小班号')
mj = unicode('面积')
yssz = unicode('优势树')
c1 = str((xz,cz,sz,xbh,mj,yssz))

def Shp2dataframe(path,ziduan):
    # 将arcpy表单变为pandas表单输出'''
    fields1 = arcpy.ListFields(path)
    table = []
    fieldname = [field.name for field in fields1]
    # 游标集合，用for 循环一次后没办法循环第二次!一个游标实例只能循环一次
    data = arcpy.SearchCursor(path,fields=ziduan)
    for row in data:
        # Shape字段中的要数是一个几何类
        r = []
        r.append(row.getValue(xz))
        r.append(row.getValue(cz))
        r.append(row.getValue(sz))
        r.append(row.getValue(xbh))
        r.append(row.getValue(mj))
        r.append(row.getValue(yssz))
        table.append(r)
    return pd.DataFrame(table, columns=(xz,cz,sz,xbh,mj,yssz))


path = "c:/data/baisheng2.shp"
ziduan = "乡镇街; 村; 社; 小班号; 面积; 优势树"
result = Shp2dataframe(path,ziduan)
print(result.dtypes)
worksheet.range('A1').value = result
workbook.save(r'c:\data\table.xlsx')
workbook.close()
app.quit()
