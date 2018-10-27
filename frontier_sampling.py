import networkx as nx
import data
import pandas as pd
import random

api = data.generate_API()
L_nodes = []
visited_nodes = []
aux_unif = []


def create_neighbours(G):
	for user_id in list(G.nodes):
#		followers = data.get_followers(user_id, api)
#		following = data.get_following(user_id, api)
		followers = [1,2,3,4,5]
		following = [1,2,3,4,5]
		for follower in followers:
			G.add_edge(user_id, follower)
		for follow in following:
			G.add_edge(follow, user_id)
	print(G.nodes)

def next_node(G):

	print("\n### next node ###")
	print(L_nodes)
	rand = random.choice(aux_unif)
	edges = G.edges(L_nodes[rand])
	edges_list = [i[1] for i in edges]
	rand_edge = random.choice(edges_list)
	print(L_nodes[rand])
	print(edges_list)
	print(rand_edge)
	L_nodes[rand] = rand_edge
	visited_nodes.append(rand_edge)
	generate_auxunif(G)


def generate_auxunif(G):
	nd = 0

	for user_id in range(len(L_nodes)):
		print("node"+str(L_nodes[user_id]))
		for i in range(G.degree(L_nodes[user_id])):
			aux_unif.append(nd)
		nd = nd + 1	

#def frontier_sampling(G):




def init_graph():
	G = nx.DiGraph()   
	files = []
	l = [6,7]
	for n in l:
		G.add_node(n)
		L_nodes.append(n)

	create_neighbours(G)
	generate_auxunif(G)
	print("\n\n")
	print(aux_unif)
	#while True:
	#	next_node(G)
	#print("\n\n")
	#print(visited_nodes)
	print(G.nodes)
	print(G.edges)		
	return G	
"""	
	for f in files:
		bf = pd.read_csv(f, skiprows=1, names = ['user_id','score'])
		user_list = bf['user_id'].tolist()
		
		for user_id in user_list:
			G.add_node(user_id)
"""

def main():
	G = init_graph()

	

if __name__ == '__main__':
	main()