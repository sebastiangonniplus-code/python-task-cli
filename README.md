# Task Tracker CLI

Una aplicación de línea de comandos (CLI) minimalista desarrollada en Python para gestionar tareas pendientes, en curso y completadas, guardando los datos de forma local en un archivo JSON.

## Características
- Añadir nuevas tareas con ID automático y fecha de creación.
- Actualizar la descripción de las tareas.
- Cambiar el estado de las tareas (`todo`, `in-progress`, `done`).
- Listar todas las tareas o filtrarlas por su estado actual.
- Persistencia de datos local utilizando únicamente la librería estándar de Python.

## Uso

Ejecuta el script desde la terminal pasando los comandos correspondientes:

```bash
# Añadir una tarea
python task.py add "Estudiar Python"

# Listar todas las tareas
python task.py list

# Marcar tarea como en progreso
python task.py mark-in-progress 1

# Marcar tarea como completada
python task.py mark-done 1

# Eliminar una tarea
python task.py delete 1
