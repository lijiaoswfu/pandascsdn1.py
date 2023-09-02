# -*-coding:utf-8-*-
import os
import arcpy.mapping as mapping
import arcpy
import shutil 

mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd,r"图层")[0]
# 引入MXD源文件

yxsj = arcpy.GetParameterAsText(0) 
qmsj = arcpy.GetParameterAsText(1)
gmsj = arcpy.GetParameterAsText(2)
cbsj = arcpy.GetParameterAsText(3)
qmlyr = arcpy.GetParameterAsText(4)
gmlyr = arcpy.GetParameterAsText(5)
cblyr = arcpy.GetParameterAsText(6)
# 引入路径

arcpy.MakeRasterLayer_management(yxsj,"rasterLayer")
path = 'C:/ljtemp'
if os.path.exists(path):
    arcpy.AddMessage("---发现存在缓存文件夹，请确认关闭重新打开GIS软件后运行本工具！！！---")
    shutil.rmtree(path)
    os.mkdir(path)
    arcpy.SaveToLayerFile_management("rasterLayer", 'C:/ljtemp/bcyx.lyr', "ABSOLUTE")
    rasterbc = mapping.Layer(r"C:\ljtemp\bcyx.lyr")    
else:
    os.mkdir(path)
    arcpy.SaveToLayerFile_management("rasterLayer", 'C:/ljtemp/bcyx.lyr', "ABSOLUTE")
    rasterbc = mapping.Layer(r"C:\ljtemp\bcyx.lyr")
mapping.AddLayer(df,rasterbc,"BOTTOM")
arcpy.AddMessage("导入影像文件成功！")
# 加载底层栅格影像并保存为图层文件

# mxd.activeDataFrame.zoomToSelectedFeatures()
# 加载缓冲图层并缩放

arcpy.CopyFeatures_management(qmsj,"C:/ljtemp/qm.shp","#","0","0","0")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrqm in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrqm.name.lower() == "qm":
            arcpy.mapping.RemoveLayer(df, lyrqm)

arcpy . AddField_management ("C:/ljtemp/qm.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/qm.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/qm.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/qm.shp", field="gt", expression="[mj]*7.1*0.0001", expression_type="VB", code_block="") 
qmbc= mapping.Layer(qmlyr)
mapping.AddLayer(df,qmbc,"TOP")
arcpy.AddMessage("乔木固碳量计算完成！")
#乔木

arcpy.CopyFeatures_management(gmsj,"C:/ljtemp/gm.shp","#","0","0","0")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrgm in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrgm.name.lower() == "gm":
            arcpy.mapping.RemoveLayer(df, lyrgm)

arcpy . AddField_management ("C:/ljtemp/gm.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/gm.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/gm.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/gm.shp", field="gt", expression="[mj]*6.29*0.0001", expression_type="VB", code_block="") 
gmbc= mapping.Layer(gmlyr)
mapping.AddLayer(df,gmbc,"TOP")
arcpy.AddMessage("灌木固碳量计算完成！")
#灌木

arcpy.CopyFeatures_management(cbsj,"C:/ljtemp/cb.shp","#","0","0","0")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrcb in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrcb.name.lower() == "cb":
            arcpy.mapping.RemoveLayer(df, lyrcb)

arcpy . AddField_management ("C:/ljtemp/cb.shp" , 'mj' , "TEXT" , field_length = 5 )
arcpy . AddField_management ("C:/ljtemp/cb.shp" , 'gt' , "TEXT" , field_length = 5 )
arcpy.CalculateField_management("C:/ljtemp/cb.shp" ,'mj' ,"!shape.Area!","PYTHON_9.3")
arcpy.CalculateField_management(in_table="C:/ljtemp/cb.shp", field="gt", expression="[mj]*5.71*0.0001", expression_type="VB", code_block="") 
cbbc= mapping.Layer(cblyr)
mapping.AddLayer(df,cbbc,"TOP")
arcpy.AddMessage("草本固碳量计算完成！")
#草本


del mxd
#保存并释放缓存