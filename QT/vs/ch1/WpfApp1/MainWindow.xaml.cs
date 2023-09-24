using System;
using System.Collections.Generic;
using System.IO;
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
using System.Windows.Navigation;
using System.Windows.Shapes;
using NPOI.SS.UserModel;
using NPOI.XSSF.UserModel;
using NPOI.XWPF.UserModel;
using OxyPlot;
using OxyPlot.Annotations;
using OxyPlot.Axes;
using OxyPlot.Legends;
using OxyPlot.Series;
using OxyPlot.Wpf;
using System.Data.SQLite;
using System.Xml.Linq;
using System.Data;
using static WpfApp1.dataTableNpoi;
using System.Collections.ObjectModel;
using NPOI.SS.Formula.Functions;
using System.ComponentModel;
using NPOI.WP.UserModel;
using static WpfApp1.NPOIWordHelper;
using static WpfApp1.DataTableToSqlite;
using HandyControl.Controls;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>


    public partial class MainWindow : System.Windows.Window
    {
        //全局声明
        private PlotModel model;
        SQLiteHelper helper = new SQLiteHelper("sqliteGis.db");
        DataTable dtGIS;

        private DataTable GetDataTable(string sqldbpath, string sql)
        {
            SQLiteHelper.ConnSqlLiteDbPath = sqldbpath;
            string sError = "";

            return SQLiteHelper.GetDataTable(out sError, sql);

        }
        private void InitDB()
        {
            string sql = "select * from user";
            DataTable dt = GetDataTable(@"sqliteGis.db", sql);
            this.DataGridSql.ItemsSource = dt.DefaultView;
        }

        public MainWindow()
        {
            InitializeComponent();

            //DataGrid绑定数据
            InitDB();


            //oxyplot制图
            model = new PlotModel
            {
                Title = "随机图表栏",
                TitleColor = OxyColors.LightGray,
                Subtitle = "李骄制作",
                SubtitleColor = OxyColors.DarkOrange,

                //改边框颜色
                PlotAreaBorderThickness = new OxyThickness(2),
                PlotAreaBorderColor = OxyColors.Gray
            };

            //设置轴体
            var axisX = new LinearAxis
            {
                Title = "X轴",
                TitlePosition = 0.5f,
                MajorStep = 1,
                MinorStep = 0.5,
                Position = AxisPosition.Bottom,
                MajorGridlineColor = OxyColors.Gray,
                MinorGridlineColor = OxyColors.Gray,
                MajorGridlineStyle = OxyPlot.LineStyle.Solid,
                MinorGridlineStyle = OxyPlot.LineStyle.Dot,
                IntervalLength = 1,
                TicklineColor = OxyColors.Gray,

                TextColor = OxyColors.White
            };


            var axisY = new LinearAxis
            {
                Title = "Y轴",
                TitlePosition = 0.5f,
                MajorStep = 1,
                MinorStep = 0.5,
                Position = AxisPosition.Left,
                //网格
                MajorGridlineColor = OxyColors.Gray,
                MinorGridlineColor = OxyColors.Gray,
                MajorGridlineStyle = OxyPlot.LineStyle.Solid,
                MinorGridlineStyle = OxyPlot.LineStyle.Dot,
                IntervalLength = 1,
                TicklineColor = OxyColors.Gray,
                TextColor = OxyColors.White

            };


            model.Axes.Add(axisX);
            model.Axes.Add(axisY);

            //添加数据
            var series1 = new LineSeries
            {
                Title = "天然气",
                MarkerType = MarkerType.Circle,
                InterpolationAlgorithm = InterpolationAlgorithms.CanonicalSpline,
                RenderInLegend = true,

            };
            var series2 = new LineSeries
            {
                Title = "石油",
                MarkerType = MarkerType.Circle,
                InterpolationAlgorithm = InterpolationAlgorithms.CanonicalSpline,
            };


            Random rdm = new Random();
            for (int i = 0; i < 10; i++)
            {
                int value1 = rdm.Next(10);
                int value2 = rdm.Next(10);
                series1.Points.Add(new DataPoint(i, value1));
                series2.Points.Add(new DataPoint(i, value2));
            }
            model.Series.Add(series1);
            model.Series.Add(series2);

            //设置图例
            Legend legend = new Legend
            {
                LegendPlacement = LegendPlacement.Outside,
                LegendPosition = LegendPosition.TopRight,
                LegendOrientation = LegendOrientation.Horizontal,
                LegendBorderThickness = 1,
                LegendTextColor = OxyColors.LightGray,
            };


            model.Legends.Add(legend);



            PlotChart.Model = model;


            //在指定位置生成提示线
            LineAnnotation annoVertical = new LineAnnotation();
            LineSeries series = (LineSeries)PlotChart.Model.Series[1];
            annoVertical.Type = LineAnnotationType.Vertical;
            annoVertical.X = series.Points[3].X;

            annoVertical.LineStyle = OxyPlot.LineStyle.LongDashDotDot;
            annoVertical.Color = OxyColors.Cyan;

            PlotChart.Model.Annotations.Add(annoVertical);

            LineAnnotation annoHorizontal = new LineAnnotation();
            annoHorizontal.Type = LineAnnotationType.Horizontal;
            annoHorizontal.Y = series.Points[3].Y;
            annoHorizontal.LineStyle = OxyPlot.LineStyle.LongDashDot;
            annoHorizontal.Color = OxyColors.Cyan;

            PlotChart.Model.Annotations.Add(annoHorizontal);

            PlotChart.Model.InvalidatePlot(true);

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Window3DGIS wG3d = new Window3DGIS();
            wG3d.Show();
            System.Windows.MessageBox.Show("导出数据到EXCEL完毕");
            // 新建工作簿对象
            XSSFWorkbook workBook = new();
            // 写入文件
            workBook.Write(new FileStream(@"test.xlsx", FileMode.Create));
            ISheet sheet = workBook.CreateSheet("mySheet");
            // 修改单元格的值
            for (int i = 0; i < 20; i++)
            {
                for (int j = 0; j < 20; j++)
                {
                    sheet.CreateRow(i).CreateCell(j).SetCellValue(i + j);
                }
            }

            workBook.Write(new FileStream(@"test.xlsx", FileMode.OpenOrCreate, FileAccess.ReadWrite));



        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            WindowGIS wG = new();
            wG.Show();
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            // 创建空白文档
            XWPFDocument doc = new XWPFDocument();

            // 创建段落
            XWPFParagraph p1 = doc.CreateParagraph();
            XWPFParagraph p2 = doc.CreateParagraph();
            XWPFRun xwpfRun1 = p1.CreateRun();//创建段落文本对象
            xwpfRun1.SetFontFamily("方正小标宋", FontCharRange.None);
            XWPFRun xwpfRun2 = p2.CreateRun();//创建段落文本对象
            xwpfRun2.SetFontFamily("方正仿宋", FontCharRange.None);

            // 设置段落文本
            p1.CreateRun().SetText("科学划定宜耕土地后备资源范围，留足留优耕地占补平衡、进出平衡和补足耕地保护目标任务缺口的资源空间，是守住耕地保护红线十分重要的一项基础性工作。为此，依据《关于开展耕地后备资源空间范围核实确认工作的通知》（渝规资〔2023〕104号），开展涪陵区耕地后备资源空间范围核实确认工作，挖掘耕地后备资源，摸清资源底数，明确资源边界，固化耕地后备资源空间范围，推进科学合理开发，为实现耕地“两平衡”、补足目标任务缺口，落实耕地保护和粮食安全责任夯实基础。");
            p2.CreateRun().SetText("本次核实确认耕地后备资源空间范围为可整治的农用地，包括国土变更调查中标注“即可恢复”和“工程恢复”的园地、林地、坑塘水面等农用地，实施整治恢复耕地可用于耕地“进出平衡”以及水库淹没区占用耕地补充；还包括二调以来非耕地中未标注“恢复属性”的宜耕园地、林地，实施整治新增耕地可用于非农业建设占用耕地的占补平衡。");


            // 创建表格
            XWPFTable table = doc.CreateTable(3, 4);

            // 设置表格内容
            table.GetRow(0).GetCell(0).SetText("行政区");
            table.GetRow(0).GetCell(1).SetText("可用于进出平衡潜力");
            table.GetRow(0).GetCell(2).SetText("可用于占补平衡潜力");
            table.GetRow(0).GetCell(3).SetText("小计");
            table.GetRow(1).GetCell(0).SetText("崇义街道");
            table.GetRow(2).GetCell(0).SetText("荔枝街道");

            // 保存文档
            FileStream stream = new FileStream("test.docx", FileMode.Create);
            doc.Write(stream);
            stream.Close();
            System.Windows.MessageBox.Show("Word文档已保存！");

            //第二个WROD文档
            XWPFDocument docx = new XWPFDocument();
            MemoryStream ms = new MemoryStream();
            WordHelper wordHelper = new WordHelper();
            //1 设置标题
            wordHelper.SetDocTitle(docx, "第二个WORD文档");
            //2 创建模块信息
            wordHelper.SetDocH1(docx, "科学划定宜耕土地后备资源范围，留足留优耕地占补平衡、进出平衡和补足耕地保护目标任务缺口的资源空间，是守住耕地保护红线十分重要的一项基础性工作。为此，依据《关于开展耕地后备资源空间范围核实确认工作的通知》（渝规资〔2023〕104号），开展涪陵区耕地后备资源空间范围核实确认工作，挖掘耕地后备资源，摸清资源底数，明确资源边界，固化耕地后备资源空间范围，推进科学合理开发，为实现耕地“两平衡”、补足目标任务缺口，落实耕地保护和粮食安全责任夯实基础。\"");
            wordHelper.SetTableTitle(docx, "本次核实确认耕地后备资源空间范围为可整治的农用地，包括国土变更调查中标注“即可恢复”和“工程恢复”的园地、林地、坑塘水面等农用地，实施整治恢复耕地可用于耕地“进出平衡”以及水库淹没区占用耕地补充；还包括二调以来非耕地中未标注“恢复属性”的宜耕园地、林地，实施整治新增耕地可用于非农业建设占用耕地的占补平衡。");

            //3 创建表的信息
            wordHelper.SetTable(docx, dtGIS);
            docx.Write(ms);
            using (FileStream fs = new FileStream("第二个WORD文档.docx", FileMode.Create, FileAccess.Write))
            {
                byte[] data = ms.ToArray();
                fs.Write(data, 0, data.Length);
                fs.Flush();
            }
            ms.Close();
        }

        //插入SQL数据
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            helper.connection.Open();
            helper.ExecuteNonQuery("INSERT INTO user ('姓名', '年龄') VALUES ('Tom', 20)");
            helper.ExecuteNonQuery("INSERT INTO user ('姓名', '年龄') VALUES ('Jerry', 18)");
            helper.ExecuteNonQuery("INSERT INTO user ('姓名', '年龄') VALUES ('Marry', 23)");
            helper.ExecuteNonQuery("CREATE TABLE zrbh AS SELECT * FROM \"自然保护地\" LEFT JOIN \"2023\" ON \"自然保护地\".xinxuhao = \"2023\".\"序号\"");
            System.Windows.MessageBox.Show("插入数据并合成数据成功！");
            helper.connection.Close();

            InitDB();
        }

        //查询SQL数据
        private void Button_Click_4(object sender, RoutedEventArgs e)
        {
            helper.connection.Open();
            SQLiteDataReader reader = helper.ExecuteReader("SELECT * FROM user");
            while (reader.Read())
            {
                string name = reader.GetString(0);
                int age = reader.GetInt32(1);
                Console.WriteLine($"name: {name}, age: {age}");
                System.Windows.MessageBox.Show($"name: {name}, age: {age}" + "查询数据成功！");
            }
            helper.connection.Close();
            InitDB();

        }

        //更新SQL数据
        private void Button_Click_5(object sender, RoutedEventArgs e)
        {
            helper.connection.Open();
            helper.ExecuteNonQuery("UPDATE user SET 年龄 = 21 WHERE 姓名 = 'Tom'");
            System.Windows.MessageBox.Show("更新数据成功！");
            helper.connection.Close();
            InitDB();

        }

        //删除SQL数据
        private void Button_Click_6(object sender, RoutedEventArgs e)
        {
            helper.connection.Open();
            helper.ExecuteNonQuery("DELETE FROM user WHERE 姓名 = 'Tom'");
            System.Windows.MessageBox.Show("删除数据成功！");
            helper.connection.Close();
            InitDB();
        }

        private void Button_Click_7(object sender, RoutedEventArgs e)
        {
            Gmap gmap = new();
            gmap.Show();
        }

        private void Button_Click_toTable(object sender, RoutedEventArgs e)
        {

            using (ExcelHelper excelHelper = new ExcelHelper(@"C:\carl\PythonExcel\pandas book\Data\baohu.xlsx"))
            {
                dtGIS = excelHelper.ExcelToDataTable("自然保护地", true);//读取数据  
                DataGridexcel.ItemsSource = dtGIS.DefaultView;
                foreach (DataRow dr in dtGIS.Rows)//DataTable转ObservableCollection  
                {
                    //persons.Add(new Person(dr[0].ToString(), Int32.Parse(dr[1].ToString()), dr[2].ToString(), dr[3].ToString()));
                }
            }
        }

        private void Button_Click_toExcel(object sender, RoutedEventArgs e)
        {
            using (ExcelHelper excelHelper = new ExcelHelper("写入勘验数据.xlsx"))//定义一个范围，在范围结束时处理对象  
            {
                excelHelper.DataTableToExcel(dtGIS, "MySheet", true);
            }
        }

        private void Button_Click_toSqlite(object sender, RoutedEventArgs e)
        {
            //建表
            helper.connection.Open();
            string createSql = "create table baohu ('MIAN_JI' char(50),'占地属性' text,'细斑号' int,'项目名称' text,'现勘时间' text,'勘测人员' text,'备注' text,'xinxuhao' int)";
            helper.ExecuteNonQuery(createSql);
            //insert 语句
            //string commandText = "INSERT INTO baohu('MIAN_JI','占地属性','细斑号','项目名称','现勘时间','勘测人员','备注','xinxuhao')VALUES(@'MIAN_JI',@'占地属性',@'细斑号',@'项目名称',@'现勘时间',@'勘测人员',@'备注',@'xinxuhao')";
            string commandText = "INSERT INTO baohu('MIAN_JI')VALUES(@'MIAN_JI')";
            helper.ExecuteMutliQuery(commandText, dtGIS);

        }
    }
}
