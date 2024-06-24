import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Node adding 
G.add_node("02-01") # Seminar Room 5
G.add_node("02-02") # Computing Gallery
G.add_node("02-03") # Seminar Room 6
G.add_node("02-C1") # As depicted in the diagram
G.add_node("02-04") # Seminar Room 2
G.add_node("02-C2") # As depicted in the diagram
G.add_node("02-05") # Cerebro@SoC
G.add_node("02-C5") # As depicted in the diagram
G.add_node("02-06-1") # Seminar Room 1 Along Corridor 3
G.add_node("02-06-2") # Seminar Room 1 Along Corridor 4
G.add_node("02-C3") # As depicted in the diagram
G.add_node("02-C4") # As depicted in the diagram
G.add_node("02-07") # Seminar Room 7
G.add_node("02-08") # Seminar Room 8
G.add_node("02-09") # Seminar Room 9
G.add_node("02-10") # Seminar Room 10
G.add_node("02-C6") # As depicted in the diagram
# There is no 02-11
G.add_node("02-12") # Seminar Room 3
G.add_node("02-C7") # As depicted in the diagram
# 02-13 is VC Room 
G.add_node("02-14") # Tutorial Room 12
G.add_node("02-C9") # As depicted in the diagram
G.add_node("02-15") # ICPC Lab 
G.add_node("02-16") # Tutorial Room 11
G.add_node("02-17") # Tutorial Room 10
G.add_node("02-18") # Computing Club 
G.add_node("02-C8") # As depicted in the diagram
# 02-19 is Undergraduate Studies office, out of bounds
G.add_node("02-20") # Discussion Room 12
G.add_node("02-21") # Student's Lounge
# G.add_node("Staircase 4") added alr
# G.add_node("Lift")
G.add_node("Cerebro Glass Door") # As stated
G.add_node("SR3 Glass Door") # As stated

# Edge adding between corridor and room
G.add_edge("02-01","02-C1", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-02","02-C1", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-03","02-C1", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-04","02-C2", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-06-1","02-C3", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-06-2","02-C4", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-05","02-C5", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-07","02-C6", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-08","02-C6", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-09","02-C6", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-10","02-C6", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-12","02-C7", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")
G.add_edge("02-15","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-16","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-17","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-18","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-20","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-21","02-C8", path = "Walk straight till you see this corridor", image="https://l1nq.com/gHqw7")
G.add_edge("02-14","02-C9", path = "Walk til you see the corridor on the next page", image="https://l1nq.com/gHqw7")

# Reverse Edges between corridor and room 
G.add_edge("02-C1","02-01", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C1","02-02", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C1","02-03", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C2","02-04", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C3","02-06-1", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C4","02-06-2", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C5","02-05", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C6","02-07", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C6","02-08", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C6","02-09", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C6","02-10", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C7","02-12", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-15", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-16", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-17", path = "Walk straight, the room is on left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-18", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-20", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C8","02-21", path = "Walk straight, the room is on right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-C9","02-14", path = "Your destination is along this corridor", image="https://acesse.dev/b1Qf1")

