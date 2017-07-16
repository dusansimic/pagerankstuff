import networkx as nx
import random
import matplotlib.pyplot as plt

g = nx.random_regular_graph(5, 500)

pr = nx.pagerank(g)

print pr

print nx.info(final)

nx.draw(final)

plt.show()