from flask import Blueprint, request, jsonify
from model import Task, db

task_routes = Blueprint('task_routes', __name__)

# Función auxiliar para validar datos
def validate_data(data, required_fields):
    if not data:
        return False
    for field in required_fields:
        if field not in data:
            return False
    return True

# Crear una nueva tarea
@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not validate_data(data, ['title', 'description']):
        return jsonify({'message': 'Datos incompletos'}), 400

    new_task = Task(
        title=data['title'],
        description=data['description']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'description': new_task.description,
        'completed': new_task.completed,
        'created_at': new_task.created_at,
        'updated_at': new_task.updated_at
    }), 201

# Obtener todas las tareas (filtradas por estado)
@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    if status == 'completed':
        tasks = Task.query.filter_by(completed=True).all()
    elif status == 'pending':
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.all()
    
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at,
        'updated_at': task.updated_at
    } for task in tasks])

# Obtener una tarea específica
@task_routes.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at,
        'updated_at': task.updated_at
    })

# Actualizar una tarea existente
@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    
    if not data:
        return jsonify({'message': 'Datos incompletos'}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    
    # Convertir el valor de 'completed' a booleano
    completed_str = data.get('completed', task.completed)
    if isinstance(completed_str, str):
        task.completed = completed_str.lower() in ['true', '1', 'yes', 'si']
    else:
        task.completed = bool(completed_str)
    
    db.session.commit()
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at,
        'updated_at': task.updated_at
    })

# Marcar una tarea como completada
@task_routes.route('/tasks/<int:task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at,
        'updated_at': task.updated_at
    })

# Eliminar una tarea
@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 204