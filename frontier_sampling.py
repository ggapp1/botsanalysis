import networkx as nx
import data


api = data.generate_API()

def create_neighbours(G):
	for user_id in list(G.nodes):
#		followers = data.get_followers(user_id, api)
#		following = data.get_following(user_id, api)
		followers = [1,2,3,4,5,6,7]
		following = [9,8,10]
		for follower in followers:
			G.add_edge(user_id, follower)
		for follow in following:
			G.add_edge(follow, user_id)
	print G.nodes


def init_graph():
	G = nx.DiGraph()   
	G.add_node(513768992)

	create_neighbours(G)
	return G



def main():

	G = init_graph()
	print(G.degree(513768992))

	print(G.out_edges(513768992))

if __name__ == '__main__':
	main()