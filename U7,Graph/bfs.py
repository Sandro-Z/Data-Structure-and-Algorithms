from pythonds3 import Vertex
from pythonds3.graphs import Graph
from pythonds3.basic import Queue

def build_graph(filename):
	buckets={}
	the_graph=Graph()
	with open(filename,'r',encoding='utf8') as file_in:
		all_words=file_in.readlines()
	for line in all_words:
		word=line.strip()
		for i,_ in enumerate(word):
			bucket=f'{word[:i]}_{word[i+1:]}'
			buckets.setdefault(bucket,set()).add(word)
	for similar_words in buckets.values():
		for word1 in similar_words:
			for word2 in similar_words-{word1}:
				the_graph.add_edge(word1,word2)
	return the_graph

def bfs(start:Vertex):
	start.distance=0
	start.previous=None
	vert_queue=Queue
	vert_queue.enqueue(start)
	while vert_queue.size()>0:
		current:Vertex=vert_queue.dequeue()
		for neighbour in current.get_neighbors():
			if neighbour.color=='white':
				neighbour.color='gray'
				neighbour.distance=current.distance+1
				neighbour.previous=current
				vert_queue.enqueue(neighbour)
		current.color='black'

def traverse(starting_vertex):
	current=starting_vertex
	while current:
		print(current.key)
		current=current.previous

