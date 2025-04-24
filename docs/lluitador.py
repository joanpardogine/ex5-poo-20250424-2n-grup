import random

class Lluitador:
    """
    Aquesta classe representa un lluitador en un combat.
    Atributs:
        nom (str): Nom del lluitador.
        vida (int): Punts de vida del lluitador.
    Mètodes:
        saludar(): Imprimeix un missatge de benvinguda.
        rebre_dany(_punts): Redueix els punts de vida del lluitador.
        atacar(altre_lluitador): Ataca un altre lluitador i li fa dany.
        mostrar_estat(): Mostra l'estat actual del lluitador.
    """

    # Atributs i constructor
    def __init__(self, _nom):
        """
        El constructor inicialitza els atributs de la classe
        i defineix el seu tipus
        El constructor rep un paràmetre: nom
        Aquesta funció inicialitza el nom del lluitador i
        li assigna 100 punts de vida.
            :param _nom: Nom del lluitador.
            :return: No retorna cap valor
        """
        # nom de tipus cadena (str)
        self.nom = _nom
        # vida de tipus enter (int)
        # Inicialitza la vida a 100
        self.vida = 100

    # Mètodes
    def saludar(self):
        """
        Aquesta funció imprimeix un missatge que indica que el lluitador està preparat per lluitar.
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Imprimeix un missatge de benvinguda
        # que inclou el nom del lluitador
        # i indica que està preparat per lluitar
        print(f"Soc {self.nom}, i estic preparat per lluitar!")

    def rebre_dany(self, _punts):
        """
        Aquesta funció redueix els punts de vida del lluitador amb els
            punts de dany rebuts.
        Si la vida és menor o igual a 0, imprimeix un missatge de derrota.
        Si la vida és superior a 0, imprimeix els punts de vida restants.
        Si els punts de dany són negatius, imprimeix un missatge d'error.
        :param _punts: Punts de dany rebuts.
        :return: No retorna cap valor
        """
        # Comprova si els punts de dany són negatius
        if _punts < 0:
            print("Error: No es poden rebre punts de dany negatius.")
            return
        # Redueix els punts de vida amb els punts
        #   de dany rebuts
        # Si la vida és menor o igual a 0, imprimeix un missatge de derrota
        if self.vida <= 0:
            print(f"{self.nom} ja ha estat derrotat!")
            return
        # Redueix els punts de vida amb els punts de dany rebuts
        self.vida -= _punts
        # Mostre una cadena que indica els punts de vida que ha rebut
        print(f"{self.nom} ha rebut {_punts} punts de dany.")

    def atacar(self, altre_lluitador):
        """
        Ataca un altre lluitador i li fa dany.
        Aquesta funció genera un valor aleatori entre 10 i 30
            per representar el dany causat.
        A continuació, redueix els punts de vida de l'altre
            lluitador amb el dany causat.
        Finalment, imprimeix un missatge que indica el dany causat.
        Si l'altre lluitador té 0 o menys punts de vida,
            imprimeix un missatge de derrota.
        :param altre_lluitador: L'altre lluitador que rep l'atac.
        :return: No retorna cap valor
        """
        # Genera un valor aleatori entre 10 i 30
        #   per representar el dany causat
        dany = random.randint(10, 30)
        # Mostra un missatge que indica el dany causat
        print(f"{self.nom} ataca {altre_lluitador.nom} "
              f"i li fa {dany} punts de dany.")
        # Redueix els punts de vida de l'altre lluitador
        #   amb el dany causat
        altre_lluitador.rebre_dany(dany)

    def mostrar_estat(self):
        """
        Aquesta funció imprimeix el nom i els punts de vida del lluitador.
        Si la vida és menor o igual a 0, imprimeix un missatge de derrota.
        Si la vida és superior a 0, imprimeix els punts de vida restants.
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Mostra l'estat actual del lluitador
        # Si la vida és menor o igual a 0, imprimeix
        #   un missatge de derrota
        if self.vida <= 0:
            print(f"{self.nom} ha estat derrotat!")
        else:
            # Si la vida és superior a 0, imprimeix el
            # nom i els punts de vida del lluitador
            print(f"{self.nom} té {self.vida} punts de vida.")
    
    def esta_viu(self):
        """
        Aquesta funció comprova si el lluitador està viu.
        :param: No rep cap valor
        :return: True si el lluitador està viu, False en cas contrari.
        """
        return self.vida > 0