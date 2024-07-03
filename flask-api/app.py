from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)
# In-memory storage for demonstration purposes
data_store = ["manoj","alok"]

@app.route('/', methods=['GET'])
def get_home():
    return "This is the home page", 200


# GET endpoint
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

# POST endpoint
@app.route('/items', methods=['POST'])
def add_item():
    item = request.data.decode('utf-8')
    data_store.append(item)
    return jsonify({'message': 'Item added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
