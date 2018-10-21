import networkx as nx
import data
import pandas as pd


api = data.generate_API()
u_ini = []
u_path = []
aux_unif = []


def create_neighbours(G):
	for user_id in list(G.nodes):
		followers = data.get_followers(user_id, api)
#		following = data.get_following(user_id, api)
#		followers = [1,2,3,4,5,6,7]
#		following = [9,8,10]
		for follower in followers:
			G.add_edge(user_id, follower)
#		for follow in following:
#			G.add_edge(follow, user_id)
	print(G.nodes)



def init_graph():
	G = nx.DiGraph()   
	files = ["checked_#BolsonaroNao_bots" ]

	for f in files:
		bf = pd.read_csv(f, skiprows=1, names = ['user_id','score'])
		user_list = bf['user_id'].tolist()
		
		for user_id in user_list:
			G.add_node(user_id)

	create_neighbours(G)		
	return G


def main():
	G = init_graph()

	

if __name__ == '__main__':
	main()