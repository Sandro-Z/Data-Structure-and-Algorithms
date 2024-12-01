from typing import List,Any

from pythonds3.basic import Stack
from pythonds3.trees import BinaryTree
import operator

def build_parse_tree(exp):
	fp_list=exp.split()
	p_stack=Stack()
	expr_tree=BinaryTree('')
	p_stack.push(expr_tree)
	current_tree=expr_tree

	for i in fp_list:
		if i=='(':
			current_tree.insert_left('')
			p_stack.push(current_tree)
			current_tree=current_tree.left_child
		elif i in ['+','-','*','/']:
			current_tree.root=i
			current_tree.insert_right('')
			p_stack.push(current_tree)
			current_tree=current_tree.right_child
		elif i.isdigit():
			current_tree.root=int(i)
			parent=p_stack.pop()
			current_tree=parent
		elif i==')':
			current_tree=p_stack.pop()
		else:raise ValueError('Unknown operator {}'.format(i))
	return expr_tree

def evaluate(parse_tree):
	operators={
		'+':operator.add,
		'-':operator.sub,
		'*':operator.mul,
		'/':operator.truediv
	}

	left_child=parse_tree.left_child
	right_child=parse_tree.right_child
	if left_child and right_child:
		fn=operators[parse_tree.root]
		return fn(evaluate(left_child),evaluate(right_child))
	else:return parse_tree.root

def print_exp(tree):
	result=''
	if tree:
		result='('+print_exp(tree.left_child)
		result+=str(tree._key)
		result=result+print_exp(tree.right_child)+')'
	return result
def helper(x):
	opls=[]
	for i in x:opls.append(i)
	for j in range(len(opls)):
		if opls[j] in ['1','2','3','4','5','6','7','8','9','0'] and j!=len(opls)-1:
			opls[j-1]=''
			opls[j+1]=''
	return ''.join(opls)
if __name__=='__main__':
	e=input()
	print(helper(print_exp(build_parse_tree(e))))
	print(evaluate(build_parse_tree(e)))
