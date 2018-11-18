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
	print("\n- creating create_neighbours")
	for user_id in list(G.nodes):
		followers =  data.get_followers(user_id, api)
		following = data.get_following(user_id, api)
		for follower in followers:
			G.add_edge(user_id, follower)
		for follow in following:	
			G.add_edge(follow, user_id)
		visited_nodes.append(user_id)

def add_node(G, user_id):
	print("\n+ adding "+str(user_id))
	followers =  data.get_followers(user_id, api)
	following = data.get_following(user_id, api)
	for follower in followers:
		if(follower not in visited_nodes): 
			G.add_edge(user_id, follower)
	for follow in following:
		if(follow not in visited_nodes):	
			G.add_edge(follow, user_id)


def write_file(rand_edge):
	file.write(str(rand_edge))
	file.write("\n")
	file.flush()

def next_node(G, aux_unif):

	print("\n# next node")
	rand = random.choice(aux_unif)
	edges = G.edges(L_nodes[rand])
	edges_list = [i[1] for i in edges]

	rand_edge = random.choice(edges_list)
	print("* selected: "+ str(rand_edge))
	L_nodes[rand] = rand_edge
	visited_nodes.append(rand_edge)

	write_file(rand_edge)
	add_node(G, rand_edge)



def generate_auxunif(G):
	nd = 0
	aux_unif = []
	print("\n& generating aux ")
	for user_id in L_nodes:
		if(G.out_degree(user_id) > 0):
			for i in range(G.degree(user_id)):
				aux_unif.append(nd)
		nd = nd + 1
	return aux_unif	


def init_graph():
	G = nx.DiGraph()   
	init_file = open('escolhidos').read().splitlines()
	l = [int(i) for i in init_file]

	for n in l:
		G.add_node(n)
		L_nodes.append(n)

	create_neighbours(G)
	aux_unif = generate_auxunif(G)

	while True:
		next_node(G, aux_unif)
		aux_unif = generate_auxunif(G)
		if not aux_unif:
			break

	print("\n\n")
	print(visited_nodes)
	file.close()		
	return G	

def main():
	G = init_graph()

	

if __name__ == '__main__':
	main()
