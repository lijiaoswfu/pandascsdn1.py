#ifndef DIALOG_H
#define DIALOG_H
#include <QLabel>
#include <QLineEdit>
#include <qpushbutton.h>
#include <QDialog>

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = 0);
    ~Dialog();

private:
    QLabel *label1,*label2;
    QLineEdit *lineEdit;
    QPushButton *button;

private slots:
    void showArea();
};


#endif // DIALOG_H
