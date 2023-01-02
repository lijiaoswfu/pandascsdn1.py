from qgis.core  import *
import qgis.utils
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()

    # 设置窗口的尺寸
    w.resize(400, 200)

    # 移动窗口
    w.move(600, 400)

    # 设置窗口的标题
    w.setWindowTitle('李骄第一个基于PyQt5的桌面应用程序')

    # 显示窗口
    w.show()

    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())