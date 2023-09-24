using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfApp1
{
    internal class LogCurve
    {
        /// <summary>
        /// 曲线名字
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// 曲线单位
        /// </summary>
        public string Unit { get; set; }

        /// <summary>
        /// 起始深度
        /// </summary>
        public double TopDep { get; set; }

        /// <summary>
        /// 终止深度
        /// </summary>
        public double BotDep { get; set; }

        /// <summary>
        /// 采样间隔
        /// </summary>
        public double Spacing { get; set; }

        /// <summary>
        /// 采样点数
        /// </summary>
        public int PointsNum { get; set; }

        /// <summary>
        /// 曲线值
        /// </summary>
        public double[] Values { get; set; }

    }
}
