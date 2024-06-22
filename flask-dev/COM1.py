import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

# COM1 Basement
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
G.add_node("Staircase 3") #Staircase outside Active learning lab
G.add_node("B-C1") #As depicted in Diagram
G.add_node("B-C2") #As depicted in Diagram
G.add_node("B-C3") #As depicted in Diagram
G.add_node("B-C4") #As depicted in Diagram
G.add_node("B-C5") #As depicted in Diagram
G.add_node("B-C6") #As depicted in Diagram
G.add_node("B-C7") #As depicted in Diagram
G.add_node("B-C8") #As depicted in Diagram
#Room to Corridor
G.add_edge("B-01-2", "B-C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-02", "B-C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-03", "B-C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-04", "B-C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-05", "B-C1", path="Walk til you see the corridor on the next page")
G.add_edge("B-06", "B-C2", path="Walk til you see the corridor on the next page") 
G.add_edge("B-07", "B-C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-08-2", "B-C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-09-2", "B-C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-10-2", "B-C3", path="Walk til you see the corridor on the next page")
G.add_edge("B-09-1", "B-C4", path="Walk til you see the corridor on the next page")
G.add_edge("B-10-1", "B-C4", path="Walk til you see the corridor on the next page")
G.add_edge("B-11-2", "B-C5", path="Walk til you see the corridor on the next page")
G.add_edge("B-12-2", "B-C5", path="Walk til you see the corridor on the next page")
G.add_edge("B-11-1", "B-C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-12-1", "B-C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-13", "B-C6", path="Walk til you see the corridor on the next page")
G.add_edge("B-14A", "B-C7", path="Walk til you see the corridor on the next page")
G.add_edge("B-14B", "B-C7", path="Walk til you see the corridor on the next page")
G.add_edge("B-01-1", "B-C8", path="Walk til you see the corridor on the next page")
G.add_edge("B-08-1", "B-C8", path="Walk til you see the corridor on the next page") 
#Corridor to room
G.add_edge("B-C1", "B-01-2", path="Your destination is along this corridor")
G.add_edge("B-C1", "B-02", path="Your destination is along this corridor")
G.add_edge("B-C1", "B-03", path="Your destination is along this corridor")
G.add_edge("B-C1", "B-04", path="Your destination is along this corridor")
G.add_edge("B-C1", "B-05", path="Your destination is along this corridor")
G.add_edge("B-C2", "B-06", path="Your destination is along this corridor") 
G.add_edge("B-C3", "B-07", path="Your destination is along this corridor")
G.add_edge("B-C3", "B-08-2", path="Your destination is along this corridor")
G.add_edge("B-C3", "B-09-2", path="Your destination is along this corridor")
G.add_edge("B-C3", "B-10-2", path="Your destination is along this corridor")
G.add_edge("B-C4", "B-09-1", path="Your destination is along this corridor")
G.add_edge("B-C4", "B-10-1", path="Your destination is along this corridor")
G.add_edge("B-C5", "B-11-2", path="Your destination is along this corridor")
G.add_edge("B-C5", "B-12-2", path="Your destination is along this corridor")
G.add_edge("B-C6", "B-11-1", path="Your destination is along this corridor")
G.add_edge("B-C6", "B-12-1", path="Your destination is along this corridor")
G.add_edge("B-C6", "B-13", path="Your destination is along this corridor")
G.add_edge("B-C7", "B-14A", path="Your destination is along this corridor")
G.add_edge("B-C7", "B-14B", path="Your destination is along this corridor")
G.add_edge("B-C8", "B-01-1", path="Your destination is along this corridor")
G.add_edge("B-C8", "B-08-1", path="Your destination is along this corridor") 
#Corridor link
G.add_edge("B-C1", "B-C3", path="Turn left")
G.add_edge("B-C1", "B-C8", path="Head straight")
G.add_edge("B-C3", "B-C2", path="Turn here") #To take photo
G.add_edge("B-C3", "B-C8", path="Turn left")
G.add_edge("B-C4", "B-C5", path="Turn right")
G.add_edge("B-C4", "B-C6", path="Turn left")
G.add_edge("B-C6", "B-C7", path = "Turn right")
G.add_edge("B-C8", "B-C4", path="Turn right")
G.add_edge("B-C8", "B-C6", path="Head straight")
#Reverse Corridor link
G.add_edge("B-C3", "B-C1", path="Turn right")
G.add_edge("B-C8", "B-C1", path="Head straight")
G.add_edge("B-C2", "B-C3", path="Head straight")
G.add_edge("B-C8", "B-C3", path="Turn right")
G.add_edge("B-C5", "B-C4", path="Turn left")
G.add_edge("B-C6", "B-C4", path="Turn right")
G.add_edge("B-C7", "B-C6", path="Turn left")
G.add_edge("B-C4", "B-C8", path="Turn right")
G.add_edge("B-C6", "B-C8", path="Head straight")
#Staircase link
G.add_edge("B-C1", "Staircase 3", path="Turn left and head up the stairs") 
G.add_edge("B-C6", "Staircase 1", path="Turn right and head up the stairs")
#Reverse Staircase link
G.add_edge("Staircase 3", "B-C1", path="Turn right")
G.add_edge("Staircase 1", "B-C6", path="Turn left") 
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

