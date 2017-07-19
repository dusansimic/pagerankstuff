import networkx as nx
import matplotlib.pyplot as plt
from gengraph import *

<<<<<<< HEAD
<<<<<<< HEAD
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv

g = genGraph(50)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))

#print nx.info(g)

a = to_agraph(g)

print a

a.layout('dot')
a.draw('graph.png')
=======
g = genGraph(50)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))

#print nx.info(g)

nx.draw_networkx(g)

plt.show()
>>>>>>> c312993e7655333ec922c09687403982d621ec32
=======
g = genGraph(50)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))

#print nx.info(g)

nx.draw_networkx(g)

plt.show()
>>>>>>> c312993e7655333ec922c09687403982d621ec32
