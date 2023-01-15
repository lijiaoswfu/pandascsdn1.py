#pragma once

#include <QtWidgets/QDialog>
#include "ui_ch1.h"
#include <qlabel.h>
#include <QlineEdit>
#include <qpushbutton.h>


class ch1 : public QDialog
{
	Q_OBJECT

public:
	ch1(QWidget* parent = Q_NULLPTR);

private:
	Ui::ch1Class ui;
	QLabel* label1, * label2, * label3;
	QLineEdit* lineEdit;
	QPushButton* button;

private slots:
	void showArea();
};
