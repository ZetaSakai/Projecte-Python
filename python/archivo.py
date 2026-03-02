# AulaManager - Operació Aula Zero

equips = [] # Lista de equipos

contador_id = 1 # Variable ID automático

# Bucle principal
while True:
    print("\n===== AulaManager =====")
    print("1. Dar de alta un equipo")       
    print("2. Ver todos los equipos")      
    print("3. Consultar estado de un equipo") 
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        equipo = {
            "id": contador_id,              
            "tipo": input("Tipo (PC, Portátil, Impresora, Switch, AP, Servidor): "),
            "nombre": input("Nombre del equipo: "),
            "aula": input("Aula: "),
            "serie": input("Número de serie: "),
            "so": input("Sistema operativo: "),
            "ram": input("RAM (ej: 16GB): "),
            "disc": input("Disco (ej: 512GB SSD): "),
            "estado": input("Estado (operativo/avariado/reparación/baja): "),
            "ip": input("IP (opcional): "),
            "mac": input("MAC (opcional): "),
            "observaciones": input("Observaciones: ")
        }

        # Guardamos el equipo en la lista
        equips.append(equipo)
        print(f"Equipo registrado con ID: {contador_id}")

        # Aumentamos el contador
        contador_id += 1

    elif opcion == "2":
        if len(equips) == 0:
            print("No hay equipos registrados.")
        else:
            for e in equips:
                print("----------------------------")
                for clave, valor in e.items(): #e representa un equipo de cada bucle
                    print(f"{clave}: {valor}")

    elif opcion == "3":
        serie_buscar = input("Introduce el número de serie del equipo: ")
        for e in equips: #e representa un equipo de cada bucle
            if e["serie"] == serie_buscar:
                print(f"El estado del equipo '{"nombre"}' es: {e['estado']}")
                break
        else:
            print("No se ha encontrado ningún equipo con ese número de serie.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")