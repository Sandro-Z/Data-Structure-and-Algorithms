from pythonds3 import Vertex
from pythonds3.graphs import Graph

def gen_legal_moves(row,col,board_size):
	new_moves=[]
	move_offsets=[
		(-1,-2),
		(-1,2),
		(-2,-1),
		(-2,1),
		(1,-2),
		(1,2),
		(2,-1),
		(2,1)
	]
	for r_off,c_off in move_offsets:
		if 0<=row+r_off<board_size and 0<=col+c_off<board_size:
			new_moves.append((row+r_off,c_off+col))
	return new_moves#返回的是位置

def knight_graph(board_size):
	kt_graph=Graph()
	for row in range(board_size):
		for col in range(board_size):
			node_id=row*board_size+col
			new_positions=gen_legal_moves(row,col,board_size)
			for row2,col2 in new_positions:
				other_node_id=row2*board_size+col2
				kt_graph.add_edge(node_id,other_node_id)
	return kt_graph

def knight_tour(n,path:list,u:Vertex,limit):
	u.color='gray'
	path.append(u)
	if n<limit:
		neighbors=sorted(list(u.get_neighbors()))
		i=0
		done=False
		while i<len(neighbors) and not done:
			if neighbors[i].color=='white':
				done=knight_tour(n+1,path,neighbors[i],limit)
			i+=1
		if not done:
			path.pop()
			u.color='white'
	else:done=True
	return done

class DFSGraph(Graph):
	def __init__(self):
		super.__init__()
		self.time=0


	def dfs(self):
		for vertex in self:
			vertex.color='white'
			vertex.previous=-1
		for vertex in self:
			if vertex.color=='white':self.dfs_visit(vertex)

	def dfs_visit(self, start_vertex):
		start_vertex.color='gray'
		self.time+=1
		start_vertex.discovery_time=self.time
		for next_vertex in start_vertex.get_neighbors():
			if next_vertex.color=='white':
				next_vertex.previous=start_vertex
				self.dfs_visit(next_vertex)
		start_vertex.color='black'
		self.time+=1
		start_vertex.closing_time=self.time

	def topoSort(self):
		self.dfs()
		self.__sort_list.reverse()