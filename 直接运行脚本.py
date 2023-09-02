# -*-coding:utf-8-*-
import os
import arcpy.mapping as mapping
import arcpy
import shutil 

mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd,r"图层")[0]
# 引入MXD源文件


arcpy.MakeRasterLayer_management(r"C:\carl\th\bcyx.tif","rasterLayer")
path = 'C:/ljtemp'
if os.path.exists(path):
    arcpy.AddMessage("---发现存在缓存文件夹，请确认关闭重新打开GIS软件后运行本工具！！！---")
    shutil.rmtree(path)
    
else:
    os.mkdir(path)
    arcpy.SaveToLayerFile_management("rasterLayer", 'C:/ljtemp/bcyx.lyr', "ABSOLUTE")
    rasterbc = mapping.Layer(r"C:\ljtemp\bcyx.lyr")
#mapping.AddLayer(df,rasterbc,"BOTTOM")
arcpy.AddMessage("导入影像文件成功！")
# 加载底层栅格影像并保存为图层文件



arcpy.CopyFeatures_management(r"C:\carl\th\shp\lyqm.shp","C:/ljtemp/qm.shp","#","0","0","0")


arcpy . AddField_management ("C:/ljtemp/qm.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/qm.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/qm.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/qm.shp", field="gt", expression="[mj]*7.1*0.0001", expression_type="VB", code_block="") 

for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrqm in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrqm.name.lower() == "qm":
            arcpy.mapping.RemoveLayer(df, lyrqm)
qmbc= mapping.Layer(r"C:\carl\th\lyr\qm.lyr")
mapping.AddLayer(df,qmbc,"TOP")
mxd.activeDataFrame.zoomToSelectedFeatures()
arcpy.AddMessage("乔木固碳量计算完成！")
#乔木

arcpy.CopyFeatures_management(r"C:\carl\th\shp\lvgm.shp","C:/ljtemp/gm.shp","#","0","0","0")
arcpy . AddField_management ("C:/ljtemp/gm.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/gm.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/gm.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/gm.shp", field="gt", expression="[mj]*6.29*0.0001", expression_type="VB", code_block="") 
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrgm in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrgm.name.lower() == "gm":
            arcpy.mapping.RemoveLayer(df, lyrgm)

gmbc= mapping.Layer(r"C:\carl\th\lyr\gm.lyr")
mapping.AddLayer(df,gmbc,"TOP")
arcpy.AddMessage("灌木固碳量计算完成！")
#灌木

arcpy.CopyFeatures_management(r"C:\carl\th\shp\cmtb.shp","C:/ljtemp/cb.shp","#","0","0","0")


arcpy . AddField_management ("C:/ljtemp/cb.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/cb.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/cb.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/cb.shp", field="gt", expression="[mj]*5.71*0.0001", expression_type="VB", code_block="") 
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrcb in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrcb.name.lower() == "cb":
            arcpy.mapping.RemoveLayer(df, lyrcb)

cbbc= mapping.Layer(r"C:\carl\th\lyr\cb.lyr")
mapping.AddLayer(df,cbbc,"TOP")
arcpy.AddMessage("草本固碳量计算完成！")
#草本

mxd.activeDataFrame.zoomToSelectedFeatures()
# 加载缓冲图层并缩放
