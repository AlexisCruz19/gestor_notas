from datetime import datetime
import os

ARCHIVO = "notas.txt"
notas = []

def cargar_notas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                notas.append(linea.strip())

def guardar_notas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for nota in notas:
            f.write(nota + "\n")

def agregar_nota(nota):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nota_formateada = f"[{fecha}] {nota}"
    notas.append(nota_formateada)
    guardar_notas()
    print("Nota agregada.")

def ver_notas():
    print("Tus notas:")
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota}")

def editar_nota(indice, nueva_nota):
    if 0 <= indice < len(notas):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notas[indice] = f"[{fecha}] {nueva_nota}"
        guardar_notas()
        print("Nota editada.")
    else:
        print("Índice no válido.")

# Cargar notas al iniciar
cargar_notas()

while True:
    print("\n1. Agregar nota")
    print("2. Ver notas")
    print("3. Editar nota")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nota = input("Escribe tu nota: ")
        agregar_nota(nota)
    elif opcion == "2":
        ver_notas()
    elif opcion == "3":
        ver_notas()
        try:
            numero = int(input("¿Qué número de nota quieres editar? ")) - 1
            nueva = input("Escribe la nueva nota: ")
            editar_nota(numero, nueva)
        except ValueError:
            print("Entrada no válida.")
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
