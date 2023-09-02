import sys
import os

from ui_demo import Ui_MainWindow

from qgis.core import *
from qgis.gui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWnd(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # 初始化Ui
        self.setupUi(self)
        # 初始化Project和Canvas
        self.project = QgsProject.instance()
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)
        self.setCentralWidget(self.canvas)
        # 在Dock窗口中添加LayerTreeView
        self.vl = QVBoxLayout(self.dockWidgetContents)
        self.layer_tree_view = QgsLayerTreeView(self)
        self.vl.addWidget(self.layer_tree_view)
        self.layer_tree_root = self.project.layerTreeRoot()
        self.layer_tree_model = QgsLayerTreeModel(self.layer_tree_root)
        self.layer_tree_model.setFlag(QgsLayerTreeModel.AllowNodeRename)
        self.layer_tree_model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
        self.layer_tree_model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.layer_tree_model.setFlag(QgsLayerTreeModel.ShowLegendAsTree)
        self.layer_tree_model.setAutoCollapseLegendNodes(10)
        self.layer_tree_view.setModel(self.layer_tree_model)
        self.layer_tree_bridge = QgsLayerTreeMapCanvasBridge(self.layer_tree_root, self.canvas)

        # 用于存放已加载的layers
        self.layers = []
        # 设置 Canvas CRS
        # crs = QgsCoordinateReferenceSystem("EPSG:3857")
        # self.canvas.setDestinationCrs(crs)

        # 加载WMS图层-天地图
        urlWithParams = 'https://t2.tianditu.gov.cn/img_w/wmts?SERVICE%3DWMTS%26REQUEST%3DGetTile%26VERSION%3D1.0.0%26LAYER%3Dimg%26STYLE%3Ddefault%26TILEMATRIXSET%3Dw%26FORMAT%3Dtiles%26TILECOL%3D%7Bx%7D%26TILEROW%3D%7By%7D%26TILEMATRIX%3D%7Bz%7D%26tk%3Df9e240b5332a9def9adab74b40013835&zmax=18&zmin=0'
        urlWithZhuji = 'https://t2.tianditu.gov.cn/cia_w/wmts?SERVICE%3DWMTS%26REQUEST%3DGetTile%26VERSION%3D1.0.0%26LAYER%3Dcia%26STYLE%3Ddefault%26TILEMATRIXSET%3Dw%26FORMAT%3Dtiles%26TILECOL%3D%7Bx%7D%26TILEROW%3D%7By%7D%26TILEMATRIX%3D%7Bz%7D%26tk%3Df9e240b5332a9def9adab74b40013835&zmax=18&zmin=0'
        self.osm_layer = QgsRasterLayer("type=xyz&url=" + urlWithParams, '天地图', "wms")
        self.layer_zhuji = QgsRasterLayer("type=xyz&url=" + urlWithZhuji, '天地图注记', "wms")
        print('天地图源', self.osm_layer.crs())
        if not self.osm_layer.isValid():
            print("天地图加载失败!")
        else:
            self.project.addMapLayer(self.osm_layer)
            self.layers.append(self.osm_layer)
            self.project.addMapLayer(self.layer_zhuji)
            self.layers.append(self.layer_zhuji)
            # self.canvas.setExtent(self.osm_layer.extent())
            # self.canvas.setLayers(self.layers)

        self.actionOpenRaster = QAction("影像图", self)
        self.actionOpenVector = QAction("矢量数据", self)
        self.actionZoomIn = QAction("缩小", self)
        self.actionZoomOut = QAction("放大", self)
        self.actionPan = QAction("移动桌布", self)

        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)
        self.actionPan.setCheckable(True)

        self.actionOpenRaster.triggered.connect(self.load_raster)
        self.actionOpenVector.triggered.connect(self.load_vector)
        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionPan.triggered.connect(self.pan)

        self.toolbar = self.addToolBar("桌布动作栏")
        self.menuOpen = QMenu('打开', self.toolbar)
        self.toolbar.addAction(self.menuOpen.menuAction())
        self.menuOpen.addAction(self.actionOpenRaster)
        self.menuOpen.addAction(self.actionOpenVector)
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionPan)

        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)  # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)  # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)
        self.pan()

    def load_raster(self):
        # 加载栅格图层
        path_to_tif, ext = QFileDialog.getOpenFileName(self, '打开', '',
                                                       '所有文件(*.tif)')  # "D:\QgisDemo\MYD11C1.A2019134.061.2020352180203.tif"
        rlayer = QgsRasterLayer(path_to_tif, os.path.basename(path_to_tif))
        if not rlayer.isValid():
            print("影像图加载失败!")
        self.project.addMapLayer(rlayer)
        self.layers.append(rlayer)
        # self.canvas.setExtent(rlayer.extent())
        # self.canvas.setLayers(self.layers)

    def load_vector(self):
        # 加载矢量图层
        path_to_tif, ext = QFileDialog.getOpenFileName(self, '打开', '', '所有文件(*.shp)')
        layer = QgsVectorLayer(path_to_tif, os.path.basename(path_to_tif), 'ogr')
        if not layer.isValid():
            print("矢量数据加载失败!")
        self.project.addMapLayer(layer)
        self.layers.append(layer)
        self.canvas.setExtent(layer.extent())
        self.canvas.setLayers(self.layers)

    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)


if __name__ == '__main__':
    qgs = QgsApplication([], True)
    qgs.setPrefixPath('C:/OSGeo4W/apps/qgis-ltr', True)
    qgs.initQgis()

    window = MyWnd()
    window.show()

    exit_code = qgs.exec_()
    qgs.exitQgis()
    sys.exit(exit_code)
