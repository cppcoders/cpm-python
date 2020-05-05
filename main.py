import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
start = []
graph = []
atts = []
path = []
data = pd.read_csv("data4.csv")
for i in range(len(data)):
    graph.append([])
    atts.append({})
for j in range(len(data)):
    atts[j]["Name"] = data.iloc[j, 0]
    atts[j]["DU"] = data.iloc[j, 2]
    if(data.iloc[j, 1] == "-"):
        start.append(ord(data.iloc[j, 0])-65)
        continue
    for k in range(len(data.iloc[j, 1])):
        graph[ord(data.iloc[j, 1][k]) -
              65].append(ord(data.iloc[j, 0])-65)

level = [None] * (len(graph))


def BFS(s, graph):
    visited = [False] * (len(graph))
    queue = []
    for i in s:
        queue.append(i)
        level[i] = 0
        visited[i] = True
    while queue:
        s = queue.pop(0)
        path.append(s)
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                level[i] = level[s] + 1
                visited[i] = True
            else:
                level[i] = max(level[s]+1, level[i])


BFS(start, graph)

levels = [None] * len(path)
for i in range(len(path)):
    levels[i] = level[path[i]]
path = [x for y, x in sorted(zip(levels, path))]
print()
print("Path")
for i in path:
    print(str(chr(i+65)), end=' ')
for s in path:
    #print(str(chr(s+65)), " ", level[s])
    # -------------Forward--------------------
    if(data.iloc[s, 1] == "-"):
        atts[s]["ES"] = 0
    else:
        ls = []
        for k in range(len(data.iloc[s, 1])):
            ls.append(atts[ord(data.iloc[s, 1][k]) - 65]["EF"])
        atts[s]["ES"] = max(ls)
    atts[s]["EF"] = atts[s]["DU"] + atts[s]["ES"]
    # ---------------------------------

for i in range(len(graph)):
    if(graph[i] == []):
        atts[i]["LF"] = atts[i]["EF"]
        atts[i]["LS"] = atts[i]["ES"]
print()
print("------------------------")
# --------------------backward
path.reverse()
for i in path:
    if(data.iloc[i, 1] != "-"):
        for k in range(len(data.iloc[i, 1])):
            if "LF" in atts[ord(data.iloc[i, 1][k]) - 65].keys():
                atts[ord(data.iloc[i, 1][k]) - 65]["LF"] = min(atts[i]
                                                               ["LS"], atts[ord(data.iloc[i, 1][k]) - 65]["LF"])
            else:
                atts[ord(data.iloc[i, 1][k]) -
                     65]["LF"] = atts[i]["LS"]
            atts[ord(data.iloc[i, 1][k]) - 65]["LS"] = atts[ord(data.iloc[i, 1]
                                                                [k]) - 65]["LF"] - atts[ord(data.iloc[i, 1][k]) - 65]["DU"]
# ----------------------------------------
for j in range(len(graph)):
    print(atts[j])
print()
# ------------------------------------------------
G2 = nx.DiGraph()

for i in range(len(graph)):
    for j in graph[i]:
        G2.add_edge(chr(i+65), chr(j+65))
temp = []
for i in range(len(atts)):
    temp.append(atts[i]["Name"])
temp = dict(zip(temp, atts))
nx.set_node_attributes(G2, temp)
fig, ax = plt.subplots(figsize=(12, 12))
pos = nx.nx_agraph.graphviz_layout(G2, prog='dot')
#nx.draw(G2, pos=pos, ax=ax, with_labels=True, font_weight='bold')
nx.draw_networkx_edges(G2, pos, edge_color='olive',
                       width=1, arrowstyle='simple', arrowsize=20, min_source_margin=25, min_target_margin=25)
crt = []
notcrt = []
for i in atts:
    if(i["LF"] == i["EF"]):
        crt.append(i["Name"])
    else:
        notcrt.append(i["Name"])
nx.draw_networkx_nodes(G2, pos, node_size=1000,
                       node_color='seagreen', ax=ax, nodelist=crt)
nx.draw_networkx_nodes(G2, pos, node_size=1000,
                       node_color='wheat', ax=ax, nodelist=notcrt)
nx.draw_networkx_labels(G2, pos, ax=ax, font_weight="bold",
                        font_color="w", font_size=16)

for node in G2.nodes:
    xy = pos[node]
    node_attr = G2.nodes[node]
    text = '\n'.join(f'{k}: {v}' for k, v in G2.nodes[node].items())
    ax.annotate(text, xy=xy, xytext=(80, 5), textcoords="offset points",
                bbox=dict(boxstyle="round", fc="lightgrey"),
                arrowprops=dict(arrowstyle="wedge"))
plt.show()
