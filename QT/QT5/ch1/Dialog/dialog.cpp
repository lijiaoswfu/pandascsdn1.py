#include "dialog.h"
#include "ui_dialog.h"

const static double PI = 3.1416;
Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_countBtn_clicked()
{
    bool ok;
    QString str1 = "Welcome";
    str1 = str1 + "to you!";
    QString str2 = "Hello,";
    str2 += "Word!";
    ui -> areaLable_2 -> setText(str2 + str1);

}
