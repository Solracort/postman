from flask import Flask, jsonify, request
app = Flask(__name__)
todos = [{ "label": "My first task", "done": False },
         {"label": "My second task", "done": False}]

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("Elemento a borrar", position)
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)
    # return jsonify("SE HA CREADO UNA NUEVA TAREA")

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text=jsonify(todos)
    return json_text
# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)