from flask import Flask, request, jsonify
import networkx as nx

app = Flask(__name__)

G = nx.DiGraph()
G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_edge("1", "2")
G.add_edge("2", "3")
G.add_edge("4", "3")

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