# Definició de la classe Llibre
class Llibre:
    """
    Aquesta classe representa un llibre amb un títol, un autor i
        una disponibilitat.
    Atributs:
        titol (str): El títol del llibre.
        autor (str): L'autor del llibre.
        disponible (bool): Indica si el llibre està disponible (True) o
            no (False).
    Mètodes:
        torna_titol(): Retorna el títol del llibre.
        torna_autor(): Retorna l'autor del llibre.
        torna_disponibilitat(): Retorna la disponibilitat del llibre.
        modificar_titol(nou_titol): Modifica el títol del llibre.
        modificar_autor(nou_autor): Modifica l'autor del llibre.
        modificar_disponibilitat(nova_disponibilitat): Modifica la
            disponibilitat del llibre.
        mostrar_info(): Mostra la informació del llibre (títol, autor i
            disponibilitat).
        prestar_llibre(): Presta el llibre (canvia la disponibilitat a False).
        retornar_llibre(): Retorna el llibre (canvia la disponibilitat a True).
    """

    # Atributs i constructor
    # El constructor inicialitza els atributs titol, autor i disponible    
    def __init__(self, titol, autor):
        """
        Constructor de la classe Llibre.
        Aquesta funció inicialitza el títol, l'autor i la disponibilitat
            del llibre.
        :param titol: El títol del llibre.
        :param autor: L'autor del llibre.
        :return: No retorna cap valor
        """
        # titol de tipus cadena (str)
        self.titol = titol
        # autor de tipus cadena (str)
        self.autor = autor
        # disponible (valor inicial: True) de tipus booleà (bool)
        self.disponible = True  # Per defecte, el llibre està disponible

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

    # Mètode per mostrar la informació del llibre
    def mostrar_info(self):
        """
        Aquesta funció mostra la informació del llibre
            (títol, autor i disponibilitat).
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Inicialitza l'estat del llibre com a cadena buida
        # Si el llibre està disponible, l'estat és una cadena buida
        estat = ""
        # Si el llibre no està disponible, afegeix "no " a l'estat
        if not self.disponible:
            estat = "no "
        # Mostra la informació del llibre
        # Mostra el títol, l'autor i la disponibilitat del llibre
        print(f"El llibre '{self.titol}', de {self.autor}"
              f" {estat}està disponible.")

    # Mètode per prestar el llibre
    def prestar_llibre(self):
        """
        Aquesta funció presta el llibre (canvia la disponibilitat a False).
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Si el llibre està disponible, el mètode canvia l'estat
        #   a no disponible
        if self.disponible:
            # Canvia la disponibilitat a False
            self.disponible = False
            # Mostra un missatge que indica que el llibre ha estat prestat
            print(f'El llibre "{self.titol}" ha estat prestat.')
        # Si el llibre no està disponible, mostra un missatge que indica
        #   que ja està prestat
        else:
            # Mostra un missatge que indica que el llibre ja està prestat
            print(f'El llibre "{self.titol}" ja està prestat.')

    # Mètode per retornar el llibre
    def retornar_llibre(self):
        """
        Aquesta funció retorna el llibre (canvia la disponibilitat a True).
        :param: No rep cap valor
        :return: No retorna cap valor
        """
        # Si el llibre no està disponible, el mètode canvia l'estat a disponible
        if not self.disponible:
            self.disponible = True
            print(f'El llibre "{self.titol}" ha estat retornat.')
        # Si el llibre ja està disponible, mostra un missatge que indica
        #   que ja estava disponible
        else:
            # Mostra un missatge que indica que el llibre ja estava disponible
            print(f'El llibre "{self.titol}" ja estava disponible.')
