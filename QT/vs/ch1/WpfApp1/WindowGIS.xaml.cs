using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using NPOI.SS.UserModel;
using NPOI.XSSF.UserModel;
using Esri.ArcGISRuntime.Geometry;
using Esri.ArcGISRuntime.Mapping;

namespace WpfApp1
{
    /// <summary>
    /// WindowGIS.xaml 的交互逻辑
    /// </summary>
    public partial class WindowGIS : Window
    {
        public WindowGIS()
        {
            InitializeComponent();
            MapPoint mapCenterPoint = new MapPoint(107.389298, 29.703113, SpatialReferences.Wgs84);
            MainMapView.SetViewpoint(new Viewpoint(mapCenterPoint, 100000));
        }
    }
}
