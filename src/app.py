from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

# Suppose you have your data in the variable named some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text



@app.route('/todos', methods=['GET'])
def todosGet():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Validate if the position is within range
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400  # Bad Request

    # Remove the task from the list
    deleted_task = todos.pop(position)
    print(f"Deleted task: {deleted_task}")

    # Return the updated todos list
    return jsonify(todos)









# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)