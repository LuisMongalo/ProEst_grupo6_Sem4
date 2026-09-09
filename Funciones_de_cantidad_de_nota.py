grades = []
classification = []


import Cantidad_de_nota
def addGrade(grade):
    grades.append(grade)

    resultado = calcular_aprendizaje(grade)
    classification.append(resultado)

def calcular_aprendizaje(grade):

    if grade >= 90:
        return "Avanzado"

    elif grade >= 80:
        return "Satisfactorio"

    elif grade >= 70:
        return "Fundamental"

    else:
        return "Aprendizaje inicial"
    
def showGrades():

    for i in range(len(grades)):
        print(f"Nota: {grades[i]} - Clasificación: {classification[i]}")


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Calcular subtotal")
    print("3. Mostrar factura")
    print("4. Salir")


opcion = 0

while opcion != 3:
    mostrar_menu()

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("1. Agregar notas")

    elif opcion == 2:
        print("2. Mostrar notas")

    elif opcion == 3:
        print("3. Salir")
        
opcion = int(input("Seleccione una opción: "))

    