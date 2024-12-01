"""12.利用turtle绘图模块修改汉诺塔程序，将盘子的移动过程可视化。提示：可以创建多只小乌龟，并将它们的形状改为长方形。"""

from turtle import *

speed(1000)
t=Turtle()
global t1,t2,t3
height=4
color=["red","orange","yellow","green","blue","purple","pink","black",'gray']


# 圆盘
class Disc(Turtle):
	def __init__(self,n):
		Turtle.__init__(self,shape="square",visible=False)  # 继承海龟属性
		self.pu()  # 抬笔
		# 矩形大小
		self.shapesize(1.5,n*1.5,2)  # 定义圆盘尺寸
		# 设置颜色
		# self.fillcolor(n / height, 0, 1 - n / height)
		self.fillcolor(color[n-1])  # 定义颜色
		self.st()  # 显示箭头形状
	# self.speed(5)


class Tower(list):  # 装列表的容器
	def __init__(self,x):  # 定义属性
		self.x=x

	# 取出盘子
	def pop(self):
		d=list.pop(self)  # 删除
		d.sety(150)  # 定义y坐标
		return d  # 返回方块

	# 加入盘子
	def push(self,d):
		d.setx(self.x)  # 定义x坐标
		d.sety(-150+34*len(self))  # 定义y坐标
		self.append(d)  # 添加到列表


def moveTower(height,fromPole,toPole,withPole):  # 定义递归传入函数和坐标
	if height>=1:  # 如果高度大于或等于1
		moveTower(height-1,fromPole,withPole,toPole)  # 继续递归
		toPole.push(fromPole.pop())  # 把第1个的最后一个删除然后放在第3个的最后
		moveTower(height-1,withPole,toPole,fromPole)  # 继续递归


def DrawPoles():  # 画三个柱子
	t.speed(0)
	t.up()
	t.left(90)
	t.pensize(10)
	DrawOnePole(-250,-200)
	DrawOnePole(0,-200)
	DrawOnePole(250,-200)


def DrawOnePole(x,y):  # 画一个柱子
	t.goto(x,y)
	t.down()
	t.fd(300)  # 高度
	t.up()


t1=Tower(-250)
t2=Tower(0)
t3=Tower(250)  # 创建对象传入坐标

ht()  # 隐藏海龟
penup()  # 落笔
goto(0,-225)  # 到坐标

DrawPoles()  # 画柱子

for i in range(height,0,-1):
	t1.push(Disc(i))  # 在a柱处取出列表中的每个圆盘在画出
print('aaa')
moveTower(height,t1,t3,t2)  # 调用递归
mainloop()  # 保存画面