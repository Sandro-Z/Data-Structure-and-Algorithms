from pythonds3.trees import BinaryHeap

class priorityQueue:
	def __init__(self):
		self.items=[]
		self.heap=BinaryHeap()
	def enqueue(self,item_lst):
		self.items=self.heap.heapify(item_lst)
	def dequeue(self):
		return self.heap.delete()

new_queue=priorityQueue()
new_queue.enqueue([1,4,5,3,2])
while new_queue.items:
	print(new_queue.dequeue())