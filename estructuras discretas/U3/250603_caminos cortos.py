import osmnx as ox
import networkx as nx
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

G=ox.graph_from_place('Talca,Chile',network_type='all', simplify=False)
#ox.save_graphml(G, filename='talca_ciclovias.graphml')
plt.figure(figsize=(15,4))
ox.plot_graph(ox.project_graph(G),node_size=0, bgcolor='w')
plt.show()
