
NOTA_MIN = 0
NOTA_MAX = 10

class Productegalvez:
    """
    Classe que representa un producte d'una botiga.
    """

    def __init__(self, _nom, _preu, _unitats):
        """
        Constructor de la classe Producte.
        Inicialitza el nom, preu i unitats del producte
            i crea la llista de valoracions buida.
        :param _nom: Nom del producte
        :param _preu: Preu del producte
        :param _unitats: Unitats disponibles del producte
        :return: No retorna res
        """
        self.nom = _nom
        self.preu = _preu
        self.unitats = _unitats
        self.valoracions = []

    def mostrar_dades(self):
        """
        Mostra les dades del producte.
        Format: Del producte 'Bolígraf' que val 0.80€ hi ha 10 unitats.
        :param No rep cap paràmetre
        :return: No retorna res
        """
        print(f"Del producte '{self.nom}' que val {self.preu:.2f}€ hi ha {self.unitats} unitats.")

    def torna_nom(self):
        """
        Retorna el nom del producte.
        :param No rep cap paràmetre
        :return: Nom del producte
        """
        return self.nom

    def canviar_preu(self, nou_preu):
        """
        Canvia el preu del producte pel valor passat com a paràmetre.
        El preu ha de ser un valor positiu.
        Mostra un missatge d'error si el preu no és vàlid.
        :param nou_preu: Nou preu del producte
        :return: No retorna res
        """
        if nou_preu > 0:
            self.preu = nou_preu
        else:
            print("Error: El preu ha de ser un valor positiu.")

    def afegir_valoracio(self, puntuacio_rebuda):
        """
        Afegeix una valoració a la llista de valoracions.
        La puntuació ha de ser un valor entre 0 i 10.
        :param puntuacio_rebuda: Puntuació a afegir
        :return: No retorna res
        """
        if NOTA_MIN <= puntuacio_rebuda <= NOTA_MAX:
            self.valoracions.append(puntuacio_rebuda)
        else:
            print(f"Error: la puntuació ha de ser entre {NOTA_MIN} i {NOTA_MAX}.")

    def mostrar_valoracio_mitjana(self):
        """
        Mostra la valoració mitjana de totes les valoracions.
        Si no hi ha valoracions, mostra un missatge indicant-ho.
        :param No rep cap paràmetre
        :return: No retorna res
        """
        if len(self.valoracions) == 0:
            print("Aquest producte no té valoracions.")
        else:
            mitjana = sum(self.valoracions) / len(self.valoracions)
            print(f"La valoració mitjana del producte és: {mitjana:.2f}")

