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

# import time

# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt

# G=nx.grid_2d_graph(4,4)  #4x4 grid

# pos=nx.spring_layout(G,iterations=100)

# # plt.subplot(2,2,1)
# nx.draw(G,pos,font_size=8)

# # plt.subplot(2,2,2)
# # nx.draw(G,pos,node_color='k',node_size=0,with_labels=False)

# # plt.subplot(2,2,3)
# # nx.draw(G,pos,node_color='g',node_size=250,with_labels=False,width=6)

# # plt.subplot(2,2,4)
# # H=G.to_directed()
# # nx.draw(H,pos,node_color='b',node_size=20,with_labels=False)

# # plt.savefig("four_grids.png")
# plt.show()








# # fig, axesList = plt.subplots(2,2)
# # x = np.arange(0, 10, 0.2)
# # y = np.sin(x)

# # axesList[0][0].plot(x,y)


# # plt.show()




# # G = nx.Graph()
# # G.add_edges_from(
# #     [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
# #      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

# # val_map = {'A': 1.0,
# #            'D': 0.5714285714285714,
# #            'H': 0.0}

# # values = [val_map.get(node, 0.25) for node in G.nodes()]

# # nx.draw(G, cmap = plt.get_cmap('jet'), node_color = values)
# # plt.show()
# # plt.close()

# # G.add_edges_from([("F","D")])
# # nx.draw(G, cmap = plt.get_cmap('jet'), node_color = values)
# # plt.draw()
# # plt.show()

