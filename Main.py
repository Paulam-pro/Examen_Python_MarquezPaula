from Calculos import calcular_propina, dividir_total

def main():

    while True:
        print("======================================")
        print("       Simulador de propina        ")
        print("======================================")
        print("1. Calcular propina y total a pagar")
        print("2. Calcular total a pagar divido entre varias personas")
        print("3. Salir")

        opcion = int(input("Por favor, selecciona una opcion: "))

        if opcion == 1:
            calcular_propina()
        elif opcion == 2:
            dividir_total()
        elif opcion == 3:
            print("Gracias por utilizar el simulador de propina ")
            break
        else:
            print("opción no valida")


main()



