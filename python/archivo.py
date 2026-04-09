equipos = []
contador_id = 1

while True:
    operativos = 0
    estropeados = 0
    reparacion = 0
    baja = 0
    
    for e in equipos:
        if e["estado"] == "operativos":
            operativos = operativos + 1
        elif e["estado"] == "estropeados":
            estropeados = estropeados + 1
        elif e["estado"] == "reparacion":
            reparacion = reparacion + 1
        elif e["estado"] == "baja":
            baja = baja + 1

    print("\n--- RESUMEN DEL AULA ---")
    print(f"Total equipos:      {len(equipos)}")
    print(f"Operativos:     {operativos}")
    print(f"Estropeados:        {estropeados}")
    print(f"En reparacion:      {reparacion}")
    print(f"De baja:        {baja}")

    print("\n=== AulaManager ===") 
    print("1) Registrar equipo") 
    print("2) Listar todos los equipos") 
    print("3) Consultar equipo") 
    print("4) Cambiar estado") 
    print("5) Modificar datos") 
    print("6) Gestionar incidencia") 
    print("0) Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        if len(equipos) >= 10:
            print("¡Error! No caben más equipos, el máximo son 10.")
        else:
            tipo = input("Tipo: ")
            nombre = input("Nombre: ")
            aula = input("Aula: ")
            
            serie = input("Número de serie: ")
            while serie == "":
                serie = input("El número de serie es obligatorio: ")

            so = input("Sistema operativo: ")
            ram = input("RAM (ej: 8GB): ")
            disc = input("Disco: ")

            estados_ok = ["operativo", "estropeado", "reparacion", "baja"]
            estado = input("Estado (operativo/estropeado/reparacion/baja): ")
            while estado not in estados_ok:
                estado = input("Error. Escribe uno de estos: operativo, estropeado, reparacion o baja: ")

            incidencia = input("¿Qué le pasa? (si no tiene nada, déjalo vacío): ")
            tecnico = input("Técnico que lo arregla: ")
            estat_inc = input("Estado de la incidencia (pendiente/resuelta): ")

            equipo = {
                "id": contador_id,
                "nombre": nombre,
                "aula": aula,
                "estado": estado,
                "so": so,
                "ram": ram,
                "disc": disc,
                "incidencia": incidencia,
                "tecnico": tecnico,
                "estat_inc": estat_inc
            }
            
            equipos.append(equipo)
            print(f"¡Hecho! Equipo guardado con el ID: {contador_id}")
            contador_id += 1

    elif opcion == "2":
        if len(equipos) == 0:
            print("No hay ningún equipo todavía.")
        else:
            print(f"\n{'ID':<3} | {'nombre':<15} | {'Aula':<15} | {'Estado':<10}")
            print("-" * 55)
            for e in equipos:
                print(f"{e['id']:<3} | {e['nombre']:<15} | {e['aula']:<15} | {e['estado']:<10}")

    elif opcion == "3":
        id_buscar = int(input("Dime el ID del equipo: "))
        encontrado = False
        
        for e in equipos:
            if e["id"] == id_buscar:
                print("\n--- INFORMACIÓ DE L'EQUIP ---")
                print(f"ID: {e['id']}")
                print(f"Nom: {e['nombre']}")
                print(f"Aula: {e['aula']}")
                print(f"Estat: {e['estado']}")
                print(f"\nSistema operatiu: {e['so']}")
                print(f"RAM: {e['ram']}")
                print(f"Disc: {e['disc']}")
                print(f"\nIncidència: {e['incidencia'] if e['incidencia'] else 'Cap'}")
                print(f"Tècnic: {e['tecnico']}")
                print(f"Estat incidència: {e['estat_inc']}")
                encontrado = True
                break
        
        if not encontrado:
            print("Error: Ese ID no existe en la lista.")

    elif opcion == "4":
        id_buscar = int(input("ID del equipo a cambiar estado: "))
        encontrado = False
        for e in equipos:
            if e["id"] == id_buscar:
                nuevo = input("Pon el nuevo estado (operativo/estropeado/etc): ")
                e["estado"] = nuevo
                print("Estado actualizado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("ID no encontrado.")

    elif opcion == "5":
            id_buscar = int(input("Introduce el ID del equipo que quieres modificar: "))
            encontrado = False
            for e in equipos:
                if e["id"] == id_buscar:
                    print(f"Modificando equipo: {e['nombre']}")
                    e["nombre"] = input("Nuevo nombre: ")
                    e["aula"] = input("Nueva aula: ")
                    e["so"] = input("Nuevo sistema operativo: ")
                    
                    print("¡Datos actualizados correctamente!")
                    encontrado = True
                    break
            if not encontrado:
                print("Error: Ese ID no existe.")

    elif opcion == "6":
        id_buscar = int(input("ID del equipo con problemas: "))
        encontrado = False
        for e in equipos:
            if e["id"] == id_buscar:
                e["incidencia"] = input("¿Qué se ha roto?: ")
                e["estado"] = "estropeado"
                e["estat_inc"] = "pendiente"
                print("Incidencia guardada y equipo marcado como 'estropeado'.")
                encontrado = True
                break
        if not encontrado:
            print("ID no encontrado.")

    elif opcion == "0":
        print("Cerrando programa... ¡Adiós!")
        break

    else:
        print("Esa opción no existe, elige un número del menú.")