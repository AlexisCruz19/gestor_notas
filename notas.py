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

def editar_nota(indice, nueva_nota):
    if 0 <= indice < len(notas):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notas[indice] = f"[{fecha}] {nueva_nota}"
        print("Nota editada.")
    else:
        print("Índice no válido.")

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
