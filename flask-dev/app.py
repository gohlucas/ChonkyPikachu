from flask import Flask, request, jsonify
import networkx as nx
from COM1 import path_finder
import matplotlib as plt

# deployed flask on render to allow next.js to talk to networkx
app = Flask(__name__)

#Database for networkx queries
# G = nx.DiGraph()
# G.add_nodes_from(all_nodes)
# G.add_edges_from(all_edges)
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

    path = path_finder(start, end)

    if not path:
        return jsonify({'error': 'No path found'}), 400

    return jsonify(path)

if __name__ == "__main__":
    app.run(debug=True)