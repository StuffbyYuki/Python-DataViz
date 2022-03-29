import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
df = pd.read_csv('data.csv') # pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
 
G=nx.from_pandas_edgelist(df, 'source', 'target', edge_attr=True)
 
nx.draw(G, with_labels=True)
plt.show()
