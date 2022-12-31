#include "dialog.h"
#include <Qgridlayout>


Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
{
    label1 = new QLabel(this);
    label1 -> setText(tr("请输入圆的半径："));
    lineEdit = new QLineEdit(this);
    label2 = new QLabel(this);
    button = new QPushButton(this);
    button -> setText(tr("显示对应圆的面积"));
    QGridLayout * mainLayout = new QGridLayout(this);
    mainLayout -> addWidget(label1,0,0);
    mainLayout -> addWidget(label2,1,0);
    mainLayout -> addWidget(lineEdit,0,1);
    mainLayout -> addWidget(button,1,1);

    connect(button,SIGNAL(clicked()),this,SLOT(showArea()));

}

Dialog::~Dialog()
{

}

void Dialog::showArea()
{

    QString valueStr = lineEdit -> text();
    valueStr = valueStr.trimmed();
    label2 -> setText(valueStr);
}
