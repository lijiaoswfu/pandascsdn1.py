# -*-coding:utf-8-*-
import os
import arcpy.mapping as mapping
import arcpy
import shutil 

mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd,r"图层")[0]
# 引入MXD源文件

yxsj = arcpy.GetParameterAsText(0) 
poi = arcpy.GetParameterAsText(1)
uv = arcpy.GetParameterAsText(2)
pois = arcpy.GetParameterAsText(3)
poihcs = arcpy.GetParameterAsText(4)
ucs = arcpy.GetParameterAsText(5)
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

uvshape = uv
addLayer1 = arcpy.mapping.Layer(uvshape)
# arcpy.mapping.AddLayer(df, addLayer1, "TOP")
arcpy.CopyFeatures_management(uv,"C:/ljtemp/UV_LCRA.shp","#","0","0","0")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyruv in arcpy.mapping.ListLayers(mxd, "", df):
        if lyruv.name.lower() == "UV_LCRA":
            arcpy.mapping.RemoveLayer(df, lyruv)

theShape = poi
addLayerpoi = arcpy.mapping.Layer(theShape)
arcpy.mapping.AddLayer(df, addLayerpoi, "TOP")
arcpy.AddMessage(poi)
arcpy.AddMessage("导入规划矢量数据文件成功！")
# 加载POI和规划矢量数据


arcpy.CopyFeatures_management(poi,"C:/ljtemp/hcqdz.shp","#","0","0","0")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyrpoi in arcpy.mapping.ListLayers(mxd, "", df):
        if lyrpoi.name.lower() == "poi":
            arcpy.mapping.RemoveLayer(df, lyrpoi)
            

# 问题出在这里
# POI导出处理图层

arcpy.AddField_management("C:/ljtemp/hcqdz.shp","BUFF_DIST","TEXT")
expression = "getClass(!tag!)"
codeblock = """def getClass(name):
    if (name == u"医疗;综合医院"):
        return 500
    elif (name == u"医疗;专科医院"):
        return 250
    elif (name == u"医疗;诊所"):
        return 150
    else:
        return 50"""
arcpy.CalculateField_management("C:/ljtemp/hcqdz.shp", "BUFF_DIST", expression, "PYTHON_9.3", 
                                codeblock)
arcpy.AddMessage("POI数据清洗和地类权重因子匹配成功！")
# 处理图层增加字段并计算缓冲区范围

arcpy.Buffer_analysis("C:/ljtemp/hcqdz.shp","C:/ljtemp/hcq2.shp","BUFF_DIST","FULL","ROUND","NONE","#")
arcpy.AddMessage("公共服务设施影响因子范围创建成功！")
# 创建缓冲区
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hcq2"



uvshapedc = r"C:/ljtemp/UV_LCRA.shp"
addLayeruvdc = arcpy.mapping.Layer(uvshapedc)
arcpy.mapping.AddLayer(df, addLayeruvdc, "TOP")
poidz = r"C:/ljtemp/hcqdz.shp"
addLayer = arcpy.mapping.Layer(poidz)
refLayer = arcpy.mapping.ListLayers(mxd, "UV_LCR*", df)[0]
mapping.InsertLayer(df, refLayer, addLayer, "BEFORE")
poihc = "C:/ljtemp/hcq2.shp"
addLayerhc = arcpy.mapping.Layer(poihc)
mapping.InsertLayer(df, refLayer, addLayerhc, "BEFORE")

# 加载缓冲区

updateLayerdz = mapping.ListLayers(mxd, "hcqdz", df)[0]
updateLayerhc = mapping.ListLayers(mxd, "hcq2", df)[0]
updateLayer1 = mapping.ListLayers(mxd, "UV_LCRA", df)[0]
sourceLayerdz = mapping.Layer(pois)
sourceLayerhc = mapping.Layer(poihcs)
sourceLayer1 = mapping.Layer(ucs)
mapping.UpdateLayer(df,updateLayerdz,sourceLayerdz,False)
mapping.UpdateLayer(df,updateLayerhc,sourceLayerhc,False)
mapping.UpdateLayer(df,updateLayer1,sourceLayer1,False)

arcpy.AddMessage("现状图图层符号更新成功！")
# 更新SHP图层符号

del mxd
#保存并释放缓存