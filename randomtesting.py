import networkx as nx
import random
import matplotlib.pyplot as plt

g = nx.random_regular_graph(3, 100)

pr = nx.pagerank(g)

print pr

print nx.info(g)

nx.draw(g)

plt.show()