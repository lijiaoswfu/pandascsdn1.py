using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.Arm;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.IO;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using GMap.NET;
using GMap.NET.MapProviders;
using GMap.NET.WindowsPresentation;
using NPOI.Util;

namespace WpfApp1
{
    /// <summary>
    /// Gmap.xaml 的交互逻辑
    /// </summary>
    public partial class Gmap : Window
    {
        // 全局参数对象
        DataPars dp = new DataPars();
        public Gmap()
        {
            InitializeComponent();

            string basePath = System.AppDomain.CurrentDomain.BaseDirectory;
            string cachePath = basePath + "MapData";
            gmap.CacheLocation = cachePath;

            // 指定地图的提供着(用的内置的微软的卫星地图) BingSatelLiteMap
            gmap.MapProvider = GMapProviders.BingSatelliteMap;
            // 设置地图初始化信息
            gmap.MinZoom = 2; // 最小缩放级别
            gmap.MaxZoom = 20; // 最大缩放级别
            gmap.Zoom = 15; // 当前缩放级别
            gmap.ShowCenter = true; // 设置显示中心十字
            gmap.DragButton = MouseButton.Left; // 指定拖拽的键(鼠标右键拖拽)
            gmap.Position = new PointLatLng(29.703113, 107.389298); // 指定当前位置
            GMaps.Instance.Mode = AccessMode.ServerAndCache; // GMap工作模式

            // 加载表格数据
            string filePath = AppDomain.CurrentDomain.BaseDirectory + @"涪陵坐标u8.csv";
            string[] strArray = File.ReadAllLines(filePath, Encoding.Default);
            dp.OilFields = new List<OilField>();
            for (int i = 0; i < strArray.Length - 1; i++)
            {
                string[] strings = strArray[i + 1].Split(',');
                OilField of = new OilField();
                of.Name = strings[3];
                of.Longitude = double.Parse(strings[0]);
                of.Latitude = double.Parse(strings[1]);
                of.Production = double.Parse(strings[2]);
                of.CityName = strings[4];
                dp.OilFields.Add(of);
            }

            // 标注数据到地图上
            // 首先清空原来的数据
            gmap.Markers.Clear();

            // 定义显示的点的直径的最大值和最小值
            double showMin = 5.0;
            double showMax = 30.0;
            double proMin = 99999; // 定义产量的最小值
            double proMax = -99999; // 定义产量的最大值
            for (int i = 0; i < dp.OilFields.Count; i++)
            {
                if (dp.OilFields[i].Production < proMin)
                {
                    // 更新最小值
                    proMin = dp.OilFields[i].Production;
                }
                if (dp.OilFields[i].Production > proMax)
                {
                    // 更新最大值
                    proMax = dp.OilFields[i].Production;
                }
            }

            double step = (showMax - showMin) / (proMax - proMin); //步长

            // 2. 通过循环添加每个油田的信息
            for (int i = 0; i < dp.OilFields.Count; i++)
            {
                // 计算显示的大小
                double showSize = showMin + (dp.OilFields[i].Production - proMin) * step;
                // 注意参数的顺序，这里是先纬度再经度
                PointLatLng pll = new PointLatLng(dp.OilFields[i].Latitude, dp.OilFields[i].Longitude);
                GMapMarker gmm = new GMapMarker(pll);
                // 设置显示的形状 以⚪的方式显示
                Ellipse e = new Ellipse();
                e.Width = showSize;
                e.Height = showSize;

                e.Fill = new RadialGradientBrush(Colors.Blue, Colors.Red); // 设置填充色
                // 设置当鼠标停留在点上时候，显示的信心
                e.ToolTip = "街道乡镇:" + dp.OilFields[i].CityName + "\r\n" + "项目名字:" + dp.OilFields[i].Name + "\r\n" + "人口:" + dp.OilFields[i].Production.ToString() + "人";

                // 添加鼠标左键单击点时的事件，绑定
                //e.MouseDown += E_MouseDown;
                // 设置鼠标移动到点上时鼠标的形状改变
                e.Cursor = Cursors.Hand;
                // 设置选中一个点后，其他数据区实时显示这个油田的信息(Binding)
                e.Tag = dp.OilFields[i];
                gmm.Shape = e;

                gmap.Markers.Add(gmm);
            }
        }

        private void Map_ToolTipOpening(object sender, ToolTipEventArgs e)
        {
            throw new NotImplementedException();
        }
    }
}
