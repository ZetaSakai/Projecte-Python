# --- CONFIGURACIÓN INICIAL ---
equips = []          # Donde guardaremos todos los equipos
contador_id = 1      # El número que le daremos al primer equipo 

while True:
    # Antes de mostrar el menú, contamos cuántos hay de cada estado
    operatius = 0
    avariats = 0
    reparacio = 0
    baixa = 0
    
    for e in equips:
        if e["estado"] == "operatiu":
            operatius = operatius + 1
        elif e["estado"] == "avariat":
            avariats = avariats + 1
        elif e["estado"] == "reparacio":
            reparacio = reparacio + 1
        elif e["estado"] == "baixa":
            baixa = baixa + 1

    # Mostramos el resumen
    print("\n--- RESUM DE L'AULA ---")
    print(f"Total equips: {len(equips)}")
    print(f"Operatius:    {operatius}")
    print(f"Avariats:     {avariats}")
    print(f"En reparació: {reparacio}")
    print(f"De baixa:     {baixa}")

    # --- EL MENÚ PRINCIPAL ---
    print("\n=== AulaManager ===")
    print("1) Registrar equip")
    print("2) Llistar tots els equips")
    print("3) Consultar equip")
    print("4) Canviar estat")
    print("5) Modificar dades")
    print("6) Gestionar incidencia")
    print("0) Sortir")

    opcion = input("\nElige una opción: ")

    # --- OPCIÓN 1: AÑADIR EQUIPO ---
    if opcion == "1":
        # Primero miramos si la lista ya está llena (máximo 10)
        if len(equips) >= 10:
            print("¡Error! No caben más equipos, el máximo son 10.")
        else:
            # Pedimos los datos básicos
            tipo = input("Tipo: ")
            nombre = input("Nombre: ")
            aula = input("Aula: ")
            
            # Obligamos a que pongan el número de serie (si está vacío, se repite)
            serie = input("Número de serie: ")
            while serie == "":
                serie = input("El número de serie es obligatorio: ")

            so = input("Sistema operativo: ")
            ram = input("RAM (ej: 8GB): ")
            disc = input("Disco: ")

            # Validamos el estado para que no escriban cualquier cosa
            estados_ok = ["operatiu", "avariat", "reparacio", "baixa"]
            estado = input("Estado (operatiu/avariat/reparacio/baixa): ")
            while estado not in estados_ok:
                estado = input("Error. Escribe uno de estos: operatiu, avariat, reparacio o baixa: ")

            # Datos de la avería
            incidencia = input("¿Qué le pasa? (si no tiene nada, déjalo vacío): ")
            tecnico = input("Técnico que lo arregla: ")
            estat_inc = input("Estado de la incidencia (pendent/resolta): ")

            # Guardamos todo en una "ficha" (diccionario)
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
            
            # Metemos la ficha en la mochila y sumamos 1 al siguiente ID
            equips.append(equipo)
            print(f"¡Hecho! Equipo guardado con el ID: {contador_id}")
            contador_id += 1

    # --- OPCIÓN 2: LISTA RÁPIDA (TABLA) ---
    elif opcion == "2":
        if len(equips) == 0:
            print("No hay ningún equipo todavía.")
        else:
            # Dibujamos los títulos de la tabla
            print(f"\n{'ID':<3} | {'Nom':<15} | {'Aula':<15} | {'Estat':<10}")
            print("-" * 55)
            # Imprimimos una fila por cada equipo que tengamos
            for e in equips:
                print(f"{e['id']:<3} | {e['nombre']:<15} | {e['aula']:<15} | {e['estado']:<10}")

    # --- OPCIÓN 3: VER TODO SOBRE UN EQUIPO ---
    elif opcion == "3":
        id_buscar = int(input("Dime el ID del equipo: "))
        encontrado = False
        
        for e in equips:
            # Si el ID coincide, mostramos todos sus detalles ordenados
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

    # --- OPCIÓN 4: CAMBIAR SOLO EL ESTADO ---
    elif opcion == "4":
        id_buscar = int(input("ID del equipo a cambiar estado: "))
        encontrado = False
        for e in equips:
            if e["id"] == id_buscar:
                nuevo = input("Pon el nuevo estado (operatiu/avariat/etc): ")
                e["estado"] = nuevo
                print("Estado actualizado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("ID no encontrado.")

    # --- OPCIÓN 6: REGISTRAR AVERÍA RÁPIDA ---
    elif opcion == "6":
        id_buscar = int(input("ID del equipo con problemas: "))
        encontrado = False
        for e in equips:
            if e["id"] == id_buscar:
                e["incidencia"] = input("¿Qué se ha roto?: ")
                e["estado"] = "avariat"  # Si hay incidencia, el estado cambia solo
                e["estat_inc"] = "pendent"
                print("Incidencia guardada y equipo marcado como 'avariat'.")
                encontrado = True
                break
        if not encontrado:
            print("ID no encontrado.")

    # --- OPCIÓN 0: SALIR ---
    elif opcion == "0":
        print("Cerrando programa... ¡Adiós!Guarra")
        break

    else:
        print("Esa opción no existe, elige un número del menú.")