import networkx as nx
import data
import pandas as pd
import random

api = data.generate_API()
L_nodes = []
visited_nodes = []
aux_unif = []

file = open("visited", "w+")

def create_neighbours(G):
	for user_id in list(G.nodes):
		followers =  data.get_followers(user_id, api)
		following = data.get_following(user_id, api)
		for follower in followers:
			G.add_edge(user_id, follower)
		for follow in following:
			G.add_edge(follow, user_id)


def write_file(rand_edge):
	file.write(str(rand_edge))
	file.write("\n")
	file.flush()

def next_node(G):

	print("\n### next node ###")
	edges_list = []

	while not edges_list:
		print("edges list")
		rand = random.choice(aux_unif)
		edges = G.edges(L_nodes[rand])
		edges_list = [i[1] for i in edges]
		print("## edges list")
		print(len(edges_list))
		print(rand)

	rand_edge = random.choice(edges_list)
	print("selected: "+ str(rand_edge))
	L_nodes[rand] = rand_edge
	visited_nodes.append(rand_edge)

	write_file(rand_edge)
	generate_auxunif(G)


def generate_auxunif(G):
	nd = 0
	aux_unif = []
	for user_id in range(len(L_nodes)):
		print("node"+str(L_nodes[user_id]))
		for i in range(G.degree(L_nodes[user_id])):
			aux_unif.append(nd)
		nd = nd + 1	

#def frontier_sampling(G):

def init_graph():
	G = nx.DiGraph()   
	l = [1865894354, 1053306459897901056, 95352888, 2531361868, 459711130]
	for n in l:
		G.add_node(n)
		L_nodes.append(n)

	create_neighbours(G)
	generate_auxunif(G)

	i = 0
	for i in range(99999999999):
		next_node(G)

	print("\n\n")
	print(visited_nodes)
	print(G.nodes)
	print(G.edges)
	file.close()		
	return G	

def main():
	G = init_graph()

	

if __name__ == '__main__':
	main()
