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

    def enlistar_tareas(self):
        #Enlista las tareas que haya en el json.
        if  not self.lista_de_tareas:
            print("No hay tareas pendientes.")
        else:
            print("--- LISTA DE TAREAS: ---")
            for tarea in self.lista_de_tareas:
                print(f"ID: {tarea['id']} | ESTADO: {tarea['estado']}  {tarea['descripcion']} CREADO: {tarea['creado_el']}")
                print("------------------------")

    def marcar_tarea_completada(self,id_tarea):
        #Marca una tarea  como completada.
        encontrada = False
        for tarea in self.lista_de_tareas:
            if tarea['id'] == int(id_tarea):
                tarea['estado'] = 'Completado'
                self.guardar_en_archivo()
                print(f"Tarea con ID: {id_tarea} Marcada como completada.")
                encontrada = True
                break
        if not encontrada:
            print("ID no encontrado.")



if __name__ == "__main__":
    gestor = GestorDeTareas()

    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "add" and len(sys.argv) > 2:
            gestor.agregar_tarea(sys.argv[2])
        elif comando == "list":
            gestor.enlistar_tareas()
        elif comando == "done" and len(sys.argv) > 2:
            # sys.argv[2] será el ID de la tarea que queremos completar
            gestor.marcar_tarea_completada(sys.argv[2])
        else:
            print("Comando inválido o faltan argumentos.")
    else:
        print("Uso: python task.py [add/list/done] [argumento]")