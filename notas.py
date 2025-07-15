# notas.py

from datetime import datetime

notas = []

def agregar_nota(nota):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notas.append(f"[{fecha}] {nota}")
    print("Nota agregada.")

def ver_notas():
    print("Tus notas:")
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota}")

while True:
    print("\n1. Agregar nota")
    print("2. Ver notas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nota = input("Escribe tu nota: ")
        agregar_nota(nota)
    elif opcion == "2":
        ver_notas()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
