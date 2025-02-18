import os

class Tasks:    
    def __init__(self):
        pass
    
    def cargar_tareas(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
            print(file)
        return []

    def guardar_tareas(self, tareas):
        with open("tasks.txt", "w") as file:
            for tarea in tareas:
                file.write(tarea + "\n")

    def mostrar_tareas(self, tareas):
        if not tareas:
            print("\n📌 No hay tareas pendientes.")
        else:
            print("\n📋 Lista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

    def agregar_tarea(self, tareas):
        tarea = input("📝 Escribe la nueva tarea: ")
        tareas.append(tarea)
        self.guardar_tareas(tareas)
        print("✅ Tarea agregada.")

    def modificar_tarea(self, tareas):
        self.mostrar_tareas(tareas)
        try:
            num = int(input("Selecciona la tarea a modificar: "))
            if 1 <= num and num <= len(tareas):
                nueva_tarea = input("Escribe la nueva tarea: ")
                tareas[num - 1] = nueva_tarea
                self.guardar_tareas(tareas)
                print("Tarea modificada.")
            else:
                print("Numero de tarea invalido.")
        except ValueError:
            print("Numero invalido, porfavor ingrese un numero valido.")

    def eliminar_tarea(self, tareas):
        self.mostrar_tareas(tareas)
        try:
            num = int(input("❌ Número de la tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea_eliminada = tareas.pop(num - 1)
                self.guardar_tareas(tareas)
                print(f"🗑 Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Ingresa un número válido.")
