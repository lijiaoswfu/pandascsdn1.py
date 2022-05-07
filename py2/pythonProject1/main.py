# ch_3.2 Matplotlib可视化基础
# 例3-11，绘制散点图
import numpy as np
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot库

# 产生数据
x = np.linspace(0, 10, 30)  # 产生0-10之间30个元素的等差数列
noise = np.random.randn(30)  # 产生30个标准正态分布的元素
y1 = x ** 2 + 2 * noise  # 产生叠加噪声的数据系列1
y2 = x ** 1 + 2 * noise  # 产生叠加噪声的数据系列2
y3 = x ** 1.5 + 2 * noise  # 产生叠加噪声的数据系列3
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei显示中文
plt.rc('font', size=10)  # 设置图中字号大小
plt.figure(figsize=(6, 4))  # 设置画布
plt.scatter(x, y1, marker='o')  # 绘制散点图
plt.scatter(x, y2, marker='*')  # 绘制散点图
plt.scatter(x, y3, marker='^')  # 绘制散点图
plt.title('散点图')  # 添加标题
plt.legend(['数据集y1', '数据集y2', '数据集y3'])  # 添加图例
plt.xlabel('x')  # 添加横轴标签
plt.ylabel('y')  # 添加纵轴标签
print("This Label1`data:",y1)
print("This Label2`data:",y2)
print("This Label3`data:",y3)
import os  # 导入os库

# 创建或访问一个文件夹，以下两条语句等效
path = 'D:\\my_python\\ch3\\output\\'
# path='D:/my_python/ch3/output/'
if not os.path.exists(path):
    os.makedirs(path)
plt.savefig(path + 'scatter.jpg')  # 保存图片
plt.show()  # 显示图片