#COM1 Level 1
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

#COM1 Level 2
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
G.add_edge("02-01","02-C1", path = "Walk straight till you see this corridor")
G.add_edge("02-02","02-C1", path = "Walk straight till you see this corridor")
G.add_edge("02-03","02-C1", path = "Walk straight till you see this corridor")
G.add_edge("02-04","02-C2", path = "Walk til you see the corridor on the next page")
G.add_edge("02-06-1","02-C3", path = "Walk til you see the corridor on the next page")
G.add_edge("02-06-2","02-C4", path = "Walk til you see the corridor on the next page")
G.add_edge("02-05","02-C5", path = "Walk til you see the corridor on the next page")
G.add_edge("02-07","02-C6", path = "Walk til you see the corridor on the next page")
G.add_edge("02-08","02-C6", path = "Walk straight till you see this corridor")
G.add_edge("02-09","02-C6", path = "Walk straight till you see this corridor")
G.add_edge("02-10","02-C6", path = "Walk straight till you see this corridor")
G.add_edge("02-12","02-C7", path = "Walk til you see the corridor on the next page")
G.add_edge("02-15","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-16","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-17","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-18","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-20","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-21","02-C8", path = "Walk straight till you see this corridor")
G.add_edge("02-14","02-C9", path = "Walk til you see the corridor on the next page")

# Reverse Edges between corridor and room 
G.add_edge("02-C1","02-01", path = "Walk straight, the room is on right")
G.add_edge("02-C1","02-02", path = "Walk straight, the room is on right")
G.add_edge("02-C1","02-03", path = "Walk straight, the room is on right")
G.add_edge("02-C2","02-04", path = "Your destination is along this corridor")
G.add_edge("02-C3","02-06-1", path = "Your destination is along this corridor")
G.add_edge("02-C4","02-06-2", path = "Your destination is along this corridor")
G.add_edge("02-C5","02-05", path = "Your destination is along this corridor")
G.add_edge("02-C6","02-07", path = "Your destination is along this corridor")
G.add_edge("02-C6","02-08", path = "Walk straight, the room is on left")
G.add_edge("02-C6","02-09", path = "Walk straight, the room is on left")
G.add_edge("02-C6","02-10", path = "Walk straight, the room is on left")
G.add_edge("02-C7","02-12", path = "Your destination is along this corridor")
G.add_edge("02-C8","02-15", path = "Walk straight, the room is on left")
G.add_edge("02-C8","02-16", path = "Walk straight, the room is on left")
G.add_edge("02-C8","02-17", path = "Walk straight, the room is on left")
G.add_edge("02-C8","02-18", path = "Walk straight, the room is on right")
G.add_edge("02-C8","02-20", path = "Walk straight, the room is on right")
G.add_edge("02-C8","02-21", path = "Walk straight, the room is on right")
G.add_edge("02-C9","02-14", path = "Your destination is along this corridor")

