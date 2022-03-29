from pyvis.network import Network
import pandas as pd
import matplotlib.pyplot as plt

net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')

# set the physics layout of the network
net.barnes_hut()
got_data = pd.read_csv('data.csv')

sources = got_data['source']
targets = got_data['target']
weights = got_data['weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net.add_node(src, src, title=src)
    net.add_node(dst, dst, title=dst)
    net.add_edge(src, dst, value=w)

neighbor_map = net.get_adj_list()

# add neighbor data to node hover data
for node in net.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

plt.show()
net.show('myfamily.html')
