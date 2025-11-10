# API de Gestión de Tareas 📝

Esta es una API simple construida con Flask que permite gestionar tareas. Incluye funcionalidades para crear, leer, actualizar y eliminar tareas, así como para marcarlas como completadas.

---

## Características 🚀

- **Crear tareas:** Añadir nuevas tareas con un título y una descripción.
- **Listar tareas:** Obtener todas las tareas, filtradas por estado (completadas o pendientes).
- **Obtener una tarea específica:** Ver los detalles de una tarea por su ID.
- **Actualizar tareas:** Modificar el título, la descripción o el estado de una tarea.
- **Marcar tareas como completadas:** Cambiar el estado de una tarea a completada.
- **Eliminar tareas:** Eliminar una tarea por su ID.

---

## Requisitos 📋

- Python 3.8 o superior.
- Flask y SQLAlchemy (instalados automáticamente con `requirements.txt`).

---

## Instalación 🛠️

1. Clona este repositorio:

   ```bash
   git clone https://github.com/ITZ-NANO21-MC/API-Tarea.git
   cd task-api
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicia la aplicación:

   ```bash
   python app.py
   ```

   La API estará disponible en `http://127.0.0.1:5000`.

---

## Uso 🚀

### Endpoints Disponibles

#### Tareas
- **Crear una tarea:**
  ```
  POST /tasks
  ```
  **Body:**
  ```json
  {
    "title": "Comprar leche",
    "description": "Ir al supermercado"
  }
  ```

- **Obtener todas las tareas:**
  ```
  GET /tasks
  ```

  **Filtrar por estado:**
  ```
  GET /tasks?status=completed
  GET /tasks?status=pending
  ```

- **Obtener una tarea específica:**
  ```
  GET /tasks/<int:task_id>
  ```

- **Actualizar una tarea:**
  ```
  PUT /tasks/<int:task_id>
  ```
  **Body:**
  ```json
  {
    "title": "Comprar pan",
    "description": "Ir a la panadería",
    "completed": true
  }
  ```

- **Marcar una tarea como completada:**
  ```
  PATCH /tasks/<int:task_id>/complete
  ```

- **Eliminar una tarea:**
  ```
  DELETE /tasks/<int:task_id>
  ```

---

## Estructura del Proyecto 📂

```
/task-api
│
├── app.py                # Punto de entrada de la aplicación
├── routes.py             # Definición de las rutas
├── model.py              # Modelo de la base de datos (Task)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo
└── database.db           # Base de datos SQLite (se crea automáticamente)
```

---

## Ejemplos de Respuestas

### Respuesta Exitosa (Crear Tarea)
```json
{
  "id": 1,
  "title": "Comprar leche",
  "description": "Ir al supermercado",
  "completed": false,
  "created_at": "2023-10-01T12:00:00",
  "updated_at": "2023-10-01T12:00:00"
}
```

### Error (Datos Incompletos)
```json
{
  "message": "Datos incompletos"
}
```

### Error (Tarea No Encontrada)
```json
{
  "message": "Task not found"
}
```

---

## Contribuir 🤝

¡Las contribuciones son bienvenidas! Si deseas mejorar esta API, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## Licencia 📄

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
