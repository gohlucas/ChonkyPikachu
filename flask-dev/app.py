from flask import Flask, request, jsonify
import networkx as nx

app = Flask(__name__)

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

#C1
G.add_edge("B-01", "C1", path="1")
G.add_edge("B-02", "C1", path="2")
G.add_edge("B-03", "C1", path="3")
G.add_edge("B-04", "C1", path="4")
G.add_edge("B-05", "C1", path="5")
G.add_edge("B-08", "C1", path="6") 
#Reverse C1
G.add_edge("C1", "B-01", path="7")
G.add_edge("C1", "B-02", path="8")
G.add_edge("C1", "B-03", path="9")
G.add_edge("C1", "B-04", path="10")
G.add_edge("C1", "B-05", path="11")
G.add_edge("C1", "B-08", path="12") 
#C2
G.add_edge("B-06", "C2", path="13") 
#Reverse C2
G.add_edge("C2", "B-06", path="14") 
#C3
G.add_edge("B-07", "C3", path="15")
G.add_edge("B-08", "C3", path="16")
G.add_edge("B-09", "C3", path="17")
G.add_edge("B-10", "C3", path="18")
#Reverse C3
G.add_edge("C3", "B-07")
G.add_edge("C3", "B-08")
G.add_edge("C3", "B-09")
G.add_edge("C3", "B-10")
#C4
G.add_edge("B-09", "C4")
G.add_edge("B-10", "C4")
#Reverse C4
G.add_edge("C4", "B-09")
G.add_edge("C4", "B-10")
#C5
G.add_edge("B-11", "C5")
G.add_edge("B-12", "C5")
#Reverse C5
G.add_edge("C5", "B-11")
G.add_edge("C5", "B-12")
#C6
G.add_edge("B-11", "C6")
G.add_edge("B-12", "C6")
G.add_edge("B-13", "C6", path="B-13 to C6")
#Reverse C6
G.add_edge("C6", "B-11")
G.add_edge("C6", "B-12")
G.add_edge("C6", "B-13")
#C7
G.add_edge("B-14A", "C7")
G.add_edge("B-14B", "C7")
#Reverse C7
G.add_edge("C7", "B-14A", path = "C7 to B-14A")
G.add_edge("C7", "B-14B")
#Corridor Link
G.add_edge("C1", "C3")
G.add_edge("C3", "C2")
G.add_edge("C1", "C4")
G.add_edge("C1", "C6")
G.add_edge("C4", "C5")
G.add_edge("C6", "C7", path = "C6 to C7")
#Reverse Corridor Link
G.add_edge("C3", "C1")
G.add_edge("C2", "C3")
G.add_edge("C4", "C1")
G.add_edge("C6", "C1")
G.add_edge("C5", "C4")
G.add_edge("C7", "C6")
#Staircase Link
G.add_edge("C1", "Staircase 2") 
G.add_edge("C6", "Staircase 1")
#Reverse Staircase Link
G.add_edge("Staircase 2", "C1")
G.add_edge("Staircase 1", "C6") 

@app.route('/shortest-path', methods=['GET'])
def shortest_path():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({'error': 'Please provide both start and end parameters'}), 400

    try:
        path = nx.shortest_path(G, source=start, target=end)
        length = nx.shortest_path_length(G, source=start, target=end)
        return jsonify({'path': path, 'length': length})
    except nx.NetworkXNoPath:
        return jsonify({'error': 'No path found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)