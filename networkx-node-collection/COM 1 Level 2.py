import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Node adding 
G.add_node("02-01") # Seminar Room 5
G.add_node("02-02") # Computing Gallery
G.add_node("02-03") # Seminar Room 6
G.add_node("C1") # As depicted in the diagram
G.add_node("02-04") # Seminar Room 2
G.add_node("C2") # As depicted in the diagram
G.add_node("02-05") # Cerebro@SoC
G.add_node("C5") # As depicted in the diagram
G.add_node("02-06") # Seminar Room 1
G.add_node("C3") # As depicted in the diagram
G.add_node("C4") # As depicted in the diagram
G.add_node("02-07") # Seminar Room 7
G.add_node("02-08") # Seminar Room 8
G.add_node("02-09") # Seminar Room 9
G.add_node("02-10") # Seminar Room 10
G.add_node("C6") # As depicted in the diagram
# There is no 02-11
G.add_node("02-12") # Seminar Room 3
G.add_node("C7") # As depicted in the diagram
G.add_node("02-13") # VC Room 
G.add_node("02-14") # Tutorial Room 12
G.add_node("C9") # As depicted in the diagram
G.add_node("02-15") # ICPC Lab 
G.add_node("02-16") # Tutorial Room 11
G.add_node("02-17") # Tutorial Room 10
G.add_node("02-18") # Computing Club 
G.add_node("C8") # As depicted in the diagram
# 02-19 is Undergraduate Studies office, out of bounds
G.add_node("02-20") # Discussion Room 12
G.add_node("02-21") # Student's Lounge
G.add_node("Stair 4") 
G.add_node("Lift")

# Edge adding between corridor and room
G.add_edge("02-01","C1", path = "Walk straight till you see this corridor")
G.add_edge("02-02","C1", path = "Walk straight till you see this corridor")
G.add_edge("02-03","C1", path = "Walk straight till you see this corridor")
G.add_edge("02-04","C2", path = "")
G.add_edge("02-06","C3", path = "")
G.add_edge("02-06","C4", path = "")
G.add_edge("02-05","C5", path = "")
G.add_edge("02-07","C6", path = "")
G.add_edge("02-08","C6", path = "Walk straight till you see this corridor")
G.add_edge("02-09","C6", path = "Walk straight till you see this corridor")
G.add_edge("02-10","C6", path = "Walk straight till you see this corridor")
G.add_edge("02-12","C7", path = "")
G.add_edge("02-15","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-16","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-17","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-18","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-20","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-21","C8", path = "Walk straight till you see this corridor")
G.add_edge("02-14","C9", path = "")

# Reverse Edges between corridor and room 
G.add_edge("C1","02-01", path = "Walk straight, the room is on right")
G.add_edge("C1","02-02", path = "Walk straight, the room is on right")
G.add_edge("C1","02-03", path = "Walk straight, the room is on right")
G.add_edge("C2","02-04", path = "")
G.add_edge("C3","02-06", path = "")
G.add_edge("C4","02-06", path = "")
G.add_edge("C5","02-05", path = "")
G.add_edge("C6","02-07", path = "")
G.add_edge("C6","02-08", path = "Walk straight, the room is on left")
G.add_edge("C6","02-09", path = "Walk straight, the room is on left")
G.add_edge("C6","02-10", path = "Walk straight, the room is on left")
G.add_edge("C7","02-12", path = "")
G.add_edge("C8","02-15", path = "Walk straight, the room is on left")
G.add_edge("C8","02-16", path = "Walk straight, the room is on left")
G.add_edge("C8","02-17", path = "Walk straight, the room is on left")
G.add_edge("C8","02-18", path = "Walk straight, the room is on right")
G.add_edge("C8","02-20", path = "Walk straight, the room is on right")
G.add_edge("C8","02-21", path = "Walk straight, the room is on right")
G.add_edge("C9","02-14", path = "")

#Edge adding between corridors:
G.add_edge("C1","C2", path ="Turn Right")
G.add_edge("C1","C3", path ="Walk Straight")
G.add_edge("C2","C1", path ="Turn Left")
G.add_edge("C2","C3", path ="Turn Right")
G.add_edge("C2","C4", path ="Walk Straight")
G.add_edge("C2","C5", path ="Turn Right")
G.add_edge("C3","C1", path ="Walk Straight")
G.add_edge("C3","C2", path ="Turn Right")
G.add_edge("C3","C4", path ="Turn Left")
G.add_edge("C4","C3", path ="Turn Right")
G.add_edge("C4","C5", path ="Walk Straight")
G.add_edge("C4","C6", path ="Turn Left")
G.add_edge("C4","C7", path ="Walk Straight")
G.add_edge("C5","C4", path ="Walk Straight")
G.add_edge("C5","C7", path ="Turn Right")
G.add_edge("C5","C8", path ="Turn Right")
G.add_edge("C6","C7", path ="Turn Left")
G.add_edge("C6","C9", path ="Turn Right")
G.add_edge("C7","C4", path ="Walk Straight")
G.add_edge("C7","C5", path ="Walk Straight")
G.add_edge("C7","C6", path ="Walk Straight")
G.add_edge("C7","C8", path ="Turn Left")
G.add_edge("C8","C5", path ="Walk Straight")
G.add_edge("C8","C7", path ="Turn Right")
G.add_edge("C8","C9", path ="Turn Left")
G.add_edge("C9","C6", path ="Turn Left")
G.add_edge("C9","C8", path ="Turn Right")

