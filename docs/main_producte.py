from lector import *

from producte_solucio import Producte

# from <primerCognomAlumne>_producte import Producte<PrimerCognomAlumne>

# Funcions que es fan servir en aquest programa.
def mostrar_tots_els_productes(llista_productes_rebuda):
    """
    Mostra tots els productes disponibles.
    :param productes: Llista de productes
    :return: No retorna res
    NOTA: cal que la classe Producte tingui el mètode mostrar() implementat
    """
    if not llista_productes_rebuda:
        print("No hi ha productes per mostrar.")
    else:
        print("\n--- LLISTA DE PRODUCTES ---")
        for i, producteActual2n in enumerate(llista_productes_rebuda):
            producteActual2n.mostrar_dades()


def seleccionar_producte(llista_productes_rebuda):
    """
    Permet seleccionar un producte de la llista.
    :param productes: Llista de productes
    :return: Producte seleccionat o None si no hi ha productes
    NOTA: cal que la classe Producte tingui el mètode torna_nom() implementat
    """
    if not llista_productes_rebuda:
        print("No hi ha productes per seleccionar.")
        return None

    print("\n--- SELECCIONA UN PRODUCTE ---")
    for i, prodAct in enumerate(llista_productes_rebuda):
        print(f"{i + 1}. {prodAct.torna_nom()}")

    while True:
        try:
            index = int(input("Número de producte: ")) - 1
            if 0 <= index < len(llista_productes_rebuda):
                return llista_productes_rebuda[index]
            else:
                print("Número de producte incorrecte.")
        except ValueError:
            print("Introdueix un número vàlid.")

# Program principal
if __name__ == "__main__":

    # Inicialització de variables
    llista_productes = []
    opcio = int()

    # Codi per entrar dos productes a la llista
    nomProductes = ["Llapis", "Bolígraf"]
    preuProductes = [7.0, 4.0]
    unitatsProductes = [15, 10]
    for i in range(0, len(nomProductes)):
        nou = Producte(nomProductes[i], preuProductes[i], unitatsProductes[i])
        llista_productes.append(nou)

    # Bucle principal del programa
    while True:
        opcio = mostrar_menu()

        match opcio:
            case 1:
                nom, preu, unitats = llegir_producte()
                nou = Producte(nom, preu, unitats)
                llista_productes.append(nou)
                print(f"Producte {nom} afegit correctament.")

            case 2:
                mostrar_tots_els_productes(llista_productes)

            case 3:
                producte = seleccionar_producte(llista_productes)
                if producte:
                    preu_vell = producte.preu
                    print(f"Preu antic: {preu_vell}")
                    nou_preu = demanar_decimal("Introdueix el nou preu: ")
                    producte.canviar_preu(nou_preu)

            case 4:
                producte = seleccionar_producte(llista_productes)
                if producte:
                    valoracio = demanar_enter("Introdueix una valoració (0 a 10): ")
                    producte.afegir_valoracio(valoracio)

            case 5:
                if not llista_productes:
                    print("No hi ha productes.")
                else:
                    print("\n--- MITJANES DE VALORACIÓ ---")
                    for producteActual2n in llista_productes:
                        print(f"{producteActual2n.torna_nom()}: ", end="")
                        producteActual2n.mostrar_valoracio_mitjana()

            case 0:
                print("Sortint del programa...")
                break

            case _:
                print("Opció no reconeguda.")

