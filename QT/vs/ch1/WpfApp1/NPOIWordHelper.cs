using NPOI.SS.UserModel;
using NPOI.XWPF.UserModel;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Documents;

namespace WpfApp1
{
    internal class NPOIWordHelper
    {
        public class WordHelper
        {
            //1 创建标题
            /// <summary>
            /// 创建标题       
            /// 
            /// </summary>
            /// <param name="doc"></param>
            /// <param name="title"></param>
            public void SetDocTitle(XWPFDocument doc, string title)
            {
                XWPFParagraph p0 = doc.CreateParagraph();//创建段落
                p0.Alignment = ParagraphAlignment.CENTER;//居中显示
                XWPFRun r0 = p0.CreateRun();
                //设置字体
                r0.FontFamily = "方正小标宋";
                //设置字体大小
                r0.FontSize = 20;
                //字体是否加粗，这里加粗了
                r0.IsBold = true;
                r0.SetText(title);//写入文本
            }
            /// <summary>
            /// 创建H1
            /// </summary>
            /// <param name="doc"></param>
            /// <param name="title"></param>
            public void SetDocH1(XWPFDocument doc, string title)
            {
                XWPFParagraph p0 = doc.CreateParagraph();//创建段落
                p0.Alignment = ParagraphAlignment.LEFT;//靠左显示
                XWPFRun r0 = p0.CreateRun();
                r0.IsCapitalized = true;
                //设置字体
                r0.FontFamily = "方正仿宋";
                //设置字体大小
                r0.FontSize = 16;
                //字体是否加粗，这里加粗了
                r0.IsBold = false;
                r0.SetText(title);//写入文本

            }

            public void SetDocH2(XWPFDocument doc, string title)
            {
                XWPFParagraph p0 = doc.CreateParagraph();//创建段落
                p0.Alignment = ParagraphAlignment.LEFT;//靠左显示
                XWPFRun r0 = p0.CreateRun();
                r0.IsCapitalized = true;
                //设置字体
                r0.FontFamily = "方正仿宋";
                //设置字体大小
                r0.FontSize = 16;
                //字体是否加粗，这里加粗了
                r0.IsBold = false;
                r0.SetText(title);//写入文本

            }

            public void SetTableTitle(XWPFDocument doc, string title)
            {
                XWPFParagraph p1 = doc.CreateParagraph();
                p1.Alignment = ParagraphAlignment.CENTER;
                XWPFRun r1 = p1.CreateRun();
                r1.SetText(title);

            }

            public void SetTable(XWPFDocument doc, DataTable dt)
            {
                if (dt != null && dt.Rows.Count > 0)
                {
                    int rowCount = dt.Rows.Count;
                    int colCount = dt.Columns.Count;
                    XWPFTable table = doc.CreateTable(rowCount + 1, colCount);
                    int colWidth = 38 / colCount;
                    colWidth = colWidth == 0 ? 1 : colWidth;
                    //设置宽度
                    for (int i = 0; i < colCount; i++)
                    {
                        table.SetColumnWidth(i, (ulong)colWidth * 256);//设置列的宽度
                    }
                    //填写表的第一行
                    for (int i = 0; i < colCount; i++)
                    {
                        string colName = dt.Columns[i].ColumnName;
                        table.GetRow(0).GetCell(i).SetText(colName);
                    }

                    //填写表的内容
                    for (int i = 0; i < rowCount; i++)
                    {
                        for (int j = 0; j < colCount; j++)
                        {
                            string value = dt.Rows[i][j].ToString();
                            table.GetRow(i + 1).GetCell(j).SetText(value);
                        }
                    }
                }
            }

        }

    }
}
//XWPFParagraph paragraph = document.CreateParagraph();//创建段落对象
//paragraph.Alignment = paragraphAlign;//文字显示位置,段落排列（左对齐，居中，右对齐）

//XWPFRun xwpfRun = paragraph.CreateRun();//创建段落文本对象
//xwpfRun.IsBold = isBold;//文字加粗
//xwpfRun.SetText(fillContent);
//xwpfRun.FontSize = fontSize;//设置文字大小
//xwpfRun.IsItalic = isItalic;//是否设置斜体（字体倾斜）
//xwpfRun.SetColor(fontColor);//设置字体颜色--十六进制
//xwpfRun.SetFontFamily(fontFamily, FontCharRange.None); //设置标题样式如：（微软雅黑，隶书，楷体）根据自己的需求而定
//xwpfRun.IsDoubleStrikeThrough = isDoubleStrike;//是否显示双删除线
//xwpfRun.IsStrikeThrough = isStrike;//是否显示单删除线
//xwpfRun.SetUnderline(underline);//设置下划线，枚举类型
//xwpfRun.SetTextPosition(20);//设置文本位置
//xwpfRun.AddBreak();//设置换行（</br>）
//xwpfRun.AddTab();//添加tab键
//xwpfRun.AddCarriageReturn();//添加回车键
//xwpfRun.IsImprinted = isImprinted;//印迹（悬浮阴影）,效果和浮雕类似
//xwpfRun.IsItalic = isItalic;//是否设置斜体（字体倾斜）
//xwpfRun.Subscript = vertical;//设置下标，枚举类型
