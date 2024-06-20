from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data
data = ["hi there"]

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# GET endpoint
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

# POST endpoint
@app.route('/data', methods=['POST'])
def add_data():
    if request.is_json:
        new_data = request.get_json()
        data.append(new_data)
        return jsonify(new_data), 201
    else:
        return {"error": "Request must be JSON"}, 400

if __name__ == '__main__':
    app.run(debug=True)
