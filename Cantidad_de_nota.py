import Funciones_de_cantidad_de_nota 


while True:

    grade = float(input("Ingrese su nota: "))

    Funciones_de_cantidad_de_nota.addGrade(grade)

    answer = input("¿Desea ingresar otra nota? (s/n): ")

    answer = answer.upper()

    if answer == "N":
        break


print("\n--- RESULTADO FINAL ---")
Funciones_de_cantidad_de_nota.showGrades()