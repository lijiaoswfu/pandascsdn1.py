# QGIS 插件资源更新（图标ICO等）
# 找到QGIS安装目录下的“OSGeo4W.bat”，双击打开它，会弹出一个命令行窗口，在命令行窗口中，我们使用“cd”命令，将当前路径设置到我们的插件工程路径下，然后使用如下命令编译这个插件的资源。pyrcc5 -o resources.py resources.qrc
