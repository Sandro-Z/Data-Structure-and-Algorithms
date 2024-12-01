"""11.写一个程序来解决这样一个问题：3个羚羊和3只狮子准备乘船过河
，河边有一艘能容纳2只动物的小船。
但是，如果两侧河岸上的狮子数量大于羚羊数量，羚羊就会被吃掉
。找到运送办法，使得所有动物都能安全渡河。"""
#我反正看不懂
from collections import Counter  # 聚集库,计算器
from random import sample,randint  # 随机列表中的元素


class Solution:
	"""解决问题的方案类"""

	def __init__(self):
		"""初始化属性"""
		self.left=['羚羊']*3+['狮子']*3  # 后面用到了Counter，所以这里可以用字符串表示，不用0,1表示，更直观一点
		self.left_checkpoint=[]  # 左边的存档，用于试错后恢复
		self.right=[]  # 右边列表初始为空
		self.right_checkpoint=[]  # 检查右边
		self.result=[[]]  # 结果，给个初始值是为了避免out of index的情况，取结果的时候切片即可
		self.result_checkpoint=[]  # 检查结果
		self.r_direction=True  # True为右，False为左

	def go(self):
		"""渡河"""
		if self.r_direction:  # 向右渡河
			boat=sample(self.left,2)  # 在左边列表随机二个元素
			for i in boat:  # 临时变量在随机二个元素列表里面循环
				self.left.remove(i)  # 左边列表删除指定对象
				self.right.append(i)  # 右边列表尾部添加
		else:  # 向左渡河
			if len(self.right)>1:  # 这里判断是为了避免sample取的时候越界(从1个里面取2个)
				boat=sample(self.right,randint(1,2))  # 在右边列表随机二个元素
			else:  # 反之
				boat=sample(self.right,1)  # 在右边列表随机一个元素
			for i in boat:  # 临时变量在随机二个元素列表里面循环
				self.right.remove(i)  # 右边列表删除指定对象
				self.left.append(i)  # # 左边列表尾部添加
		return boat  # 返回列表

	def judge(self):
		"""判断"""
		if self.left and self.right:  # 如果左边列表和右边列表
			left_counter=Counter(self.left)  # 左边元素出现的次数
			right_counter=Counter(self.right)  # 右边元素出现的次数
			if (left_counter['羚羊'] and left_counter['羚羊']<left_counter['狮子']) or\
					(right_counter['羚羊'] and right_counter['羚羊']<right_counter['狮子']):
				return False  #
		return True

	def checkpoint(self):
		"""检查点"""
		self.left_checkpoint,self.right_checkpoint,self.result_checkpoint=\
			self.left.copy(),self.right.copy(),self.result.copy(
			)  # 左边结果，右边结果，检查结果 = 拷贝左边结果，拷贝右边结果，拷贝检查结果

	def reset(self):
		"""读档"""  # 左边结果，右边结果，检查结果 = 拷贝左边结果，拷贝右边结果，拷贝检查结果
		self.left,self.right,self.result=\
			self.left_checkpoint.copy(),self.right_checkpoint.copy(),self.result_checkpoint.copy()

	def get_result(self):
		"""模拟渡河过程，获取结果"""
		while len(self.right)<6:  # 右边的个数小于6就循环
			self.checkpoint()  # 存档
			boat=self.go()  # 渡河
			boat.sort()  # 排序
			# 这里判断是为了避免相同的人来回的情况，以求尽可能少的解
			if self.judge() and boat!=self.result[-1]:
				self.r_direction=not self.r_direction  # 调转船头
				self.result.append(boat)
			else:
				self.reset()  # 读档
		return self.result[1:]


def main():
	"""主函数"""
	repeat=165  # 重复执行次数
	result_set=set()  # 解的集合
	solution=Solution()  # 创建对象

	for _ in range(repeat):  # 在指定的次数里循环
		result=solution.get_result()
		result_set.add(str(result))  # 把结果添加到集合
		solution.__init__()  # 对象调用属性

	print(f'经{repeat}次执行，共得到{len(result_set)}种不同的结果，结果如下：',end='\n\n')
	for result in result_set:  # 在集合里循环
		print(result)  # 打印


if __name__=='__main__':
	main()