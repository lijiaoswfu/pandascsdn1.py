from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.shared import Pt

doc = Document()
# print(doc.add_heading("一级标题", level=1))   添加一级标题的时候出错，还没有解决！
strHead = '重庆市涪陵区林业规划和资源监测中心关于曾淑明居民房占地的现场勘验报告'
paragraphHead = doc.add_paragraph()
runHead = paragraphHead.add_run(strHead) # 变量代入内容
runHead.font.name='方正小标宋_GBK'
runHead.font.element.rPr.rFonts.set(qn('w:eastAsia'), '方正小标宋_GBK')  # 设置中文字体
runHead.font.size = Pt(22) # 字体大小
paragraph_formatHead = paragraphHead.paragraph_format
paragraph_formatHead.line_spacing = Pt(30)  # 固定值，30磅
paragraphHead.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 段落居中对齐

paragraphFirst = doc.add_paragraph()
strFirst = "按照区林业局安排，我中心就曾淑明居民房占地一案，本着实事求是、客观公正的原则，严格按照相关调查技术规范，深入现场进行了实地勘验。现就勘验情况报告如下："
runFirst = paragraphFirst.add_run(strFirst)
runFirst.font.name='方正仿宋_GBK'
runFirst.font.element.rPr.rFonts.set(qn('w:eastAsia'), '方正仿宋_GBK')
runFirst.font.size = Pt(16)
paragraph_formatFirst = paragraphFirst.paragraph_format
paragraph_formatFirst.line_spacing = Pt(28)  # 固定值，30磅
paragraphFirst.paragraph_format.first_line_indent = Cm(2.0)

doc.save('new.docx')
"""
添加段落的时候，赋值给一个变量，方便我们后面进行格式调整；
"""