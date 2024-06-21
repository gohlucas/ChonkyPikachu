import networkx as nx
import matplotlib.pyplot as plt

#Venv installed networkx, matplotlib, pyodbc, flask
G = nx.DiGraph()

G.add_node("01-07") #Database 3 Electronic Commerce & Database
G.add_node("01-08-1") #Database 1 Opposite Database 2
G.add_node("01-08-2") #Database 1 Opposite E&A Cluster 4
G.add_node("01-09-1") #E&A Cluster 4 Opposite Database 1
G.add_node("01-09-2") #E&A Cluster 4 Opposite Database 2
G.add_node("01-10") #E&A Cluster 2
G.add_node("01-11-1") #Database 2 Opposite Database 1
G.add_node("01-11-2") #Database 2 Opposite AHU
G.add_node("01-12-1") #Artificial Intelligence 1: Adaptive Computing Opposite Database 3
G.add_node("01-12-2") #Artificial Intelligence 1: Adaptive Computing Beside Wire Center
G.add_node("01-13-1") #Embedded Systems Teaching Lab 2 Opposite Database 3
G.add_node("01-13-2") #Embedded Systems Teaching Lab 2 Opposite Computational Biology 1
G.add_node("01-14-1") #Embedded Systems Teaching Lab 1 Opposite Database 3
G.add_node("01-14-2") #Embedded Systems Teaching Lab 1 Opposite MR 4
G.add_node("01-15") #Computational Biology 2
G.add_node("01-16") #E&A Cluster 1
G.add_node("01-18") #MR 5
G.add_node("01-19") #E&A Cluster 2
G.add_node("01-20-1") #Programming Lab 6 Opposite Wire Center
G.add_node("01-20-2") #Programming Lab 6 Beside Computational Biology 1
G.add_node("01-21-1") #Computational Biology 1 Opposite MR 4
G.add_node("01-21-2") #Computational Biology 1 Opposite AHU
G.add_node("01-22") #MR 4
G.add_node("01-23") #Career Consultation Room
G.add_node("01-24") #Robot Living Studio
G.add_node("Staircase 1") #Near Robot Living Studio
G.add_node("Staircase 2") #Near Computational Biology 1
G.add_node("Staircase 3") #Near E&A Cluster 4
G.add_node("Staircase 4") #Beside Lift Lobby
G.add_node("01-C1") #As depicted in Diagram
G.add_node("01-C2") #As depicted in Diagram
G.add_node("01-C3") #As depicted in Diagram
G.add_node("01-C4") #As depicted in Diagram
G.add_node("01-C5") #As depicted in Diagram
G.add_node("01-C6") #As depicted in Diagram
G.add_node("01-C7") #As depicted in Diagram
G.add_node("01-C8") #As depicted in Diagram
G.add_node("01-C9") #As depicted in Diagram
G.add_node("01-C10") #As depicted in Diagram
G.add_node("01-C11") #As depicted in Diagram
G.add_node("01-C12") #As depicted in Diagram
G.add_node("01-C13") #As depicted in Diagram
G.add_node("01-C14") #As depicted in Diagram

#Room to Corridor
G.add_edge("01-07", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-08-1", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-11-1", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-12-1", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-13-1", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-14-1", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-15", "01-C1", path="Walk til you see the corridor on the next page")
G.add_edge("01-08-2", "01-C2", path="Walk til you see the corridor on the next page")
G.add_edge("01-09-1", "01-C2", path="Walk til you see the corridor on the next page")
G.add_edge("01-09-2", "01-C3", path="Walk til you see the corridor on the next page")
G.add_edge("01-10", "01-C3", path="Walk til you see the corridor on the next page")
G.add_edge("01-18", "01-C4", path="Walk til you see the corridor on the next page")
G.add_edge("01-19", "01-C5", path="Walk til you see the corridor on the next page")
G.add_edge("01-11-2", "01-C6", path="Walk til you see the corridor on the next page")
G.add_edge("01-12-2", "01-C7", path="Walk til you see the corridor on the next page")
G.add_edge("01-13-2", "01-C8", path="Walk til you see the corridor on the next page")
G.add_edge("01-20-1", "01-C8", path="Walk til you see the corridor on the next page")
G.add_edge("01-21-1", "01-C9", path="Walk til you see the corridor on the next page")
G.add_edge("01-22", "01-C9", path="Walk til you see the corridor on the next page")
G.add_edge("01-20-2", "01-C11", path="Walk til you see the corridor on the next page")
G.add_edge("01-21-2", "01-C11", path="Walk til you see the corridor on the next page")
G.add_edge("01-14-2", "01-C12", path="Walk til you see the corridor on the next page")
G.add_edge("01-16", "01-C12", path="Walk til you see the corridor on the next page")
G.add_edge("01-23", "01-C13", path="Walk til you see the corridor on the next page")
G.add_edge("01-24", "01-C14", path="Walk til you see the corridor on the next page")

