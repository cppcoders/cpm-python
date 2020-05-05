# Critical Path Method
The critical path method, or critical path analysis, is an algorithm for scheduling a set of project activities. It is commonly used in conjunction with the program evaluation and review technique.
-----------------------------------------------------------------------
This is a python program that 
* takes an activity table with each activity's predecessors and duration and stores it into a graph
* using a modified Breadth First Search algorithm to traverse the graph and determine the correct path
* calculates number of attributes for each activity following the selected path, these attributes are :
  * DU = Activity Duration
  * ES = Early Start Time
  * EF = Early Finish Time
  * LS = Late Start Time
  * LF = Late Finish Time
* draws a plot showing the the graph, attributes for each node and critical path (green nodes),
-----------------------------------------------------------------------
Here is Some Sample Tests And It's Output
---------------------
Activity|Predecessors|Duration
--------|------------|--------
A|-|3
B|A|4
C|A|2
D|B|5
E|C|1
F|C|2
G|D E|4
H|F G|3

![fig3](/images/fig3.png)
---------------------
Activity|Predecessors|Duration
--------|------------|--------
A|-|3
B|A|60
C|A|5
D|A|15
E|B|6
F|D|40
G|C E|10
H|F|7
I|G|6
J|H I|12

![fig4](/images/fig4.png)
---------------------
Activity|Predecessors|Duration
--------|------------|--------
A|-|7
B|A|7
C|B|14
D|A|14
E|D|14
F|D|14
G|E|21
H|F|7
I|G|7
J|C H|1
K|E|7
L|E|7
M|L|7
N|I J K M|7

![fig5](/images/fig5.png)
---------------------
Activity|Predecessors|Duration
--------|------------|--------
A|-|2
B|A|4
C|B|3
D|B|2
E|C D|10
F|B|4

![fig6](/images/fig6.png)
-------------------------------------
Used Tools:
* Python -obviously-
* Pandas: to import the data from csv files and store it in adjacency list for the graph
* Networkx: to make the graph, nodes, edges, colors, arrows and everything
* Graphviz: to calculate the positions for the graph nodes by "dot" engine
* Matplotlib: to draw all these stuff
