import networkx as nx
import matplotlib.pyplot as plt
from gengraph import *

g = genGraph(2000)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))

#print nx.info(g)

nx.draw(g)

plt.show()