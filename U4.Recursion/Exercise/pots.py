#水桶问题可能对于某些数据是无解的，而对于有解的问题本程序也只能解决一部分，这是由于递归链条单一导致的。
import sys
sys.setrecursionlimit(999999999)
class Pot:
	def __init__(self,name,volume):
		self.volume=volume
		self.water_inside=0
		self.name=name

	def fill(self):
		print('filling pot {} to full'.format(self.name))
		self.water_inside=self.volume

	def empty(self):
		print('emptying pot {}'.format(self.name))
		self.water_inside=0

	def transfer(self,pot):
		print('transfering {0} gallons of water from pot {1} to pot {2}'.format((self.water_inside if pot.volume-pot.water_inside>=self.water_inside else pot.volume-pot.water_inside),self.name,pot.name))
		transfer_volume=(self.water_inside if pot.volume-pot.water_inside>=self.water_inside else pot.volume-pot.water_inside)
		pot.water_inside+=transfer_volume
		self.water_inside-=transfer_volume

def move_water(potA:Pot,potB:Pot,target):
	potA.fill()
	potA.transfer(potB)
	if potA.water_inside==target:
		print('complete')
		return
	potB.empty()
	potA.transfer(potB)
	if potA.water_inside==target:
		print('complete')
		return
	else:move_water(potA,potB,target)


if __name__=='__main__':
	pot1=Pot('A',5)
	pot2=Pot('B',3)
	move_water(pot1,pot2,3)

'''
以下是另一种解决方法：
s1=Stack()  # 创建对象3升桶
s2=Stack()  # 创建对象4升桶


def solution(a,b,c):  # 定义函数（3升桶，4升桶，要装几升）
	for i in range(b):
		s2.push('water')  # 把4升桶装满
	print('----------------------------------------------------')
	print('Initial')
	print('3升桶:',s1.items)
	print('4升桶:',s2.items)

	for i in range(a):  # 把3升桶装满
		s1.push(s2.pop())  # 把4升桶倒入3升桶
	print('----------------------------------------------------')
	print('把 4升桶 的水倒入 3升桶:')
	print('3升桶:',s1.items)
	print('4升桶:',s2.items)

	if not s2.size()==c:  # 4升桶不等于2升水（递归出口）
		for i in range(a):  # 把3升桶的水倒掉
			s1.pop()
		print('----------------------------------------------------')
		print('drop 3升桶:')
		print('3升桶:',s1.items)
		print('4升桶:',s2.items)

		s1.push(s2.pop())  # 把4升桶倒入3升桶
		return solution(2*a-b,b,c)  # 递归
	else:
		print('----------------------------------------------------')
		return 'comleted'
'''