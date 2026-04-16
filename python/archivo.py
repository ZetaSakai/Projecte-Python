import csv
import os
from datetime import datetime

equipos = []
contador_id = 1


if os.path.exists("equips.csv"):
    with open("equips.csv", "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fila["id"] = int(fila["id"]) # El ID debe ser un número
            equipos.append(fila)
    if equipos:
        contador_id = max(e["id"] for e in equipos) + 1
    print(f"Dades carregades correctament ({len(equipos)} equips).") [cite: 39]

while True:

    operativos = 0
    estropeados = 0
    reparacion = 0
    baja = 0
    
    for e in equipos:
        if e["estado"] == "operativo":
            operativos = operativos + 1
        elif e["estado"] == "estropeado":
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
    print("7) Cercar equipo") 
    print("8) Generar informe")
    print("0) Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        if len(equipos) >= 10:
            print("¡Error! No caben más equipos, el máximo son 10.")
        else:
            nombre = input("Nombre: ")
            aula = input("Aula: ")
            serie = input("Número de serie: ")
            while serie == "":
                serie = input("El número de serie es obligatorio: ")
            
            tipo = input("Tipo (PC/Portátil): ")
            so = input("Sistema operativo: ")
            ram = input("RAM: ")
            disc = input("Disco: ")

            estado = "operativo"
            
            equipo = {
                "id": contador_id, "nombre": nombre, "aula": aula, "serie": serie,
                "tipo": tipo, "so": so, "ram": ram, "disc": disc, "estado": estado,
                "incidencia": "", "tecnico": "", "estat_inc": ""
            }
            
            equipos.append(equipo)
            print(f"¡Hecho! ID: {contador_id}")
            contador_id += 1

    elif opcion == "2":
        if not equipos:
            print("No hay equipos.")
        else:
            for e in equipos:
                print(f"ID: {e['id']} | {e['nombre']} | {e['aula']} | {e['estado']}")

    elif opcion == "6":
        id_buscar = int(input("ID del equipo: "))
        for e in equipos:
            if e["id"] == id_buscar:
                accion = input("1) Nueva incidencia 2) Resolver incidencia: ")
                if accion == "1":
                    e["incidencia"] = input("¿Qué pasa?: ")
                    e["tecnico"] = input("Técnico: ")
                    e["estat_inc"] = "pendiente"
                    e["estado"] = "estropeado"
                elif accion == "2":

                    fecha = datetime.now().strftime("%Y-%m-%d")
                    linea = f"{fecha} | ID:{e['id']} | {e['nombre']} | {e['incidencia']} | Resuelta\n"
                    with open("historial.txt", "a") as h:
                        h.write(linea) [cite: 54]
                    
                    e["incidencia"] = ""
                    e["tecnico"] = ""
                    e["estat_inc"] = "resuelta"
                    e["estado"] = "operativo"
                    print("Incidencia resuelta y guardada en historial.txt")

    elif opcion == "7":
        busqueda = input("Nombre, aula o estado a buscar: ").lower()
        encontrados = False
        for e in equipos:
            if busqueda in e["nombre"].lower() or busqueda in e["aula"].lower() or busqueda in e["estado"].lower():
                print(f"ID: {e['id']} | {e['nombre']} | {e['estado']}")
                encontrados = True
        if not encontrados:
            print("No se ha encontrado nada.") [cite: 93]

    elif opcion == "8": 
        with open("informe.txt", "w") as f:
            f.write("--- INFORME AULA ZERO ---\n")
            f.write(f"Fecha: {datetime.now()}\n")
            f.write(f"Total equipos: {len(equipos)}\n")
            for e in equipos:
                f.write(f"ID: {e['id']} - {e['nombre']} - {e['estado']}\n")
        print("Informe generado en informe.txt") [cite: 144]

    elif opcion == "0":

        campos = ["id", "nombre", "aula", "serie", "tipo", "so", "ram", "disc", "estado", "incidencia", "tecnico", "estat_inc"]
        with open("equips.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(equipos)
        print("Dades guardades correctament. ¡Adiós!") [cite: 42]
        break