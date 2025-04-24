def llegir_producte():
    """
    Aquesta funció llegeix les dades d'un producte.
    :param No rep cap valor
    :return: Un tuple amb el nom, preu i unitats del producte
    """
    nom_llegit = demanar_cadena("Introdueix el nom del producte: ")
    preu_llegit = demanar_decimal("Introdueix el preu del producte: ")
    unitats_llegides = demanar_enter("Introdueix el nombre d'unitats: ")
    return nom_llegit, preu_llegit, unitats_llegides

def mostrar_menu():
    """
    Aquesta funció mostra el menú de la botiga i demana a l'usuari que triï una opció.
    :param No rep cap valor
    :return: L'opció triada per l'usuari
    """
    opcions = list()
    opcions.append("Afegir un producte")
    opcions.append("Mostrar tots els productes")
    opcions.append("Canviar el preu d'un producte")
    opcions.append("Afegir la valoració d'un producte")
    opcions.append("Mostrar la valoració mitjana de TOTS els productes")

    print("\n--- MENÚ BOTIGA ---")
    for i in range(0, len(opcions)):
        print(f"{i + 1}. {opcions[i]}")
    print("0. Sortir")
    while True:
        try:
            # Demana a l'usuari que triï una opció
            opcio = int(input("Tria una opció: "))
            if 0 <= opcio <= len(opcions):
                break
            else:
                print(f"Introdueix un número entre 0 i {len(opcions)}.")
        except ValueError:
            print("Introdueix un número vàlid.")
    return opcio

def demanar_cadena(cadenaDemanar):
    """
    Aquesta funció demana a l'usuari que introdueixi una cadena de text.
    :param cadenaDemanar: El text que es mostrarà a l'usuari
    :return: La cadena de text introduïda per l'usuari
    """
    resposta = ""
    while resposta.strip() == "":
        # Demana a l'usuari que introdueixi una cadena de text
        resposta = input(cadenaDemanar)
    return resposta

def demanar_enter(cadenaDemanar):
    """
    Aquesta funció demana a l'usuari que introdueixi un valor enter.
    :param cadenaDemanar: El text que es mostrarà a l'usuari
    :return: El valor enter introduït per l'usuari
    """
    while True:
        try:
            # Demana a l'usuari que introdueixi un valor enter
            # i intenta convertir-lo a un enter
            valor = int(input(cadenaDemanar))
            # Comprova si el valor és un enter vàlid
            if valor < 0:
                print("El valor ha de ser un enter positiu.")
                continue
            # Retorna el valor enter introduït
            return valor
        except ValueError:
            # Si no es pot convertir a enter, mostra un missatge d'error
            # i torna a demanar l'entrada
            print("Introdueix un valor enter vàlid.")

def demanar_decimal(cadenaDemanar):
    """
    Aquesta funció demana a l'usuari que introdueixi un valor decimal.
    :param cadenaDemanar: El text que es mostrarà a l'usuari
    :return: El valor decimal introduït per l'usuari
    """
    while True:
        try:
            # Demana a l'usuari que introdueixi un valor decimal
            # i intenta convertir-lo a un float
            valor = float(input(cadenaDemanar))
            # Comprova si el valor és un decimal vàlid
            if valor < 0:
                print("El valor ha de ser un decimal positiu.")
                continue
            # Retorna el valor decimal introduït
            return valor
        except ValueError:
            # Si no es pot convertir a float, mostra un missatge d'error
            # i torna a demanar l'entrada
            print("Introdueix un valor decimal vàlid.")
