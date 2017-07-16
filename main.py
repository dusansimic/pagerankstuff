import networkx as nx
import matplotlib.pyplot as plt

gleft = nx.circular_ladder_graph(50)
 
# treba da se sloze i da se linkuju

gmaster = gleft

print nx.info(gmaster)

nx.draw(gmaster)

plt.show()
