import numpy as np
import pandas as pd
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


def BFS(s, graph):
    visited = [False] * (len(graph))
    queue = []
    for i in s:
        queue.append(i)
        visited[i] = True
    while queue:
        s = queue.pop(0)
        print(str(chr(s+65)), end=' ')
        path.append(s)
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
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


print()
print("Path")
BFS(start, graph)
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
