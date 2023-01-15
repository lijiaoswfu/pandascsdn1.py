#include "ch1.h"
#include <ui_ch1.h>
#include <qgridlayout>
#include <qlabel>
#include <QlineEdit>
#include <qpushbutton>
#include <qdebug.h>
#include <qcoreapplication.h>

ch1::ch1(QWidget* parent)
	: QDialog(parent)
{
	// 界面设计
	ui.setupUi(this);
	label1 = new QLabel(this);
	label1->setText(tr(u8"请输入圆的半径："));
	lineEdit = new QLineEdit(this);
	label2 = new QLabel(this);
	button = new QPushButton(this);
	button->setText(tr(u8"显示对应圆的面积："));
	label3 = new QLabel(this);
	QGridLayout* mainLayout = new QGridLayout(this);
	mainLayout->addWidget(label1, 0, 0);
	mainLayout->addWidget(lineEdit, 0, 1);
	mainLayout->addWidget(label2, 1, 0);
	mainLayout->addWidget(button, 1, 1);
	mainLayout->addWidget(label3, 2, 0);

	// 按钮动作（信号和槽的对应关系）
	connect(button, SIGNAL(clicked()), this, SLOT(showArea()));
}

const static double PI = 3.1416;
void ch1::showArea()
{
	bool ok;
	QString tempStr;
	QString valueStr = lineEdit->text();
	int valueInt = valueStr.toInt(&ok);
	double area = valueInt * valueInt * PI;
	label2->setText(tempStr.setNum(area));

	// 字符串连接
	QString str1 = u8"欢迎";
	QString str2 = u8"来到";
	str1.append(str2);
	str1.append(u8"重庆");
	QString str;
	str = QString(u8"%1是我的%2").arg(u8"小薇安").arg("最爱");
	str1.append(str);

	// 判断字符串是否以XX开头,然后根据Ture or Flase做出不同的响应
	if (str1.contains(u8"欢迎", Qt::CaseInsensitive))
		label3->setText(str);
	else
		label3->setText(str1);

	// 字符串转换为整数，同时将整数转换为字符串打印到label
	QString str4 = "125";
	int hex = str4.toInt(&ok, 16);
	int dec = str4.toInt(&ok, 8);
	QString ceShi1;
	QString ceShi2;
	label1->setText(ceShi1.setNum(hex) + ceShi2.setNum(dec));

	// QList类存储策略和字符串写入
	QList<QString> list;
	QString str5(u8"这是一个测试字符串");
	list << str5;
	QString str6 = u8"你好，";
	qDebug() << list[0] << str6;

	// Java风格迭代器遍历容器Qlist
	QList<int> list1;
	list1 << 1 << 2 << 3 << 4 << 5;
	QListIterator<int> i(list1);
	for (; i.hasNext();)
		qDebug() << i.next();

	// Qlist读写遍历法
	QList<int> List2;                           //创建一个空的列表list2
	QMutableListIterator<int> m(List2);         //创建上述列表的读写迭代器
	for (int j = 0; j < 10; ++j)
		m.insert(j);                            //通过QMutableListIterator<T>::insert()插入操作，为该列表插入10个整数值
	for (m.toFront(); m.hasNext();)             //移动迭代器的迭代点到列表前端，完成对列表的遍历和输出
		qDebug() << m.next();
	for (m.toBack(); m.hasPrevious();)          //移动迭代器的迭代点到列表后端，完成对列表的遍历，如果前一个列表项的值为偶数，则将该列表项删除，否则，将该列表项修改为原来的10倍
	{
		if (m.previous() % 2 == 0)
			m.remove();
		else
			m.setValue(m.peekNext() * 10);     //修改遍历函数跳过的列表项的值，但不会移动迭代点的位置，找到对应列表项则修改值，找不到则不修改
	}
	for (m.toFront(); m.hasNext();)
		qDebug() << m.next();


}

