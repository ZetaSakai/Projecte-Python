equips = []  # Lista de equipos
contador_id = 1  # Variable ID automático

while True:
    print("===AulaManager===")
    print("1) Registrar equip")
    print("2) Consultar equip")
    print("3) Canviar estat")
    print("4) Modificar dades")
    print("5) Gestionar incidencia")
    print("0) Sortir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        tipo = input("Tipo (PC, Portátil, Impresora, Switch, AP, Servidor): ")
        nombre = input("Nombre del equipo: ")
        aula = input("Aula: ")
        serie = input("Número de serie: ")
        while serie == "":
            serie = input("Error: El número de serie es obligatorio. Introdúcelo: ")
        so = input("Sistema operativo: ")
        ram = int(input("RAM (ej: 16): "))
        disc = input("Disco (ej: 512GB SSD): ")

        estados_validos = ["operatiu", "avariat", "reparacio", "baixa"]
        estado = input("Estado (operatiu/avariat/reparacio/baixa): ")
        while estado not in estados_validos:
            print(f"Estado no válido. Elige uno de estos: {estados_validos}")
            estado = input("Estado: ")
        ip = input("IP (opcional): ")
        mac = input("MAC (opcional): ")
        observaciones = input("Observaciones: ")

        equipo = {
            "id": contador_id,
            "tipo": tipo,
            "nombre": nombre,
            "aula": aula,
            "serie": serie,
            "so": so,
            "ram": ram,
            "disc": disc,
            "estado": estado,
            "ip": ip,
            "mac": mac,
            "observaciones": observaciones
        }

        equips.append(equipo)
        print(f"Equipo registrado con ID: {contador_id}")
        contador_id += 1

    elif opcion == "2":
        if not equips:
            print("No hay equipos registrados.")
        else:
            for equipo in equips:
                print(f"ID: {equipo['id']} | Nombre: {equipo['nombre']} | Estado: {equipo['estado']}")
                print(f"Tipo: {equipo['tipo']} | Aula: {equipo['aula']} | Serie: {equipo['serie']}")
                print(f"Specs: {equipo['ram']}GB RAM - {equipo['disc']} - {equipo['so']}")

    elif opcion == "3":
        serie_buscar = input("Introduce el número de serie del equipo: ")
        encontrado = False
        for equipo in equips:
            if equipo["serie"] == serie_buscar:
                print(f"El estado actual de {equipo['nombre']} es: {equipo['estado']}")
                nuevo_estado = input("Introduce el nuevo estado: ")
                equipo["estado"] = nuevo_estado
                print("actualizado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("No se ha encontrado ningún equipo con ese número de serie.")

    elif opcion == "4":
        print("Función de modificación aún no implementada.")

    elif opcion == "5":
        print("Gestión de incidencias aún no implementada.")

    elif opcion == "0":
        print("Saliendo del programa... ¡Adiós!")
        break

    else:
        print("Opción no válida.")