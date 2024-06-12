import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node("B-01") #Tech HangOut
G.add_node("B-02") #Data Comms & Networking Lab/Parallel and Distributed Computing Lab
G.add_node("B-03") #Active Learning Lab
G.add_node("B-04") #Technical Room 2
G.add_node("B-05") #Technical Room 1
G.add_node("B-06") #DR 4
G.add_node("B-07") #DR 3
G.add_node("B-08") #Programming Lab 3
G.add_node("B-09") #Programming Lab 2
G.add_node("B-10") #Progrmaming Lab 5
G.add_node("B-11") #Programming Lab 4
G.add_node("B-12") #Programming Lab 1
G.add_node("B-13") #IT Security & OS Lab
G.add_node("B-14A") #DR 2
G.add_node("B-14B") #DR 1
G.add_node("Staircase 1") #Staircase outside DR 2
G.add_node("Staircase 2") #Staircase outside Active Learning Lab
G.add_node("C1") #As depicted in Diagram
G.add_node("C2") #As depicted in Diagram
G.add_node("C3") #As depicted in Diagram
G.add_node("C4") #As depicted in Diagram
G.add_node("C5") #As depicted in Diagram
G.add_node("C6") #As depicted in Diagram
G.add_node("C7") #As depicted in Diagram

edges_list = [("B-01", "C1"), ("B-02", "C1"), ("B-03", "C1"), ("B-04", "C1"), ("B-05", "C1"), ("B-08", "C1"), #C1
              ("C1", "B-01"), ("C1", "B-02"), ("C1", "B-03"), ("C1", "B-04"), ("C1", "B-05"), ("C1", "B-08"), #Reverse C1
              ("B-06", "C2"), #C2
              ("C2", "B-06"), #Reverse C2
              ("B-07", "C3"), ("B-08", "C3"), ("B-09", "C3"), ("B-10", "C3"), #C3
              ("C3", "B-07"), ("C3", "B-08"), ("C3", "B-09"), ("C3", "B-10"), #Reverse C3
              ("B-09", "C4"), ("B-10", "C4"), #C4
              ("C4", "B-09"), ("C4", "B-10"), #Reverse C4
              ("B-11", "C5"), ("B-12", "C5"), #C5
              ("C5", "B-11"), ("C5", "B-12"), #Reverse C5
              ("B-11", "C6"), ("B-12", "C6"), ("B-13", "C6"), #C6
              ("C6", "B-11"), ("C6", "B-12"), ("C6", "B-13"), #Reverse C6
              ("B-14A", "C7"), ("B-14B", "C7"), #C7
              ("C7", "B-14A"), ("C7", "B-14B"), #Reverse C7
              ("C1", "C3"), ("C3", "C2"), ("C1", "C4"), ("C1", "C6"), ("C4", "C5"), ("C6", "C7"), #Corridor Link
              ("C3", "C1"), ("C2", "C3"), ("C4", "C1"), ("C6", "C1"), ("C5", "C4"), ("C7", "C6"), #Reverse Corridor Link
              ("C1", "Staircase 2"), ("C6", "Staircase 1"), #Staircase Link
              ("Staircase 2", "C1"), ("Staircase 1", "C6")] #Reverse Staircase Link
G.add_edges_from(edges_list)

