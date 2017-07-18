import networkx as nx
import random
import math

def testFunc(n):
  centerPrecent = 0.39
  inAndOutPrecent = 0.305
  centerNum = int(n * centerPrecent)
  inAndOutNum = int(n * inAndOutPrecent)
  inAndOutEdgesPrecent = 0.5
  connectionPrecent = 0.05
  connectionNum = int((inAndOutNum + centerNum) / 2 * connectionPrecent)
  g = nx.Graph()
  for nodeIndex in range(n):
    g.add_node(nodeIndex)
    if nodeIndex > 0:
      g.add_edge(nodeIndex - 1, nodeIndex)
  g.add_edge(nodeIndex, 0)
  return g

def genGraph(n):
  centerPrecent = 0.2989
  inAndOutPrecent = 0.2337
  tubesPrecent = 0.2337
  centerNum = int(n * centerPrecent)
  inAndOutNum = int(n * inAndOutPrecent)
  inAndOutEdgesPrecent = 0.5
  connectionPrecent = 0.05
  connectionNum = int((inAndOutNum + centerNum) / 2 * connectionPrecent)
  g = nx.DiGraph()
  
  # adding in all nodes
  for nodeIndex in range(n):
    g.add_node(nodeIndex)
  

  # making three giant networks
  count = 0
  for nodeIndex in range(inAndOutNum * 2):
    a = random.randint(0, inAndOutNum)
    b = random.randint(0, inAndOutNum)
    count += 1
    g.add_edge(a, b)

  count = 0
  for nodeIndex in range(centerNum * 2):
    a = random.randint(inAndOutNum + 1, inAndOutNum + centerNum)
    b = random.randint(inAndOutNum + 1, inAndOutNum + centerNum)
    count += 1
    g.add_edge(a, b)
  
  count = 0
  for nodeIndex in range(inAndOutNum * 2):
    a = random.randint(inAndOutNum + centerNum + 1, inAndOutNum + centerNum + inAndOutNum)
    b = random.randint(inAndOutNum + centerNum + 1, inAndOutNum + centerNum + inAndOutNum)
    count += 1
    g.add_edge(a, b)

  # connect masters
  masterIn = 0
  masterCount = 0
  for nodeIndex in range(inAndOutNum):
    count = g.in_degree(nodeIndex)
    if count > masterCount:
      masterIn = nodeIndex
      masterCount = count
  
  masterCenterIn = 0
  masterCenterOut = 0
  masterCount = 0
  masterCountOut = 0
  for nodeIndex in range(centerNum):
    count = g.in_degree(inAndOutNum + nodeIndex + 1)
    if count > masterCount:
      masterCenterIn = nodeIndex
      masterCount = count
    count = g.out_degree(inAndOutNum + nodeIndex + 1)
    if count > masterCountOut:
      masterCenterOut = nodeIndex
      masterCountOut = count

  masterOut = 0
  masterCount = 0
  for nodeIndex in range(inAndOutNum):
    count = g.out_degree(inAndOutNum + centerNum + nodeIndex + 1)
    if count > masterCount:
      masterOut = nodeIndex
      masterCount = count

  g.add_edge(masterIn, masterCenterOut)
  g.add_edge(masterCenterIn, masterOut)

  #print masterIn, masterCenterIn, masterCenterOut, masterOut
  
  # cleanup, remove single nodes
  for i in range(n):
    if g.degree(i) <= 1:
      g.remove_node(i)

  return g