#Corridor to Room
G.add_edge("01-C1", "01-07", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-08-1", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-11-1", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-12-1", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-13-1", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-14-1", path="Your destination is along this corridor")
G.add_edge("01-C1", "01-15", path="Your destination is along this corridor")
G.add_edge("01-C2", "01-08-2", path="Your destination is along this corridor")
G.add_edge("01-C2", "01-09-1", path="Your destination is along this corridor")
G.add_edge("01-C3", "01-09-2", path="Your destination is along this corridor")
G.add_edge("01-C3", "01-10", path="Your destination is along this corridor")
G.add_edge("01-C4", "01-18", path="Your destination is along this corridor")
G.add_edge("01-C5", "01-19", path="Your destination is along this corridor")
G.add_edge("01-C6", "01-11-2", path="Your destination is along this corridor")
G.add_edge("01-C7", "01-12-2", path="Your destination is along this corridor")
G.add_edge("01-C8", "01-13-2", path="Your destination is along this corridor")
G.add_edge("01-C8", "01-20-1", path="Your destination is along this corridor")
G.add_edge("01-C9", "01-21-1", path="Your destination is along this corridor")
G.add_edge("01-C9", "01-22", path="Your destination is along this corridor")
G.add_edge("01-C11", "01-20-2", path="Your destination is along this corridor")
G.add_edge("01-C11", "01-21-2", path="Your destination is along this corridor")
G.add_edge("01-C12", "01-14-2", path="Your destination is along this corridor")
G.add_edge("01-C12", "01-16", path="Your destination is along this corridor")
G.add_edge("01-C13", "01-23", path="Your destination is along this corridor")
G.add_edge("01-C14", "01-24", path="Your destination is along this corridor")

#Corridor Link
G.add_edge("01-C1", "01-C3", path="Turn right")
G.add_edge("01-C1", "01-C14", path="Turn left")
G.add_edge("01-C2", "01-C3", path="Turn right")
G.add_edge("01-C2", "01-C1", path="Head straight")
G.add_edge("01-C3", "01-C4", path="Head straight")
G.add_edge("01-C3", "01-C6", path="Turn right")
G.add_edge("01-C4", "01-C5", path="Turn left")
G.add_edge("01-C4", "01-C6", path="Turn left")
G.add_edge("01-C6", "01-C7", path="Turn right")
G.add_edge("01-C6", "01-C8", path="Head straight")
G.add_edge("01-C7", "01-C8", path="Turn right")
G.add_edge("01-C8", "01-C9", path="Turn left")
G.add_edge("01-C8", "01-C12", path="Head straight")
G.add_edge("01-C9", "01-C10", path="Turn left")
G.add_edge("01-C9", "01-C12", path="Turn left")
G.add_edge("01-C10", "01-C11", path="Turn left")
G.add_edge("01-C12", "01-C13", path="Turn left")
G.add_edge("01-C12", "01-C14", path="Turn right")
G.add_edge("01-C13", "01-C14", path="Head straight")

#Reverse Corridor Link
G.add_edge("01-C3", "01-C1", path="Turn left")
G.add_edge("01-C14", "01-C1", path="Turn right")
G.add_edge("01-C3", "01-C2", path="Turn right")
G.add_edge("01-C1", "01-C2", path="Head straight")
G.add_edge("01-C4", "01-C3", path="Head straight")
G.add_edge("01-C6", "01-C3", path="Turn left")
G.add_edge("01-C5", "01-C4", path="Turn right")
G.add_edge("01-C6", "01-C4", path="Turn right")
G.add_edge("01-C7", "01-C6", path="Turn left")
G.add_edge("01-C8", "01-C6", path="Head straight")
G.add_edge("01-C8", "01-C7", path="Turn left")
G.add_edge("01-C9", "01-C8", path="Turn right")
G.add_edge("01-C12", "01-C8", path="Head straight")
G.add_edge("01-C10", "01-C9", path="Turn right")
G.add_edge("01-C12", "01-C9", path="Turn right")
G.add_edge("01-C11", "01-C10", path="Turn right")
G.add_edge("01-C13", "01-C12", path="Turn right")
G.add_edge("01-C14", "01-C12", path="Turn left")
G.add_edge("01-C14", "01-C13", path="Head straight")

#Staircase Link
G.add_edge("01-C1", "Staircase 1", path="Head straight, head down the staircase on the right")
G.add_edge("01-C14", "Staircase 1", path="Turn left, head down the staircase on the right")
G.add_edge("01-C9", "Staircase 2", path="Head straight, the staircase is on the right")
G.add_edge("01-C10", "Staircase 2", path="Head straight, the staircase is straight ahead")
G.add_edge("01-C2", "Staircase 3", path="Head straight, head down the staircase on the left")
G.add_edge("01-C13", "Staircase 4", path="Exit to the lobby, the staircase is on the left")

#Reverse Staircase Link
G.add_edge("Staircase 1", "01-C1", path="Turn left and head straight")
G.add_edge("Staircase 1", "01-C14", path="Turn left and turn right at the junction")
G.add_edge("Staircase 2", "01-C9", path="Head straight and turn left")
G.add_edge("Staircase 2", "01-C10", path="Head straight")
G.add_edge("Staircase 3", "01-C2", path="Turn right")
G.add_edge("Staircase 4", "01-C13", path="Turn Left and head through the door")

# #Room to Room
G.add_edge("01-07", "01-08-1", path="Turn left, the room is on the left")
G.add_edge("01-07", "01-11-1", path="Turn left and walk straight, the room is on the right")
G.add_edge("01-07", "01-12-1", path="The room is directly opposite")
G.add_edge("01-07", "01-13-1", path="The room is directly opposite")
G.add_edge("01-07", "01-14-1", path="The room is directly opposite")
G.add_edge("01-07", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-08-1", "01-07", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-08-1", "01-11-1", path="The room is directly opposite")
G.add_edge("01-08-1", "01-12-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-08-1", "01-13-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-08-1", "01-14-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-08-1", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-11-1", "01-07", path="Turn left and walk straight, the room is on the right")
G.add_edge("01-11-1", "01-08-1", path="The room is directly opposite")
G.add_edge("01-11-1", "01-12-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-11-1", "01-13-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-11-1", "01-14-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-11-1", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-12-1", "01-07", path="The room is directly opposite")
G.add_edge("01-12-1", "01-08-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-12-1", "01-11-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-12-1", "01-13-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-12-1", "01-14-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-12-1", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-13-1", "01-07", path="The room is directly opposite")
G.add_edge("01-13-1", "01-08-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-13-1", "01-11-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-13-1", "01-12-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-13-1", "01-14-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-13-1", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-14-1", "01-07", path="The room is directly opposite")
G.add_edge("01-14-1", "01-08-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-14-1", "01-11-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-14-1", "01-12-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-14-1", "01-13-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-14-1", "01-15", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-15", "01-07", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-15", "01-08-1", path="Turn right and walk straight, the room is on the left")
G.add_edge("01-15", "01-11-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-15", "01-12-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-15", "01-13-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-15", "01-14-1", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-08-2", "01-09-1", path="The room is directly opposite")
G.add_edge("01-09-1", "01-08-2", path="The room is directly opposite")
G.add_edge("01-09-2", "01-10", path="Turn left and walk straight, the room is on the left")
G.add_edge("01-10", "01-09-2", path="Turn right and walk straight, the room is on the right")
G.add_edge("01-13-2", "01-20-1", path="Turn left and walk straight, the room is on the right")
G.add_edge("01-20-1", "01-13-2", path="Turn left and walk straight, the room is on the right")
G.add_edge("01-21-1", "01-22", path="The room is directly opposite")
G.add_edge("01-22", "01-21-1", path="The room is directly opposite")
G.add_edge("01-20-2", "01-21-2", path="Walk straight, the room is on the right")
G.add_edge("01-21-2", "01-20-2", path="Walk straight, the room is on the right")
G.add_edge("01-14-2", "01-16", path="Turn left and walk straight, the room is on the right")
G.add_edge("01-16", "01-14-2", path="Turn right and walk straight, the room is on the left")

nx.draw(G, with_labels=True)

#Testing
shortest_path = nx.shortest_path(G, source="01-11-1", target="01-20-2")
print("Shortest path:", shortest_path)
shortest_path_attributes = []
for i in range(len(shortest_path) - 1):
    x = shortest_path[i]
    y = shortest_path[i + 1]
    shortest_path_attributes.append(G[x][y]['path'])
    # shortest_path_attributes.append(G[x][y]['image'])
print("Path of nodes in the shortest path:", shortest_path_attributes)


# plt.show() 
