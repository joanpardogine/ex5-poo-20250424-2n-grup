class Llibre2:
    """
    Classe Llibre2 que representa un llibre amb atributs com el títol, l'autor,
    l'any de publicació i la quantitat d'exemplars disponibles.
    Atributs:
        titol (str): Títol del llibre.
        autor (str): Autor del llibre.
        any_publicacio (int): Any de publicació del llibre.
        quantitat_exemplars (int): Quantitat total d'exemplars disponibles.
        quantitat_en_prestec (int): Quantitat d'exemplars en préstec.
    Mètodes:
        mostrar_info(): Mostra la informació del llibre.
        prestar(): Presta un exemplar del llibre.
        retornar(): Retorna un exemplar del llibre.
        mateix_autor(altre_llibre): Comprova si l'autor és el mateix que
            l'autor d'un altre llibre.
    """

    # Atributs i constructor
    def __init__(self, _titol, _autor, _any_publicacio, _quantitat_exemplars):
        """
        Constructor de la classe Llibre2.
        :param _titol: Títol del llibre.
        :param _autor: Autor del llibre.
        :param _any_publicacio: Any de publicació del llibre.
        :param _quantitat_exemplars: Quantitat total d'exemplars disponibles.
        Aquesta funció inicialitza els atributs del llibre i estableix la
            quantitat en préstec a 0.
        """
        # Inicialitza els atributs del llibre
        # titol de tipus cadena (str)
        self.titol = _titol
        # autor de tipus cadena (str)
        self.autor = _autor
        # any_publicacio de tipus enter (int)
        self.any_publicacio = _any_publicacio
        # quantitat_exemplars de tipus enter (int)
        self.quantitat_exemplars = _quantitat_exemplars
        # quantitat_en_prestec de tipus enter (int)
        # Inicialitza la quantitat en préstec a 0
        # Aquesta variable s'incrementa quan es presta un llibre
        # i es decrementa quan es retorna un llibre
        self.quantitat_en_prestec = 0


    # Mètode per obtenir el títol del llibre
    def torna_titol(self):
        """
        Aquesta funció retorna el títol del llibre.
        :param: No rep cap valor
        :return: El títol del llibre.
        """
        # Retorna el títol del llibre
        return self.titol

    # Mètode per obtenir l'autor del llibre
    def torna_autor(self):
        """
        Aquesta funció retorna l'autor del llibre.
        :param: No rep cap valor
        :return: L'autor del llibre.
        """
        # Retorna l'autor del llibre
        return self.autor
    
    # Mètode per obtenir la disponibilitat del llibre
    def torna_disponibilitat(self):
        """
        Aquesta funció retorna la disponibilitat del llibre.
        :param: No rep cap valor
        :return: True si el llibre està disponible, False en cas contrari.
        """
        # Retorna la disponibilitat del llibre
        # Si el llibre està disponible, retorna True
        # Si el llibre no està disponible, retorna False
        return self.disponible

    # Mètode per modificar el títol del llibre
    def modificar_titol(self, nou_titol):
        """
        Aquesta funció modifica el títol del llibre.
        :param nou_titol: El nou títol del llibre.
        :return: No retorna cap valor
        """
        # Modifica el títol del llibre
        # Assigna el nou títol al llibre
        # Si el nou títol és una cadena buida, mostra un missatge d'error
        if not nou_titol:
            print("Error: El títol no pot ser buit.")
            return # Si el nou títol és buit, no es modifica i retorna none
        # Si el nou títol no és una cadena buida, assigna el nou títol al llibre
        self.titol = nou_titol

    # Mètode per modificar l'autor del llibre
    def modificar_autor(self, nou_autor):
        """
        Aquesta funció modifica l'autor del llibre.
        :param nou_autor: El nou autor del llibre.
        :return: No retorna cap valor
        """
        # Modifica l'autor del llibre
        # Assigna el nou autor al llibre
        # Si el nou autor és una cadena buida, mostra un missatge d'error
        if not nou_autor:
            print("Error: L'autor no pot ser buit.")
            return
        # Si el nou autor no és una cadena buida, assigna el nou autor al llibre
        self.autor = nou_autor

    # Mètode per modificar la disponibilitat del llibre
    def modificar_disponibilitat(self, nova_disponibilitat):
        """
        Aquesta funció modifica la disponibilitat del llibre.
        :param nova_disponibilitat: La nova disponibilitat
            del llibre (True o False).
        :return: No retorna cap valor
        """
        # Modifica la disponibilitat del llibre
        # Assigna la nova disponibilitat al llibre
        # Si la nova disponibilitat no és un valor booleà,
        #   mostra un missatge d'error
        if not isinstance(nova_disponibilitat, bool):
            print("Error: La disponibilitat ha de ser True o False.")
            return
        self.disponible = nova_disponibilitat

    def mostrar_info(self):
        """
        Aquesta funció mostra la informació del llibre, incloent el títol,
            l'autor, l'any de publicació, la quantitat total d'exemplars,
            la quantitat en préstec i la quantitat disponible.
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Calcula la quantitat d'exemplars disponibles
        # Exemplars disponibles = Quantitat total d'exemplars - Quantitat en préstec
        exemplars_disponibles = self.quantitat_exemplars - self.quantitat_en_prestec
        # Imprimeix la informació del llibre
        # El missatge inclou el títol, l'autor, l'any de publicació,
        # la quantitat total d'exemplars, la quantitat en préstec
        print(f"Títol: {self.titol} ({self.any_publicacio})")
        print(f"Autor: {self.autor}")
        print(f"Exemplars totals: {self.quantitat_exemplars}")
        print(f"En préstec: {self.quantitat_en_prestec}")
        print(f"Disponibles: {exemplars_disponibles}")
        print("-" * 30)

    def prestar(self):
        """
        Aquesta funció presta un exemplar del llibre.
        Si hi ha exemplars disponibles, incrementa la quantitat en préstec
            i imprimeix un missatge de confirmació.
        Si no hi ha exemplars disponibles, imprimeix un missatge d'error.
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Comprova si hi ha exemplars disponibles
        if self.quantitat_en_prestec < self.quantitat_exemplars:
            # Incrementa la quantitat en préstec
            self.quantitat_en_prestec += 1
            # Imprimeix un missatge de confirmació
            # El missatge inclou el títol del llibre
            # i indica que s'ha prestat un exemplar
            en_queden = self.quantitat_exemplars - self.quantitat_en_prestec
            print(f'S\'ha prestat un exemplar de "{self.titol}", i en queden {en_queden} exemplars.')
        # Si no hi ha exemplars disponibles
        else:
            # Imprimeix un missatge d'error
            print(f'No hi ha exemplars disponibles de "{self.titol}".')

    def retornar(self):
        """
        Aquesta funció retorna un exemplar del llibre.
        Si hi ha exemplars en préstec, decrementa la quantitat en préstec
            i imprimeix un missatge de confirmació.
        Si no hi ha exemplars en préstec, imprimeix un missatge d'error.
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Comprova si hi ha exemplars en préstec
        # Si hi ha exemplars en préstec,
        if self.quantitat_en_prestec > 0:
            # Decrementa la quantitat en préstec
            self.quantitat_en_prestec -= 1
            # i imprimeix un missatge de confirmació
            print(f'S\'ha retornat un exemplar de "{self.titol}".')
        # Si no hi ha exemplars en préstec, imprimeix un missatge d'error
        else:
            # Imprimeix un missatge d'error
            print(f'No hi ha cap exemplar de "{self.titol}" en préstec.')

    def mateix_autor(self, altre_llibre):
        """
        Aquesta funció comprova si l'autor del llibre és el mateix que
            l'autor d'un altre llibre.
        :param altre_llibre: Un altre llibre a comparar.
        :return: True si els autors són els mateixos, False en cas contrari.
        """
        # Comprova si l'autor del llibre és el mateix que l'autor
        #   d'un altre llibre
        # Si els autors són els mateixos, retorna True
        # Si no són els mateixos, retorna False
        return self.autor == altre_llibre.autor
