import time # import time per fer pauses entre els atacs

from lluitador import Lluitador  # Importa la classe Lluitador

# Programa principal (main)
if __name__ == "__main__":
    # 1. Crear dos lluitadors
    lluitador1 = Lluitador("Ragnar")
    lluitador2 = Lluitador("Ezio")

    # 2. Bucle de combat fins que un perdi tota la vida
    torn = 0
    print("🗡️ COMENÇA EL COMBAT!\n")
    while lluitador1.esta_viu() and lluitador2.esta_viu():
        time.sleep(1)  # Petita pausa per fer-ho més visual
        if torn % 2 == 0:
            lluitador1.atacar(lluitador2)
        else:
            lluitador2.atacar(lluitador1)
        torn += 1

    # 3. Mostrar el guanyador
    guanyador = lluitador1 if lluitador1.esta_viu() else lluitador2
    print(f"🏆 El guanyador és {guanyador.nom} amb {guanyador.vida} punts de vida restants!")
