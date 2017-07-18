import networkx as nx
import matplotlib.pyplot as plt
from gengraph import *

g = testFunc(20)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))

print nx.info(g)

nx.draw_circular(g)

plt.show()