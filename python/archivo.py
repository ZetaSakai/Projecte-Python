# ==========================================
# AulaManager - Operació Aula Zero
# ==========================================

equips = []
contador_id = 1


def donar_alta():
    global contador_id

    print("\n--- DONAR D'ALTA EQUIP ---")

    tipus = input("Tipus (PC, Portàtil, Impressora, Switch, AP, Servidor): ")
    nom = input("Nom d'equip: ")
    aula = input("Aula: ")
    serie = input("Número de sèrie: ")
    so = input("Sistema operatiu: ")
    ram = input("RAM (ex: 16GB): ")
    disc = input("Disc (ex: 512GB SSD): ")
    estat = input("Estat (operatiu / avariat / reparació / baixa): ")
    ip = input("IP (opcional): ")
    mac = input("MAC (opcional): ")
    observacions = input("Observacions: ")

    equip = {
        "id": contador_id,
        "tipus": tipus,
        "nom": nom,
        "aula": aula,
        "serie": serie,
        "so": so,
        "ram": ram,
        "disc": disc,
        "estat": estat,
        "ip": ip,
        "mac": mac,
        "observacions": observacions
    }

    equips.append(equip)
    print(f"\n✅ Equip registrat amb ID {contador_id}")

    contador_id += 1


def mostrar_equips():
    print("\n--- LLISTAT D'EQUIPS ---")

    if len(equips) == 0:
        print("No hi ha equips registrats.")
        return

    for equip in equips:
        print("---------------------------------")
        for clau, valor in equip.items():
            print(clau, ":", valor)


def buscar_per_serie():
    serie_buscar = input("\nIntrodueix número de sèrie: ")

    for equip in equips:
        if equip["serie"] == serie_buscar:
            print("\nEquip trobat:")
            for clau, valor in equip.items():
                print(clau, ":", valor)
            return

    print("❌ No s'ha trobat cap equip amb aquest número de sèrie.")


# =========================
# MENÚ PRINCIPAL
# =========================

while True:
    print("\n===== AulaManager =====")
    print("1. Donar d'alta equip")
    print("2. Mostrar equips")
    print("3. Buscar per número de sèrie")
    print("4. Sortir")

    opcio = input("Escull una opció: ")

    if opcio == "1":
        donar_alta()
    elif opcio == "2":
        mostrar_equips()
    elif opcio == "3":
        buscar_per_serie()
    elif opcio == "4":
        print("Sortint del programa...")
        break
    else:
        print("Opció no vàlida.")