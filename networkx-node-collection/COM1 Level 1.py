import networkx as nx
import matplotlib.pyplot as plt
import pyodbc

#Venv installed networkx, matplotlib, pyodbc, flask
G = nx.DiGraph()

G.add_node("01-07") #Database 3 Electronic Commerce & Database
G.add_node("01-08") #Database 1
G.add_node("01-09") #E&A Cluster 4
G.add_node("01-10") #E&A Cluster 2
G.add_node("01-11") #Datanase 2
G.add_node("01-12") #Artificial Intelligence 1: Adaptive Computing
G.add_node("01-13") #Embedded Systems Teaching Lab 2
G.add_node("01-14") #Embedded Systems Teaching Lab 1
G.add_node("01-15") #Computational Biology 2
G.add_node("01-16") #E&A Cluster 1
G.add_node("01-18") #MR 5
G.add_node("01-19") #E&A Cluster 2
G.add_node("01-20") #Programming Lab 6
G.add_node("01-21") #Computational Biology 1
G.add_node("01-22") #MR 4
G.add_node("01-23") #Career Consultation Room
G.add_node("01-24") #Robot Living Studio
G.add_node("Staircase 1") #Near Robot Living Studio
G.add_node("Staircase 2") #Near Computational Biology 1
G.add_node("Staircase 3") #Near E&A Cluster 4
G.add_node("Staircase 4") #Beside Lift Lobby
G.add_node("C1") #As depicted in Diagram
G.add_node("C2") #As depicted in Diagram
G.add_node("C3") #As depicted in Diagram
G.add_node("C4") #As depicted in Diagram
G.add_node("C5") #As depicted in Diagram
G.add_node("C6") #As depicted in Diagram
G.add_node("C7") #As depicted in Diagram
G.add_node("C8") #As depicted in Diagram
G.add_node("C9") #As depicted in Diagram
G.add_node("C10") #As depicted in Diagram
G.add_node("C11") #As depicted in Diagram
G.add_node("C12") #As depicted in Diagram
G.add_node("C13") #As depicted in Diagram
G.add_node("C14") #As depicted in Diagram


#C1
G.add_edge("01-07", "C1")
G.add_edge("01-08", "C1")
G.add_edge("01-11", "C1")
G.add_edge("01-12", "C1")
G.add_edge("01-13", "C1")
G.add_edge("01-14", "C1")
G.add_edge("01-15", "C1")
#Reverse C1
G.add_edge("C1", "01-07")
G.add_edge("C1", "01-08")
G.add_edge("C1", "01-11")
G.add_edge("C1", "01-12")
G.add_edge("C1", "01-13")
G.add_edge("C1", "01-14")
G.add_edge("C1", "01-15")
#C2
G.add_edge("01-08", "C2")
G.add_edge("01-09", "C2")
#Reverse C2
G.add_edge("C2", "01-08")
G.add_edge("C2", "01-09")
#C3
G.add_edge("01-09", "C3")
G.add_edge("01-10", "C3")
#Reverse C3
G.add_edge("C3", "01-09")
G.add_edge("C3", "01-10")
#C4
G.add_edge("01-18", "C4")
#Reverse C4
G.add_edge("C4", "01-18")
#C5
G.add_edge("01-19", "C5")
#Reverse C5
G.add_edge("C5", "01-19")
#C6
G.add_edge("01-11", "C6")
#Reverse C6
G.add_edge("C6", "01-11")
#C7
G.add_edge("01-12", "C7")
#Reverse C7
G.add_edge("C7", "01-12")
#C8
G.add_edge("01-13", "C8")
G.add_edge("01-20", "C8")
#Reverse C8
G.add_edge("C8", "01-13")
G.add_edge("C8", "01-20")
#C9
G.add_edge("01-21", "C9")
G.add_edge("01-22", "C9")
#Reverse C8
G.add_edge("C9", "01-21")
G.add_edge("C9", "01-22")
#C11
G.add_edge("01-21", "C11")
#Reverse C11
G.add_edge("C11", "01-21")
#C12
G.add_edge("01-14", "C12")
G.add_edge("01-16", "C12")
#Reverse C12
G.add_edge("C12", "01-14")
G.add_edge("C12", "01-16")
#C13
G.add_edge("01-23", "C13")
#Reverse C13
G.add_edge("C13", "01-23")
#C14
G.add_edge("01-24", "C14")
#Reverse C14
G.add_edge("C14", "01-24")
#Corridor Link
G.add_edge("C2", "C3")
G.add_edge("C2", "C1")
G.add_edge("C1", "C14")
G.add_edge("C3", "C4")
G.add_edge("C3", "C6")
G.add_edge("C4", "C5")
G.add_edge("C6", "C7")
G.add_edge("C6", "C8")
G.add_edge("C8", "C9")
G.add_edge("C8", "C12")
G.add_edge("C9", "C10")
G.add_edge("C10", "C11")
G.add_edge("C12", "C13")
G.add_edge("C12", "C14")
#Reverse Corridor Link
G.add_edge("C3", "C2")
G.add_edge("C1", "C2")
G.add_edge("C14", "C1")
G.add_edge("C4", "C3")
G.add_edge("C6", "C3")
G.add_edge("C5", "C4")
G.add_edge("C7", "C6")
G.add_edge("C8", "C6")
G.add_edge("C9", "C8")
G.add_edge("C12", "C8")
G.add_edge("C10", "C9")
G.add_edge("C11", "C10")
G.add_edge("C13", "C12")
G.add_edge("C14", "C12")
#Staircase Link
G.add_edge("C1", "Staircase 1")
G.add_edge("C14", "Staircase 1")
G.add_edge("C9", "Staircase 2")
G.add_edge("C10", "Staircase 2")
G.add_edge("C2", "Staircase 3")
G.add_edge("C13", "Staircase 4")
#Reverse Staircase Link
G.add_edge("Staircase 1", "C1")
G.add_edge("Staircase 1", "C14")
G.add_edge("Staircase 2", "C9")
G.add_edge("Staircase 2", "C10")
G.add_edge("Staircase 3", "C2")
G.add_edge("Staircase 4", "C13")
