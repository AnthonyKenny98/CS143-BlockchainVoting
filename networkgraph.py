import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def plot():
	
	G = nx.Graph()
	G.add_edges_from([(1,2),(2,3),(3,4), (1,5), (1,6)])

	pos=nx.spring_layout(G,iterations=100)

	nx.draw(G,pos,font_size=8,with_labels=True)

	plt.show()

plot()