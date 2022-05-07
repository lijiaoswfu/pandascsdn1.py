#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import arcpy
import xlwings as xw
import pandas as pd

app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add(unicode('新工作表'))

delimfield = arcpy.AddFieldDelimiters("c:/data/baisheng2.shp","面积")
delimfield1 = arcpy.AddFieldDelimiters("c:/data/baisheng2.shp","社")
str =  delimfield1 +" = '7'"
whereclause = """{} >1""".format(arcpy.AddFieldDelimiters("c:/data/baisheng2.shp", "面积"))

rows = arcpy.SearchCursor("c:/data/baisheng2.shp",
                          fields="乡镇街; 村; 社; 小班号; 面积; 优势树",
                          where_clause=str,
                          sort_fields="村 A; 社 B;小班号 C"
                          )
'''
for row in rows:
    print("乡镇: {0}, 村: {1},社: {2},小班号: {3},面积: {4},优势树种: {5}".format(
        row.getValue("乡镇街"),
        row.getValue("村"),
        row.getValue("社"),
        row.getValue("小班号"),
        row.getValue("面积"),
        row.getValue("优势树")
    ))
'''
# 创建一个空的Dataframe


xz = unicode('乡镇街')
cz = unicode('村')
sz = unicode('社')
xbh = unicode('小班号')
mj = unicode('面积')
yssz = unicode('优势树')
result =pd.DataFrame(columns=(xz,cz,sz,xbh,mj,yssz))
#将计算结果逐行插入result

for row in rows:
    xiangzhen = row.getValue(xz).encode("utf_8_sig"),
    cun = row.getValue(cz).encode("utf_8_sig"),
    she = row.getValue(sz).encode("utf_8_sig"),
    xiaobanhao = row.getValue(xbh).encode("utf_8_sig"),
    mianji = row.getValue(mj),
    youshizhuzhong = row.getValue(yssz).encode("utf_8_sig"),
    result=result.append(pd.DataFrame({xz:[xiangzhen],cz:[cun],sz:[she],xbh:[xiaobanhao],mj:[mianji],yssz:[youshizhuzhong]}),ignore_index=True)
    print("乡镇: {0}, 村: {1},社: {2},小班号: {3},面积: {4},优势树种: {5}".format(
        row.getValue("乡镇街"),
        row.getValue("村"),
        row.getValue("社"),
        row.getValue("小班号"),
        row.getValue("面积"),
        row.getValue("优势树")
    ))


print (result)
result.to_csv('tab.csv',header=None, index=None, encoding='utf_8_sig')
print(result.dtypes)
worksheet.range('A1').value = result
workbook.save(r'c:\data\table.xlsx')
workbook.close()
app.quit()
