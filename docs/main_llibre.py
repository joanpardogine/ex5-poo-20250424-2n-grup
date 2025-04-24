from llibre import Llibre

# Funció per mostrar la informació dels llibres
def mostrar_tots_els_llibres():
    """
    Aquesta funció mostra la informació de tots els llibres de la llista.
    :param: No rep cap valor
    :return: No retorna cap valor
    """
    mida = 3
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
    llibre1 = Llibre("Mecanoscrit del segon origen", "Manuel de Pedrolo")
    llibre2 = Llibre("La plaça del Diamant", "Mercè Rodoreda")
    llibre3 = Llibre("Llibre de les bèsties", "Ramon Llull")

    llibres = list()

    llibres.append(llibre1)
    llibres.append(llibre2)
    llibres.append(llibre3)

    # Mostrar informació inicial
    mostrar_tots_els_llibres()

    print("\nAccions:")
    print(f"\n\tEs fa el préstec del llibre '{llibre1.torna_titol()}'")
    llibre1.prestar_llibre()
    print(f"\n\tEs fa el préstec del llibre '{llibre2.torna_titol()}'")
    llibre2.prestar_llibre()
    print(f"\n\tS'intentar torna a fer el préstec del llibre '{llibre2.torna_titol()}, que ja està prestat!'")
    llibre2.prestar_llibre()  # Intentar tornar a prestar-lo
    print(f"\n\tEs retorna el llibre '{llibre2.torna_titol()}'")
    llibre2.retornar_llibre()
    print(f"\n\tS'intentar retornar el llibre '{llibre3.torna_titol()}', que ja està disponible!")
    llibre3.retornar_llibre()  # Intentar retornar-lo si ja està disponible

    print()
    mostrar_tots_els_llibres()
