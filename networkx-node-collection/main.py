import networkx as nx
import matplotlib.pyplot as plt
import pyodbc

#COM1 Basement
# G = nx.DiGraph()

# G.add_node("B-01") #Tech HangOut
# G.add_node("B-02") #Data Comms & Networking Lab/Parallel and Distributed Computing Lab
# G.add_node("B-03") #Active Learning Lab
# G.add_node("B-04") #Technical Room 2
# G.add_node("B-05") #Technical Room 1
# G.add_node("B-06") #DR 4
# G.add_node("B-07") #DR 3
# G.add_node("B-08") #Programming Lab 3
# G.add_node("B-09") #Programming Lab 2
# G.add_node("B-10") #Progrmaming Lab 5
# G.add_node("B-11") #Programming Lab 4
# G.add_node("B-12") #Programming Lab 1
# G.add_node("B-13") #IT Security & OS Lab
# G.add_node("B-14A") #DR 2
# G.add_node("B-14B") #DR 1
# G.add_node("Staircase 1") #Staircase outside DR 2
# G.add_node("Staircase 2") #Staircase outside Active Learning Lab
# G.add_node("C1") #As depicted in Diagram
# G.add_node("C2") #As depicted in Diagram
# G.add_node("C3") #As depicted in Diagram
# G.add_node("C4") #As depicted in Diagram
# G.add_node("C5") #As depicted in Diagram
# G.add_node("C6") #As depicted in Diagram
# G.add_node("C7") #As depicted in Diagram


G = nx.Graph()

G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")

G.add_edge("1", "2", path="Do nothing", image="https://imgur.com/rKnqDmn")
G.add_edge("2", "3", path="Continue Straight", image="https://imgur.com/rKnqDmn")
G.add_edge("1", "3", path="Turn Left", image="https://imgur.com/rKnqDmn")
G.add_edge("3", "4", path="Turn Left", image="https://imgur.com/rKnqDmn")

for u, v, data in G.edges(data=True):
    path = data['path']
    image_data = data['image']
    print(f"Edge from {u} to {v}: Path = {path}, Image = {image_data}")

server = 'orbital.database.windows.net'
database = 'SoC_Buildings'
username = 'orbital@orbital'
password = 'Chonkypikachu2024!'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()
edge_len = G.number_of_edges()
for u, v, data in G.edges(data=True):
    path = data['path']
    image_data = data['image']
    cursor.execute(
        "INSERT INTO Nodes (FromNodeID, ToNodeID, PathDescription, Image) VALUES(?, ?, ?, ?)",
        u, v, path, image_data
    )
conn.commit()
cursor.close()
conn.close()
print("successful commit")


# graph_data = {
#     "nodes": [{"id": n, "path": G.nodes[n]['path']} for n in G.nodes],
#     "edges": [{"source": u, "target": v, "image": G[u][v]['image']} for u, v in G.edges],
#     "shortest_path": shortest_path
# }

# with open('graph_data.json', 'w') as f:
#     json.dump(graph_data, f, indent=4)

# #C1
# G.add_edge("B-01", "C1", path="turn right", image=NotDoneYet)
# G.add_edge("B-02", "C1")
# G.add_edge("B-03", "C1")
# G.add_edge("B-04", "C1")
# G.add_edge("B-05", "C1")
# G.add_edge("B-08", "C1") 
# #Reverse C1
# G.add_edge("C1", "B-01")
# G.add_edge("C1", "B-02")
# G.add_edge("C1", "B-03")
# G.add_edge("C1", "B-04")
# G.add_edge("C1", "B-05")
# G.add_edge("C1", "B-08") 
# #C2
# G.add_edge("B-06", "C2") 
# #Reverse C2
# G.add_edge("C2", "B-06") 
# #C3
# G.add_edge("B-07", "C3")
# G.add_edge("B-08", "C3")
# G.add_edge("B-09", "C3")
# G.add_edge("B-10", "C3")
# #Reverse C3
# G.add_edge("C3", "B-07")
# G.add_edge("C3", "B-08")
# G.add_edge("C3", "B-09")
# G.add_edge("C3", "B-10")
# #C4
# G.add_edge("B-09", "C4")
# G.add_edge("B-10", "C4")
# #Reverse C4
# G.add_edge("C4", "B-09")
# G.add_edge("C4", "B-10")
# #C5
# G.add_edge("B-11", "C5")
# G.add_edge("B-12", "C5")
# #Reverse C5
# G.add_edge("C5", "B-11")
# G.add_edge("C5", "B-12")
# #C6
# G.add_edge("B-11", "C6")
# G.add_edge("B-12", "C6")
# G.add_edge("B-13", "C6")
# #Reverse C6
# G.add_edge("C6", "B-11")
# G.add_edge("C6", "B-12")
# G.add_edge("C6", "B-13")
# #C7
# G.add_edge("B-14A", "C7")
# G.add_edge("B-14B", "C7")
# #Reverse C7
# G.add_edge("C7", "B-14A")
# G.add_edge("C7", "B-14B")
# #Corridor Link
# G.add_edge("C1", "C3")
# G.add_edge("C3", "C2")
# G.add_edge("C1", "C4")
# G.add_edge("C1", "C6")
# G.add_edge("C4", "C5")
# G.add_edge("C6", "C7")
# #Reverse Corridor Link
# G.add_edge("C3", "C1")
# G.add_edge("C2", "C3")
# G.add_edge("C4", "C1")
# G.add_edge("C6", "C1")
# G.add_edge("C5", "C4")
# G.add_edge("C7", "C6")
# #Staircase Link
# G.add_edge("C1", "Staircase 2") 
# G.add_edge("C6", "Staircase 1")
# #Reverse Staircase Link
# G.add_edge("Staircase 2", "C1")
# G.add_edge("Staircase 1", "C6") 



# nx.set_edge_attributes(G, attributes)
#draw out the graph
# nx.draw_planar(G, with_labels=True)
#calculate shortest path
# shortest_path = nx.shortest_path(G, source="B-08", target="B-12")
# print("Shortest path:", shortest_path)
# #collect the values
# shortest_path_attributes = []
# lengs = len(shortest_path)
# for i in range(lengs - 1):
#     x = shortest_path[i]
#     y = shortest_path[i + 1]
#     shortest_path_attributes.append(G[x][y]['path'])
#     # shortest_path_attributes.append(G[x][y]['image'])
# print("Path of nodes in the shortest path:", shortest_path_attributes)
# plt.show() 