#Edge adding between corridors:
G.add_edge("02-C1","02-C2", path ="Turn right, then turn left")
G.add_edge("02-C1","02-C3", path ="Walk straight")
G.add_edge("02-C2","02-C1", path ="Turn left")
G.add_edge("02-C2","02-C3", path ="Turn right")
G.add_edge("02-C2","Cerebro Glass Door", path ="Walk straight pass the door")
G.add_edge("Cerebro Glass Door", "02-C2", path ="Walk straight")
G.add_edge("Cerebro Glass Door","02-C4", path ="Walk straight")
G.add_edge("02-C4", "Cerebro Glass Door", path ="Walk straight pass the door")
G.add_edge("Cerebro Glass Door","02-C5", path ="Turn right")
G.add_edge("02-C5","Cerebro Glass Door", path ="Turn left and walk pass the door")
G.add_edge("02-C3","02-C1", path ="Walk straight")
G.add_edge("02-C3","02-C2", path ="Turn right")
G.add_edge("02-C3","Cerebro Glass Door", path ="Turn left and walk pass the door")
G.add_edge("Cerebro Glass Door", "02-C3", path ="Turn right")
G.add_edge("02-C4","02-C5", path ="Walk straight")
G.add_edge("02-C4","SR3 Glass Door", path ="Turn left and walk pass the door")
G.add_edge("SR3 Glass Door", "02-C4", path ="Turn right")
G.add_edge("SR3 Glass Door","02-C6", path ="Turn right")
G.add_edge("02-C4","02-C7", path ="Walk straight")
G.add_edge("02-C5","02-C4", path ="Walk straight")
G.add_edge("02-C5","02-C7", path ="Turn right")
G.add_edge("02-C5","02-C8", path ="Walk straight") #Photo of Cerebro to Com Club Student Room 
G.add_edge("02-C6", "SR3 Glass Door", path="Turn left and walk pass the door")
G.add_edge("SR3 Glass Door","02-C7", path ="Head straight")
G.add_edge("02-C6","02-C9", path ="Turn right")
G.add_edge("02-C7","02-C4", path ="Walk straight")
G.add_edge("02-C7","02-C5", path ="Walk straight")
G.add_edge("02-C7","SR3 Glass Door", path ="Walk straight pass the door")
G.add_edge("02-C7","02-C8", path ="Turn left")
G.add_edge("02-C8","02-C5", path ="Walk straight")
G.add_edge("02-C8","02-C7", path ="Turn right")
G.add_edge("02-C8","02-C9", path ="Turn left")
G.add_edge("02-C9","02-C6", path ="Turn left")
G.add_edge("02-C9","02-C8", path ="Turn right")

# Stairs to corridor
G.add_edge("Staircase 4","02-C5", path = "Walk straight and turn left, walking pass the door")

# Reverse Stairs to corridor
G.add_edge("02-C5","Staircase 4", path = "Walk straight pass the door and head up the staircase on the right")

# Room to Room 
# Corridor 1
G.add_edge("02-01","02-02",path = "Turn left and walk straight, it is the first room on the left")
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


all_nodes = G.nodes
all_edges = G.edges
# nx.draw(G, with_labels=True)

#Testing
# shortest_path = nx.shortest_path(G, source="B-12-2", target="02-10")
# print("Shortest path:", shortest_path)
# shortest_path_attributes = []
# for i in range(len(shortest_path) - 1):
#     x = shortest_path[i]
#     y = shortest_path[i + 1]
#     shortest_path_attributes.append(G[x][y]['path'])
#     # shortest_path_attributes.append(G[x][y]['image'])
# print("Path of nodes in the shortest path:", shortest_path_attributes)

# plt.show() 

