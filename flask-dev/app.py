from flask import Flask, request, jsonify
import networkx as nx
from COM1 import all_nodes, all_edges
import matplotlib as plt

# deployed flask on render to allow next.js to talk to networkx
app = Flask(__name__)

#Database for networkx queries
G = nx.DiGraph()
G.add_nodes_from(all_nodes)
G.add_edges_from(all_edges)
# nx.draw(G, with_labels=True)
# plt.show()clear

#app details
@app.route('/')
def home():
    return 'Just a homepage, nothing to see here...'

@app.route('/shortest_path', methods=['GET'])
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