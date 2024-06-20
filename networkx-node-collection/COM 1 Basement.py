import networkx as nx
import matplotlib.pyplot as plt
import pyodbc

# COM1 Basement
G = nx.DiGraph()

G.add_node("B-01-1") #Tech HangOut Opposite Programming Lab 3
G.add_node("B-01-2") #Tech HangOut Opposite Technical room 1
G.add_node("B-02") #Data Comms & Networking Lab/Parallel and Distributed Computing Lab
G.add_node("B-03") #Active Learning Lab
G.add_node("B-04") #Technical Room 2
G.add_node("B-05") #Technical Room 1
G.add_node("B-06") #Dr 4
G.add_node("B-07") #Dr 3
G.add_node("B-08-1") #Programming Lab 3 Beside lift
G.add_node("B-08-2") #Programming Lab 3 Opposite Technical room 1
G.add_node("B-09-1") #Programming Lab 2 Opposite Programming lab 4
G.add_node("B-09-2") #Programming Lab 2 Opposite Dr 3
G.add_node("B-10-1") #Progrmaming Lab 5 Beside Store room 1
G.add_node("B-10-2") #Progrmaming Lab 5 Opposite AHU
G.add_node("B-11-1") #Programming Lab Beside Common Area
G.add_node("B-11-2") #Programming Lab Opposite Store room 1
G.add_node("B-12-1") #Programming Lab 1 Beside Staircase
G.add_node("B-12-2") #Programming Lab 1 Beside Store room 2
G.add_node("B-13") #IT Security & OS Lab
G.add_node("B-14A") #Dr 2
G.add_node("B-14B") #Dr 1
G.add_node("Staircase 1") #Staircase outside Dr 2
G.add_node("Staircase 2") #Staircase outside Active learning lab
G.add_node("C1") #As depicted in Diagram
G.add_node("C2") #As depicted in Diagram
G.add_node("C3") #As depicted in Diagram
G.add_node("C4") #As depicted in Diagram
G.add_node("C5") #As depicted in Diagram
G.add_node("C6") #As depicted in Diagram
G.add_node("C7") #As depicted in Diagram
G.add_node("C8") #As depicted in Diagram

# G.add_edge("1", "2", path="Do nothing", image="https://imgur.com/rKnqDmn")

# server = 'orbital.database.windows.net'
# database = 'SoC_Buildings'
# username = 'orbital@orbital'
# password = 'Chonkypikachu2024!'
# driver = '{ODBC Driver 17 for SQl Server}'

# conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
# cursor = conn.cursor()
# edge_len = G.number_of_edges()
# for u, v, data in G.edges(data=True):
#     path = data['path']
#     image_data = data['image']
#     cursor.execute(
#         "INSERT INTO Nodes (FromNodeID, ToNodeID, PathDescription, Image) VAlUES(?, ?, ?, ?)",
#         u, v, path, image_data
#     )
# conn.commit()
# cursor.close()
# conn.close()
# print("successful commit")


# graph_data = {
#     "nodes": [{"id": n, "path": G.nodes[n]['path']} for n in G.nodes],
#     "edges": [{"source": u, "target": v, "image": G[u][v]['image']} for u, v in G.edges],
#     "shortest_path": shortest_path
# }

#Room to Corridor
G.add_edge("B-01-2", "C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-02", "C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-03", "C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-04", "C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-05", "C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-06", "C2", path="Walk til you see the corridor on the next page") 
G.add_edge("B-07", "C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-08-2", "C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-09-2", "C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-10-2", "C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-09-1", "C4", path="Walk til you see the corridor on the next page")
G.add_edge("B-10-1", "C4", path="Walk til you see the corridor on the next page")
G.add_edge("B-11-2", "C5", path="Walk til you see the corridor on the next page")
G.add_edge("B-12-2", "C5", path="Walk til you see the corridor on the next page")
G.add_edge("B-11-1", "C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-12-1", "C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-13", "C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-14A", "C7", path="Walk til you see the corridor on the next page")
G.add_edge("B-14B", "C7", path="Walk til you see the corridor on the next page")
G.add_edge("B-01-1", "C8", path="Walk til you see the corridor on the next page")
G.add_edge("B-08-1", "C8", path="Walk til you see the corridor on the next page") 

