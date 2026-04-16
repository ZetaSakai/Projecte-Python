import csv
import os
from datetime import datetime

equipos = []
contador_id = 1

# --- 1: CARREGAR DADES (PERSISTÈNCIA) ---
# Al principi, mirem si el fitxer ja existeix per no perdre el que teníem
if os.path.exists("equips.csv"):
    with open("equips.csv", "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Convertim l'ID a número perquè es llegeix com a text
            fila["id"] = int(fila["id"])
            equipos.append(fila)
    
    if equipos:
        # Busquem l'ID més alt per saber per quin número seguir
        for e in equipos:
            if e["id"] >= contador_id:
                contador_id = e["id"] + 1
    print(f"Dades carregades correctament ({len(equipos)} equips).")

while True:
    # Comptadors per al resum de l'inici
    operatius = 0
    avariats = 0
    reparacio = 0
    baja = 0
    
    for e in equipos:
        if e["estado"] == "operatiu":
            operatius = operatius + 1
        elif e["estado"] == "avariat":
            avariats = avariats + 1
        elif e["estado"] == "reparacio":
            reparacio = reparacio + 1
        elif e["estado"] == "baja":
            baja = baja + 1

    print("\n--- RESUM DEL AULA ---")
    print(f"Total equips: {len(equipos)} | Operatius: {operatius} | Avariats: {avariats}")

    print("\n=== AulaManager ===") 
    print("1) Registrar equip") 
    print("2) Llistar tots els equips") 
    print("3) Consultar equip") 
    print("4) Canviar estat") 
    print("5) Modificar dades") 
    print("6) Gestionar incidència")
    print("7) Cercar equip")
    print("8) Generar informe")
    print("0) Sortir")

    opcio = input("\nTria una opció: ")

    if opcio == "1": # OPCIÓ 1: REGISTRAR
        if len(equipos) >= 10:
            print("Error! El màxim són 10 equips.")
        else:
            nom = input("Nom del equip: ")
            aula = input("Aula: ")
            serie = input("Número de sèrie: ")
            tipus = input("Tipus (PC/Portàtil): ")
            so = input("Sistema Operatiu: ")
            ram = input("RAM: ")
            disc = input("Disc: ")
            
            nou_equip = {
                "id": contador_id, "nom": nom, "aula": aula, "serie": serie,
                "tipus": tipus, "so": so, "ram": ram, "disc": disc,
                "estado": "operatiu", "ip": "", "mac": "", "obs": "",
                "incidencia": "", "tecnic": "", "estat_inc": ""
            }
            equipos.append(nou_equip)
            print(f"Equip guardat amb ID: {contador_id}")
            contador_id = contador_id + 1

    elif opcio == "2": # OPCIÓ 2: LLISTAR
        if len(equipos) == 0:
            print("No hi ha equips.")
        else:
            print(f"{'ID':<3} | {'Nom':<15} | {'Aula':<15} | {'Estat':<10}")
            for e in equipos:
                print(f"{e['id']:<3} | {e['nom']:<15} | {e['aula']:<15} | {e['estado']:<10}")

    elif opcio == "3": # OPCIÓ 3: CONSULTAR
        id_buscat = int(input("ID de l'equip a consultar: "))
        trobat = False
        for e in equipos:
            if e["id"] == id_buscat:
                print("\n--- INFORMACIÓ DE L'EQUIP ---")
                print(f"ID: {e['id']} | Nom: {e['nom']} | Aula: {e['aula']}")
                print(f"Estat: {e['estado']} | Sèrie: {e['serie']}")
                print(f"SO: {e['so']} | RAM: {e['ram']} | Disc: {e['disc']}")
                print(f"Incidència: {e['incidencia'] if e['incidencia'] else 'Cap'}")
                print(f"Tècnic: {e['tecnic']} | Estat Incidència: {e['estat_inc']}")
                trobat = True
                break
        if not trobat:
            print("ID no trobat.")

    elif opcio == "4": # OPCIÓ 4: CANVIAR ESTAT
        id_buscat = int(input("ID de l'equip: "))
        trobat = False
        for e in equipos:
            if e["id"] == id_buscat:
                e["estado"] = input("Nou estat (operatiu/avariat/reparacio/baja): ")
                print("Estat actualitzat.")
                trobat = True
                break
        if not trobat:
            print("ID no trobat.")

    elif opcio == "5": # OPCIÓ 5: MODIFICAR
        id_buscat = int(input("ID de l'equip a modificar: "))
        trobat = False
        for e in equipos:
            if e["id"] == id_buscat:
                e["nom"] = input("Nou nom: ")
                e["aula"] = input("Nova aula: ")
                e["so"] = input("Nou SO: ")
                print("Dades actualitzades.")
                trobat = True
                break
        if not trobat:
            print("ID no trobat.")

    elif opcio == "6": # OPCIÓ 6: GESTIONAR INCIDÈNCIA
        id_buscat = int(input("ID de l'equip: "))
        trobat = False
        for e in equipos:
            if e["id"] == id_buscat:
                trobat = True
                print("1) Nova incidència | 2) Marcar com a resolta")
                accio = input("Què vols fer?: ")
                
                if accio == "1":
                    e["incidencia"] = input("Descripció del error: ")
                    e["tecnic"] = input("Nom del tècnic: ")
                    e["estat_inc"] = "pendent"
                    e["estado"] = "avariat"
                    print("Incidència registrada.")
                
                elif accio == "2":
                    # FASE 2: HISTORIAL - Guardem abans de borrar la incidencia
                    ara = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    linea_hist = f"[{ara}] ID:{e['id']} Equip:{e['nom']} | Incidència:{e['incidencia']} Tècnic:{e['tecnic']} | Resolta\n"
                    
                    with open("historial.txt", "a") as h:
                        h.write(linea_hist)
                    
                    # Netegem els camps de incidència de l'equip
                    e["incidencia"] = ""
                    e["tecnic"] = ""
                    e["estat_inc"] = ""
                    e["estado"] = "operatiu"
                    print("Incidència resolta i arxivada a historial.txt")
        if not trobat:
            print("ID no trobat.")

    elif opcio == "7": # OPCIÓ 7: CERCA D'EQUIPS
        print("Cercar per: 1) Nom | 2) Estat | 3) Aula")
        criteri = input("Tria criteri: ")
        busqueda = input("Text a buscar: ").lower()
        trobats = 0
        
        for e in equipos:
            match = False
            if criteri == "1" and busqueda in e["nom"].lower(): match = True
            elif criteri == "2" and busqueda == e["estado"].lower(): match = True
            elif criteri == "3" and busqueda == e["aula"].lower(): match = True
            
            if match:
                print(f"ID:{e['id']} | {e['nom']} | {e['aula']} | {e['estado']}")
                trobats = trobats + 1
        
        if trobats == 0:
            print("No s'han trobat resultats.")

    elif opcio == "8": # OPCIÓ 8: GENERAR INFORME
        with open("informe.txt", "w") as f:
            f.write("INFORME D'ESTAT AULA ZERO\n")
            f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"RESUM GLOBAL\nTotal equips: {len(equipos)}\nOperatius: {operatius}\nAvariats: {avariats}\n")
            f.write("\nDETALL D'EQUIPS\n")
            for e in equipos:
                f.write(f"ID: {e['id']} - Nom: {e['nom']} - Estat: {e['estado']}\n")
            f.write("\nINCIDÈNCIES ACTIVES\n")
            for e in equipos:
                if e["estat_inc"] == "pendent":
                    f.write(f"Equip: {e['nom']} | {e['incidencia']} | Tècnic: {e['tecnic']} | PENDENT\n")
        print("Informe generat correctament: informe.txt")

    elif opcio == "0": # OPCIÓ 0: SORTIR I GUARDAR
        # Guardem tot al CSV abans de tancar
        camps = ["id", "nom", "aula", "serie", "tipus", "so", "ram", "disc", "estado", "ip", "mac", "obs", "incidencia", "tecnic", "estat_inc"]
        with open("equips.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=camps)
            escritor.writeheader()
            escritor.writerows(equipos)
        print("Dades guardades correctament a equips.csv. Adéu!")
        break