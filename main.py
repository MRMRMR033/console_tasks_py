import os
from taskshandler import Tasks

tasks = Tasks()

def limpiar_pantalla():
    os.system("clear")

def main():
    tareas = tasks.cargar_tareas()
    while True:
        print("\n📌 MENÚ")
        print("1️⃣ Agregar tarea")
        print("2️⃣ Ver tareas")
        print("3️⃣ Eliminar tarea")
        print("4️⃣ Salir")
        print("5 Modificar una tarea")
        
        opcion = input("👉 Elige una opción: ")
        
        if opcion == "1":
            limpiar_pantalla()
            tasks.agregar_tarea(tareas)
        elif opcion == "2":
            limpiar_pantalla()
            tasks.mostrar_tareas(tareas)
        elif opcion == "3":
            limpiar_pantalla()
            tasks.eliminar_tarea(tareas)
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        elif opcion == "5":
            limpiar_pantalla()
            tasks.modificar_tarea(tareas)
        else:
            print("⚠ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()