# Stairs to corridor
G.add_edge("Stair 4","C5", path = "Walk straight")

# Room to Room 
# Corridor 1
G.add_edge("02-01","02-02",path = "Turn left and walk striaght, it is the first room on the left")
G.add_edge("02-01","02-03",path = "Turn left and walk straight, it is the second room on the left")
G.add_edge("02-02","02-01", path = "Turn right and walk straight, it is the first room on the right")
G.add_edge("02-02","02-03", path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-03","02-01", path = "Turn right and walk straight, it is the second room on the right")
G.add_edge("02-03","02-02",path = "Turn right and walk straight, it is the first room on the right")
# Corridor 2 has nothing 
# Corridor 3 has nothing 
# Corridor 4 has nothing 
# Corridor 5 has nothing 
# Corridor 6 
G.add_edge("02-07","02-08",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-07","02-09",path = "Turn left and walk straight, it is the second room on the left")
G.add_edge("02-07","02-10",path = "Turn left and walk straight, it is the third room on the left")
G.add_edge("02-08","02-07",path = "Turn right and walk straight, it is the first room on the right")
G.add_edge("02-08","02-09",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-08","02-10",path = "Turn left and walk straight, it is the second room on the left")
G.add_edge("02-09","02-07",path = "Turn right and walk straight, it is the second room on the left")
G.add_edge("02-09","02-08",path = "Turn right and walk straight, it is the first room on the left")
G.add_edge("02-09","02-10",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-10","02-07", path = "Turn right and walk straight, it is the third room on the right")
G.add_edge("02-10","02-08", path = "Turn right and walk straight, it is the second room on the right")
G.add_edge("02-10","02-09", path = "Turn right and walk straight, it is the first room on the right")
# Corridor 7 has nothing 
# Corridor 8
G.add_edge("02-15","02-16",path = "Turn right and walk straight, it is the second room on the right")
G.add_edge("02-15","02-17",path = "Turn right and walk straight, it is the third room on the right")
G.add_edge("02-15","02-18",path = "It is the room directly opposite")
G.add_edge("02-15","02-20",path = "Turn right and walk straight, it is the third room on the left")
G.add_edge("02-15","02-21",path = "Turn right and walk straight, it is the fourth room on the left")
G.add_edge("02-16","02-15",path = "Turn left and walk straight, it is the second room on the left")
G.add_edge("02-16","02-17",path = "Turn right and walk straight, it is the first room on the left")
G.add_edge("02-16","02-18",path = "Turn left and walk straight, it is the second room on the right")
G.add_edge("02-16","02-20",path = "It is the room directly opposite")
G.add_edge("02-16","02-21",path = "Turn right and walk straight, it is the first room on the right")
G.add_edge("02-17","02-15",path = "Turn left and walk straight, it is the third room on the left")
G.add_edge("02-17","02-16",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-17","02-18",path = "Turn left and walk straight, it is the third room on the left")
G.add_edge("02-17","02-20",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-17","02-21",path = "It is the room directly opposite")
G.add_edge("02-18","02-15",path = "It is the room directly opposite")
G.add_edge("02-18","02-16",path = "Turn left and walk straight, it is the third room on the right")
G.add_edge("02-18","02-17",path = "Turn left and walk straight, it is the fourth room on the right")
G.add_edge("02-18","02-20",path = "Turn left and walk straight, it is the second room on the right")
G.add_edge("02-18","02-21",path = "Turn left and walk straight, it is the third room on the right")
G.add_edge("02-20","02-15",path = "Turn right and walk straight, it is the third room on the left")
G.add_edge("02-20","02-16",path = "It is the room directly opposite")
G.add_edge("02-20","02-17",path = "Turn left and walk straight, it is the second room on the right")
G.add_edge("02-20","02-18",path = "Turn right and walk straight, it is the third room on the right")
G.add_edge("02-20","02-21",path = "Turn left and walk straight, it is the first room on the left")
G.add_edge("02-21","02-15",path = "Turn right and walk straight, it is the fourth room on the left")
G.add_edge("02-21","02-16",path = "Turn right and walk straight, it is the second room on the left")
G.add_edge("02-21","02-17",path = "It is the room directly opposite")
G.add_edge("02-21","02-18",path = "Turn right and walk straight, it is the fourth room on the right")
G.add_edge("02-21","02-20",path = "Turn right and walk straight, it is the first room on the left")

# Corridor 9 has nothing 




nx.draw_planar(G, with_labels=True)
shortest_path = nx.shortest_path(G, source="02-01", target="02-15")
print("Shortest path:", shortest_path)
shortest_path_attributes = []
len = len(shortest_path)
for i in range(len - 1):
    x = shortest_path[i]
    y = shortest_path[i + 1]
    shortest_path_attributes.append(G[x][y]['path'])
print("Path of nodes in the shortest path:", shortest_path_attributes)
plt.show() 


