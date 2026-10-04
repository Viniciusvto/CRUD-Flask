from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Variáveis globais no topo do arquivo
tasks = []  # Lista para armazenar as tarefas
task_id_control = 1  # Controlador de ID


# 2. Definição das Rotas
@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control

    data = request.get_json()

    # Validação simples
    if not data or "title" not in data:
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    new_task = {
        "id": task_id_control,
        "title": data.get("title"),
        "description": data.get("description", ""),
        "completed": False,
    }

    tasks.append(new_task)
    task_id_control += 1

    return (
        jsonify({"message": "Task created successfully", "task": new_task}),
        201,
    )


# 3. Inicialização do servidor SEMPRE no final do arquivo
if __name__ == "__main__":
    app.run(debug=True)