#Corridor to room
G.add_edge("C1", "B-01-2", path="Your destination is along this corridor")
G.add_edge("C1", "B-02", path="Your destination is along this corridor")
G.add_edge("C1", "B-03", path="Your destination is along this corridor")
G.add_edge("C1", "B-04", path="Your destination is along this corridor")
G.add_edge("C1", "B-05", path="Your destination is along this corridor")
G.add_edge("C2", "B-06", path="Your destination is along this corridor") 
G.add_edge("C3", "B-07", path="Your destination is along this corridor")
G.add_edge("C3", "B-08-2", path="Your destination is along this corridor")
G.add_edge("C3", "B-09-2", path="Your destination is along this corridor")
G.add_edge("C3", "B-10-2", path="Your destination is along this corridor")
G.add_edge("C4", "B-09-1", path="Your destination is along this corridor")
G.add_edge("C4", "B-10-1", path="Your destination is along this corridor")
G.add_edge("C5", "B-11-2", path="Your destination is along this corridor")
G.add_edge("C5", "B-12-2", path="Your destination is along this corridor")
G.add_edge("C6", "B-11-1", path="Your destination is along this corridor")
G.add_edge("C6", "B-12-1", path="Your destination is along this corridor")
G.add_edge("C6", "B-13", path="Your destination is along this corridor")
G.add_edge("C7", "B-14A", path="Your destination is along this corridor")
G.add_edge("C7", "B-14B", path="Your destination is along this corridor")
G.add_edge("C8", "B-01-1", path="Your destination is along this corridor")
G.add_edge("C8", "B-08-1", path="Your destination is along this corridor") 

#Corridor link
G.add_edge("C1", "C3", path="Turn left")
G.add_edge("C3", "C2", path="Turn here") #To take photo
G.add_edge("C1", "C8", path="Head straight")
G.add_edge("C8", "C4", path="Turn right")
G.add_edge("C8", "C6", path="Head straight")
G.add_edge("C4", "C5", path="Turn right")
G.add_edge("C6", "C7", path = "Turn right")

#Reverse Corridor link
G.add_edge("C3", "C1", path="Turn right")
G.add_edge("C2", "C3", path="Head straight")
G.add_edge("C8", "C1", path="Head straight")
G.add_edge("C4", "C8", path="Turn right")
G.add_edge("C6", "C8", path="Head straight")
G.add_edge("C5", "C4", path="Turn left")
G.add_edge("C7", "C6", path="Turn left")

#Staircase link
G.add_edge("C1", "Staircase 2", path="Turn left") 
G.add_edge("C6", "Staircase 1", path="Turn right")

#Reverse Staircase link
G.add_edge("Staircase 2", "C1", path="Turn right")
G.add_edge("Staircase 1", "C6", path="Turn left") 

#Room to Room
G.add_edge("B-01-2", "B-02", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-01-2", "B-03", path="Turn left and walk straight, the room is on the right")
G.add_edge("B-01-2", "B-04", path="Turn left and walk straight, the room is on the right")
G.add_edge("B-01-2", "B-05", path="It is the room directly opposite")
G.add_edge("B-02", "B-01-2", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-02", "B-03", path="It is the room directly opposite")
G.add_edge("B-02", "B-04", path="It is the room directly opposite")
G.add_edge("B-02", "B-05", path="Turn right and walk straight, the room is on the left")
G.add_edge("B-03", "B-01-2", path="Turn left and walk straight, the room is on the right")
G.add_edge("B-03", "B-02", path="It is the room directly opposite")
G.add_edge("B-03", "B-04", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-03", "B-05", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-04", "B-01-2", path="Turn left and walk straight, the room is on the right")
G.add_edge("B-04", "B-02", path="it is the room directly opposite")
G.add_edge("B-04", "B-03", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-04", "B-05", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-05", "B-01-2", path="It is the room directly opposite")
G.add_edge("B-05", "B-02", path="Turn right and walk straight, the room is on the left")
G.add_edge("B-05", "B-03", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-05", "B-04", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-08-2", "B-09-2", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-08-2", "B-10-2", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-09-2", "B-08-2", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-09-2", "B-10-2", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-10-2", "B-08-2", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-10-2", "B-09-2", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-09-1", "B-10-1", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-10-1", "B-09-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("B-11-2", "B-12-2", path="Turn right, the room is straight ahead")
G.add_edge("B-12-2", "B-11-2", path="Head straight, the room is on the left")
G.add_edge("B-11-1", "B-12-1", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-11-1", "B-13", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-12-1", "B-11-1", path="Turn right, the room is on the right")
G.add_edge("B-12-1", "B-13", path="Turn left and walk straight, the room is on the left")
G.add_edge("B-13", "B-11-1", path="Turn right, the room is on the right")
G.add_edge("B-13", "B-12-1", path="Turn right, the room is on the right")
G.add_edge("B-14A", "B-14B", path="Turn left, the room is straight ahead")
G.add_edge("B-14B", "B-14A", path="Walk straight, the room is on the right")


# nx.draw(G, with_labels=True)

#Testing
# shortest_path = nx.shortest_path(G, source="B-14A", target="B-12-2")
# print("Shortest path:", shortest_path)
# shortest_path_attributes = []
# for i in range(len(shortest_path) - 1):
#     x = shortest_path[i]
#     y = shortest_path[i + 1]
#     shortest_path_attributes.append(G[x][y]['path'])
#     # shortest_path_attributes.append(G[x][y]['image'])
# print("Path of nodes in the shortest path:", shortest_path_attributes)


# plt.show() 