#Edge adding between corridors:
G.add_edge("02-C1","02-C2", path ="Turn right, then turn left", image="https://l1nq.com/gHqw7")
G.add_edge("02-C1","02-C3", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C2","02-C1", path ="Turn left", image="https://l1nq.com/gHqw7")
G.add_edge("02-C2","02-C3", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C2","Cerebro Glass Door", path ="Walk straight pass the door", image="https://i.imghippo.com/files/soRwz1719230137.jpg")
G.add_edge("Cerebro Glass Door", "02-C2", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("Cerebro Glass Door","02-C4", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C4", "Cerebro Glass Door", path ="Walk straight pass the door", image="https://i.imghippo.com/files/qLqVC1719230080.jpg")
G.add_edge("Cerebro Glass Door","02-C5", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C5","Cerebro Glass Door", path ="Turn left and walk pass the door", image="https://i.imghippo.com/files/qLqVC1719230080.jpg")
G.add_edge("02-C3","02-C1", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C3","02-C2", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C3","Cerebro Glass Door", path ="Turn left and walk pass the door", image="https://i.imghippo.com/files/soRwz1719230137.jpg")
G.add_edge("Cerebro Glass Door", "02-C3", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C4","02-C5", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C4","SR3 Glass Door", path ="Turn left and walk pass the door", image="https://i.imghippo.com/files/P6r541719230289.jpg")
G.add_edge("SR3 Glass Door", "02-C4", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("SR3 Glass Door","02-C6", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C4","02-C7", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C5","02-C4", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C5","02-C7", path ="Turn right", image="https://l1nq.com/gHqw7")
G.add_edge("02-C5","02-C8", path ="Walk straight", image="https://i.imghippo.com/files/FfVm81719230388.jpg") #Photo of Cerebro to Com Club Student Room 
G.add_edge("02-C6", "SR3 Glass Door", path="Walk pass this glass door, turn left and walk pass the door", image="https://i.imghippo.com/files/dqFic1719230168.jpg")
G.add_edge("SR3 Glass Door","02-C7", path ="Head straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C6","02-C9", path ="Turn right", image="https://i.imghippo.com/files/oX5Rr1719230234.jpg")
G.add_edge("02-C7","02-C4", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C7","02-C5", path ="Walk straight", image="https://l1nq.com/gHqw7")
G.add_edge("02-C7","SR3 Glass Door", path ="Walk straight pass the door", image="https://i.imghippo.com/files/P6r541719230289.jpg")
G.add_edge("02-C7","02-C8", path ="Turn left", image="https://i.imghippo.com/files/qIpB41719230726.png") #blank, to fill
G.add_edge("02-C8","02-C5", path ="Walk straight", image="https://i.imghippo.com/files/lAOxw1719230332.jpg")
G.add_edge("02-C8","02-C7", path ="Turn right", image="https://i.imghippo.com/files/lAOxw1719230332.jpg")
G.add_edge("02-C8","02-C9", path ="Turn left at the end of the corridor after exiting door", image="https://i.imghippo.com/files/FfVm81719230388.jpg")
G.add_edge("02-C9","02-C6", path ="Turn left", image="https://i.imghippo.com/files/NfiBi1719230468.jpg")
G.add_edge("02-C9","02-C8", path ="Turn right", image="https://i.imghippo.com/files/ZPbea1719230443.jpg")

# Stairs to corridor
G.add_edge("Staircase 4","02-C5", path = "Walk straight and turn left, walking pass the door", image="https://i.imghippo.com/files/qIpB41719230726.png") #blank, to fill

# Reverse Stairs to corridor
G.add_edge("02-C5","Staircase 4", path = "Walk straight pass the door and head down the staircase on the right", image="https://i.imghippo.com/files/Fcxl41719230492.jpg")

# Room to Room 
# Corridor 1
G.add_edge("02-01","02-02",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-01","02-03",path = "Turn left and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-02","02-01", path = "Turn right and walk straight, it is the first room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-02","02-03", path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-03","02-01", path = "Turn right and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-03","02-02",path = "Turn right and walk straight, it is the first room on the right", image="https://acesse.dev/b1Qf1")
# Corridor 2 has nothing 
# Corridor 3 has nothing 
# Corridor 4 has nothing 
# Corridor 5 has nothing 
# Corridor 6 
G.add_edge("02-07","02-08",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-07","02-09",path = "Turn left and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-07","02-10",path = "Turn left and walk straight, it is the third room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-08","02-07",path = "Turn right and walk straight, it is the first room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-08","02-09",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-08","02-10",path = "Turn left and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-09","02-07",path = "Turn right and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-09","02-08",path = "Turn right and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-09","02-10",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-10","02-07", path = "Turn right and walk straight, it is the third room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-10","02-08", path = "Turn right and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-10","02-09", path = "Turn right and walk straight, it is the first room on the right", image="https://acesse.dev/b1Qf1")
# Corridor 7 has nothing 
# Corridor 8
G.add_edge("02-15","02-16",path = "Turn right and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-15","02-17",path = "Turn right and walk straight, it is the third room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-15","02-18",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-15","02-20",path = "Turn right and walk straight, it is the third room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-15","02-21",path = "Turn right and walk straight, it is the fourth room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-16","02-15",path = "Turn left and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-16","02-17",path = "Turn right and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-16","02-18",path = "Turn left and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-16","02-20",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-16","02-21",path = "Turn right and walk straight, it is the first room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-17","02-15",path = "Turn left and walk straight, it is the third room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-17","02-16",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-17","02-18",path = "Turn left and walk straight, it is the third room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-17","02-20",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-17","02-21",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-18","02-15",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-18","02-16",path = "Turn left and walk straight, it is the third room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-18","02-17",path = "Turn left and walk straight, it is the fourth room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-18","02-20",path = "Turn left and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-18","02-21",path = "Turn left and walk straight, it is the third room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-20","02-15",path = "Turn right and walk straight, it is the third room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-20","02-16",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-20","02-17",path = "Turn left and walk straight, it is the second room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-20","02-18",path = "Turn right and walk straight, it is the third room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-20","02-21",path = "Turn left and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-21","02-15",path = "Turn right and walk straight, it is the fourth room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-21","02-16",path = "Turn right and walk straight, it is the second room on the left", image="https://acesse.dev/b1Qf1")
G.add_edge("02-21","02-17",path = "It is the room directly opposite", image="https://acesse.dev/b1Qf1")
G.add_edge("02-21","02-18",path = "Turn right and walk straight, it is the fourth room on the right", image="https://acesse.dev/b1Qf1")
G.add_edge("02-21","02-20",path = "Turn right and walk straight, it is the first room on the left", image="https://acesse.dev/b1Qf1")
# Corridor 9 has nothing 


# nx.draw(G, with_labels=True)
# shortest_path = nx.shortest_path(G, source="02-01", target="02-14")
# print("Shortest path:", shortest_path)
# shortest_path_attributes = []
# len = len(shortest_path)
# for i in range(len - 1):
#     x = shortest_path[i]
#     y = shortest_path[i + 1]
#     shortest_path_attributes.append(G[x][y]['path'])
# print("Path of nodes in the shortest path:", shortest_path_attributes)
# plt.show() 


