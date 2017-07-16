import networkx as nx
import random
import math

def testFunc(n):
  g = nx.Graph()
  for nodeIndex in range(n):
    g.add_node(nodeIndex)
    if nodeIndex % 2 == 1:
      g.add_edge(nodeIndex-1, nodeIndex)
      for edgeIndex in range(1, int(math.sqrt(nodeIndex))):
        g.add_edge(random.randint(0, nodeIndex-2), nodeIndex)
  return g

def genGraph(n):
  centerPrecent = 0.39
  inAndOutPrecent = 0.305
  centerNum = int(n * centerPrecent)
  inAndOutNum = int(n * inAndOutPrecent)
  inAndOutEdgesPrecent = 0.5
  connectionPrecent = 0.05
  connectionNum = int((inAndOutNum + centerNum) / 2 * connectionPrecent)
  gin = nx.Graph()
  gcntr = nx.Graph()
  gout = nx.Graph()
  g = nx.Graph()
  state = True
  for nodeIndex in range(inAndOutNum):
    g.add_node(nodeIndex)
    if nodeIndex % 2 == 1:
      if state:
        state = False
        g.add_edge(nodeIndex-1, nodeIndex)
        for edgeIndex in range(1, int(math.sqrt(nodeIndex))):
          g.add_edge(random.randint(0, nodeIndex-2), nodeIndex)
      else:
        state = True
  
  state = True
  for nodeIndex in range(centerNum):
    g.add_node(inAndOutNum + nodeIndex)
    if nodeIndex % 2 == 1:
      if state:
        state = False
        g.add_edge(inAndOutNum + nodeIndex-1, nodeIndex)
        for edgeIndex in range(1, int(math.sqrt(nodeIndex))):
          g.add_edge(random.randint(inAndOutNum, inAndOutNum + nodeIndex-2), inAndOutNum + nodeIndex)
      else:
        state = True

  for connectionIndex in range(connectionNum):
    g.add_edge(random.randint(0, nodeIndex), random.randint(inAndOutNum, inAndOutNum + nodeIndex))
  
  # cleanup, remove single nodes

  for i in range(inAndOutNum + centerNum):
    if g.degree_iter(i) == 0:
      g.remove_node(i)

  #for nodeIndex in range(inAndOutNum):
  #  gout.add_node(inAndOutNum + centerNum + nodeIndex)
  #  if nodeIndex % 2 == 1:
  #    if state:
  #      state = False
  #      gout.add_edge(random(inAndOutNum + centerNum + nodeIndex-1), inAndOutNum + centerNum + nodeIndex)
  #    else:
  #      state = True

  return g