attributes = {
    ("B-01", "C1"): {'path': 'test'}, ("B-02", "C1"): {'path': 'test'}, ("B-03", "C1"): {'path': 'test'}, #C1
    ("B-04", "C1"): {'path': 'test'}, ("B-05", "C1"): {'path': 'test'}, ("B-08", "C1"): {'path': 'test'}, #C1
              ("C1", "B-01"): {'path': 'test'}, ("C1", "B-02"): {'path': 'test'}, ("C1", "B-03"): {'path': 'test'}, #Reverse C1
                ("C1", "B-04"): {'path': 'test'}, ("C1", "B-05"): {'path': 'test'}, ("C1", "B-08"): {'path': 'test'}, #Reverse C1
              ("B-06", "C2"): {'path': 'test'}, #C2
              ("C2", "B-06"): {'path': 'test'}, #Reverse C2
              ("B-07", "C3"): {'path': 'test'}, ("B-08", "C3"): {'path': 'test'}, #C3
              ("B-09", "C3"): {'path': 'test'}, ("B-10", "C3"): {'path': 'test'}, #C3
              ("C3", "B-07"): {'path': 'test'}, ("C3", "B-08"): {'path': 'test'},
                ("C3", "B-09"): {'path': 'test'}, ("C3", "B-10"): {'path': 'test'}, #Reverse C3
              ("B-09", "C4"): {'path': 'test'}, ("B-10", "C4"): {'path': 'test'}, #C4
              ("C4", "B-09"): {'path': 'test'}, ("C4", "B-10"): {'path': 'test'}, #Reverse C4
              ("B-11", "C5"): {'path': 'test'}, ("B-12", "C5"): {'path': 'test'}, #C5
              ("C5", "B-11"): {'path': 'test'}, ("C5", "B-12"): {'path': 'test'}, #Reverse C5
              ("B-11", "C6"): {'path': 'test'}, ("B-12", "C6"): {'path': 'test'}, ("B-13", "C6"): {'path': 'test'}, #C6
              ("C6", "B-11"): {'path': 'test'}, ("C6", "B-12"): {'path': 'test'}, ("C6", "B-13"): {'path': 'test'}, #Reverse C6
              ("B-14A", "C7"): {'path': 'test'}, ("B-14B", "C7"): {'path': 'test'}, #C7
              ("C7", "B-14A"): {'path': 'test'}, ("C7", "B-14B"): {'path': 'test'}, #Reverse C7
              ("C1", "C3"): {'path': 'test', 'image': "./pikachu.png"}, ("C3", "C2"): {'path': 'test', 'image': "./pikachu.png"}, ("C1", "C4"): {'path': 'test', 'image': "./pikachu.png"}, #Corridor Link
                ("C1", "C6"): {'path': 'test', 'image': "./pikachu.png"}, ("C4", "C5"): {'path': 'test', 'image': "./pikachu.png"}, ("C6", "C7"): {'path': 'test', 'image': "./pikachu.png"}, #Corridor Link
              ("C3", "C1"): {'path': 'test', 'image': "./pikachu.png"}, ("C2", "C3"): {'path': 'test', 'image': "./pikachu.png"}, ("C4", "C1"): {'path': 'test', 'image': "./pikachu.png"}, #Reverse Corridor Link
                ("C6", "C1"): {'path': 'test', 'image': "./pikachu.png"}, ("C5", "C4"): {'path': 'test', 'image': "./pikachu.png"}, ("C7", "C6"): {'path': 'test', 'image': "./pikachu.png"}, #Reverse Corridor Link
              ("C1", "Staircase 2"): {'path': 'test', 'image': "./pikachu.png"}, ("C6", "Staircase 1"): {'path': 'test', 'image': "./pikachu.png"}, #Staircase Link
              ("Staircase 2", "C1"): {'path': 'test', 'image': "./pikachu.png"}, ("Staircase 1", "C6"): {'path': 'test', 'image': "./pikachu.png"} #Reverse Staircase Link
}
nx.set_edge_attributes(G, attributes)
nx.draw_planar(G, with_labels=True)
shortest_path = nx.shortest_path(G, source="B-01", target="B-14A")
print("Shortest path:", shortest_path)
shortest_path_attributes = []
len = len(shortest_path)
for i in range(len - 1):
    x = shortest_path[i]
    y = shortest_path[i + 1]
    shortest_path_attributes.append(G[x][y]['path'])
print("Path of nodes in the shortest path:", shortest_path_attributes)
plt.show() 


