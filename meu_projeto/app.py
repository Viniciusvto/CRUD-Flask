from flask import Flask, jsonify, request

app = Flask(__name__)  # cria uma instância do aplicativo Flask

# 1. Variáveis globais no topo do arquivo
tasks = []  # Lista para armazenar as tarefas
task_id_control = 1  # Controlador de ID


# 2. Definição das Rotas
@app.route("/") #chama o app (instancia) e cria  a rota raiz do aplicativo
def hello(): # a função mostra uma msg dentro da rota raiz
    return "Servidor Flask está funcionando!" \
    "\nAcesse /tasks para ver as tarefas."


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


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks, "total": len(tasks)})


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "tarefa não encontrada"}), 404
    return jsonify({"task": task})


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    data = request.get_json()
    # Atualiza os campos da tarefa com os dados enviados
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify({"message": "Tarefa atualizada com sucesso!", "task": task})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso!"})


# 3. Inicialização do servidor SEMPRE no final do arquivo
if __name__ == "__main__": # verifica se o arquivo está sendo executado diretamente e não importado como módulo
    app.run(debug=True) #roda o servidor em modo de depuração para facilitar o desenvolvimento
