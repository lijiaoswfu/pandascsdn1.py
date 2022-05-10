from docx import Document
from docx.shared import Pt,RGBColor
from docx.oxml.ns import qn

doc = Document()
# print(doc.add_heading("一级标题", level=1))   添加一级标题的时候出错，还没有解决！
str = '我是很英俊的李骄'
paragraph1 = doc.add_paragraph()
run1 = paragraph1.add_run("这是一个段落"+str)
run1.font.name=u'Cambria'

paragraph2 = doc.add_paragraph("这是第二个段落")
doc.save('new.docx')
"""
添加段落的时候，赋值给一个变量，方便我们后面进行格式调整；
"""