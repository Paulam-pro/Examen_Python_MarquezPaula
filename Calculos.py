
def calcular_propina():

    while True:
        print("======================================")
        print("        Calculo de propina        ")
        print("======================================")
        precio = float(input("Ingrese el monto total de la cuenta:$ "))
        porcentaje = float(input("Dijite el porcentaje de propina que desee dejar (10%, 15%, 20%): "))

        
        if precio <= 0 or porcentaje <= 0 :
            print("El monto total y porcentaje debe ser mayor a 0")
            print("Ingrese numeros validos")
            return None
        
        monto_total = precio * (porcentaje/100)
        total_pagar = monto_total + precio
        
        print(f"La propina calculada es: ${monto_total:}")
        print(f"El total a pagar es: ${total_pagar}")

        print("===============================")
        print("¿Deseas calcular nuevamente?"  )
        print("1. Si")
        print("2. No gracias")

        opcion =int(input("Selecciona una opcion: "))
        
        if opcion == 1:
            calcular_propina()
        elif opcion == 2:
            print("Gracias por su visita")
            break
    

def dividir_total():
    
    while True:
        print("======================================")
        print(" Dividir Cuenta entre Varias Personas ")
        print("======================================")
        precio = float(input("Ingrese el monto total de la cuenta:$ "))
        porcentaje = float(input("Dijite el porcentaje de propina que desee dejar (por ejemplo: 15): "))
        personas = int(input("Ingrese el número de personas que desee dividir la cuenta: "))

        if precio <= 0 or porcentaje <= 0:
            print("El monto total y porcentaje debe ser mayor a 0")
            print("Ingrese numeros validos")
            return None
        
        propina = precio * (porcentaje/100)
        total_pagar = propina + precio
        monto_total = total_pagar / personas
        
            
        print(f"La propina calculada es: ${propina:}")
        print(f"El total a pagar es: ${total_pagar}")
        print(f"Monto por persona: ${monto_total}")
        
        print("===============================")
        print(" ¿Deseas calcular nuevamente?"  )
        print("1. Si")
        print("2. No gracias")

        opcion =int(input("Selecciona una opcion: "))
        
        if opcion == 1:
            dividir_total()
        elif opcion == 2:
            print("==================== ")
            print("Gracias por su visita")
            break
            


