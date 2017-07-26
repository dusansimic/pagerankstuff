import networkx as nx
import matplotlib.pyplot as plt

lajne = []

with open('links.txt', 'r') as f:
  for line in f:
    line.split(' ')
    lajne.append((line[0], line[1]))
f.close()

g = nx.Graph()
g.add_edges_from(lajne)

pr = nx.pagerank(g)

with open('output', 'w') as f:
  f.write(str(pr))
f.close()

print nx.info(g)

nx.draw(g)

plt.show()