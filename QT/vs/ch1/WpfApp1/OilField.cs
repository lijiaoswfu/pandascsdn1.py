using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApp1
{
    internal class OilField
    {
        /// <summary>
        /// 油田名字
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// 油田所在中心城市名字
        /// </summary>
        public string CityName { get; set; }

        /// <summary>
        /// 油田位置经度坐标
        /// </summary>
        public double Longitude { get; set; }

        /// <summary>
        /// 油田位置纬度坐标
        /// </summary>
        public double Latitude { get; set; }

        /// <summary>
        /// 油田的当期产量
        /// </summary>
        public double Production { get; set; }

    }
}
