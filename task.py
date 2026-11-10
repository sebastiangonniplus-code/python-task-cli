import sys
import json
import os
from datetime import datetime

class Tarea:
    # Modela una tarea con su id, descripción, estado y fecha de creación.
    def __init__(self, id, descripcion, estado, fecha_de_creacion):
        self.id = id
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_de_creacion = fecha_de_creacion

class GestorDeTareas:
    # Modela al gestor de Tareas con el nombre del archivo y guardando las tareas.
    
    def __init__(self, nombre_de_archivo="tareas.json"):
        self.nombre_de_archivo = nombre_de_archivo
        self.lista_de_tareas = []
        self.cargar_tareas()
        
    def cargar_tareas(self):
        # Carga las tareas en el sistema.
        if os.path.exists(self.nombre_de_archivo):
            with open(self.nombre_de_archivo, "r", encoding="utf-8") as archivo:
                try:
                    self.lista_de_tareas = json.load(archivo)
                except json.JSONDecodeError:
                    self.lista_de_tareas = []
        else:
            self.lista_de_tareas = []                        
            
    def agregar_tarea(self, descripcion):
        # Agrega una tarea nueva.
        nuevo_id = self.lista_de_tareas[-1]["id"] + 1 if self.lista_de_tareas else 1
        now = datetime.now() # Fecha actual.
        fecha_actua_en_string = now.strftime("%d/%m/%Y, %H:%M")
        
        nueva_tarea = {
            "id": nuevo_id,
            "estado": "todo",
            "descripcion": descripcion,
            "creado_el": fecha_actua_en_string
        }
        
        self.lista_de_tareas.append(nueva_tarea)
        self.guardar_en_archivo()
        print(f"Tarea agregada correctamente, ID: {nuevo_id}")
        
    def guardar_en_archivo(self):
        # Guarda la lista de tareas en el archivo.
        with open(self.nombre_de_archivo, "w", encoding="utf-8") as archivo:  
            json.dump(self.lista_de_tareas, archivo, indent=4, ensure_ascii=False)