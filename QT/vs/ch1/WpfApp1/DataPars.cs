using NPOI.Util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApp1
{
    internal class DataPars
    {
        /// <summary>
        /// 油田名称列表
        /// </summary>
        public string[] FieldNames { get; set; }

        /// <summary>
        /// 油气当量列表
        /// </summary>
        public double[] Productions { get; set; }

        /// <summary>
        /// 油气类型
        /// </summary>
        public string[] TypeNames { get; set; }

        /// <summary>
        /// 类型占比
        /// </summary>
        public double[] TypePersents { get; set; }

        /// <summary>
        /// 交易日期
        /// </summary>
        public DateTime[] ShareData { get; set; }

        /// <summary>
        /// 开盘价
        /// </summary>
        public double[] OpenPrice { get; set; }

        /// <summary>
        /// 收盘价
        /// </summary>
        public double[] ClosePrice { get; set; }

        /// <summary>
        /// 最高价
        /// </summary>
        public double[] HighPrice { get; set; }

        /// <summary>
        /// 最低价
        /// </summary>
        public double[] LowPrice { get; set; }

        /// <summary>
        /// 等值线 X坐标位置
        /// </summary>
        public double[] XScale { get; set; }

        /// <summary>
        /// 等值线y坐标位置
        /// </summary>
        public double[] YScale { get; set; }

        /// <summary>
        /// 饱和度值 等值线坐标（x,y）上的值
        /// </summary>
        public double[,] Values { get; set; }

        /// <summary>
        /// 油田信息
        /// </summary>
        public List<OilField> OilFields { get; set; }

        /// <summary>
        /// 曲线信息字典
        /// </summary>
        public Dictionary<string, LogCurve> LogCurveDic { get; set; }
    }
}
