from llibre2 import Llibre2

# Funció per mostrar la informació dels llibres
def mostrar_tots_els_llibres(mida):
    """
    Aquesta funció mostra la informació de tots els llibres de la llista.
    :param: No rep cap valor
    :return: No retorna cap valor
    """

    # Imprimeix un missatge d'inici
    print("Llistat dels llibres")
    print("--------------------")
    pos = 0
    # Itera sobre la llista de llibres
    while (pos < mida):
        # i mostra la informació de cada llibre
        llibres[pos].mostrar_info()
        pos += 1

# Programa principal (main)
if __name__ == "__main__":
    # Crear llibres
    # Els llibres es creen amb el títol, l'autor, l'any de publicació i la quantitat d'exemplars
    llibre1 = Llibre2("Mecanoscrit del segon origen", "Manuel de Pedrolo", 1984, 3)
    llibre2 = Llibre2("La plaça del Diamant", "Mercè Rodoreda", 1962, 3)
    llibre3 = Llibre2("Llibre de les bèsties", "Ramon Llull", 1492, 2)
    llibre4 = Llibre2("Mirall trencat", "Mercè Rodoreda", 1962, 2)

    # Es crea una llista de llibres
    # Aquesta llista conté tots els llibres creats
    llibres = list()
    
    # Afegir llibres a la llista
    llibres.append(llibre1)
    llibres.append(llibre2)
    llibres.append(llibre3)
    llibres.append(llibre4)

    # Mostrar informació dels llibres 
    mostrar_tots_els_llibres(llibres.__len__())

    print("\nAccions:")
    
    print(f"\n\tEs presta un exemplar del llibre '{llibre1.torna_titol()}'")
    llibre1.prestar()

    print(f"\n\tEs tornar a prestar un exemplar del llibre '{llibre1.torna_titol()}'")
    llibre1.prestar()

    print(f"\n\tEs tornar a prestar un exemplar del llibre '{llibre1.torna_titol()}'")
    llibre1.prestar()

    print(f"\n\tEs tornar a prestar un exemplar del llibre '{llibre1.torna_titol()}'"
          f"\n\tpero ja no en queden exemplars disponibles!!")
    llibre1.prestar()  # Ja no en queden

    print(f"\n\tEs mostra la informació del llibre '{llibre1.torna_titol()}'")
    llibre1.mostrar_info()

    print(f"\n\tPer provar el mètode 'mateix_autor', es comparen els llibres 1, 2"
          f"\n\tEs farà servir la comanda llibre1.mateix_autor(llibre2) i serà False")
    # Es mostra la informació del llibre 1
    print(f"\nLlibre 1 (Es farà servir la comanda llibre1.mostrar_info())")
    llibre1.mostrar_info()
    # Es mostra la informació del llibre 2
    print(f"\nLlibre 2 (Es farà servir la comanda llibre2.mostrar_info())")
    llibre2.mostrar_info()


    print(f"El llibre 1 i el llibre 2 tenen el mateix autor? {llibre1.mateix_autor(llibre2)}")  # False

    print(f"\n\tPer tornar a provar el mètode 'mateix_autor', es comparen els llibres 2, 4" 
          f"\n\tEs farà servir la comanda llibre2.mateix_autor(llibre4) i serà True")
    print(f"\nLlibre 2 (Es farà servir la comanda llibre2.mostrar_info())")
    llibre2.mostrar_info()

    print(f"\nLlibre 4 (Es farà servir la comanda llibre4.mostrar_info())")
    llibre4.mostrar_info()

    print(f"El llibre 2 i el llibre 4 tenen el mateix autor? {llibre2.mateix_autor(llibre4)}")  # False
