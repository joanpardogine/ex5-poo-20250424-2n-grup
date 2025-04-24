# Enunciat de l'activitat avaluable - **Gestió d'una petita botiga** 

Cal desenvolupar un petit sistema per gestionar productes d'una botiga.

Cada producte té:

- un **`nom`** de tipus **`cadena`** (nom de l'atribut **`nom`**).
- un **`preu`** de tipus **`decimal`** (nom de l'atribut **`preu`**).
- una quantitat d'**`unitats disponibles`** de tipus **`enter`** (nom de l'atribut **`unitats`**).
- una llista de **`valoracions rebudes`** (nom de l'atribut **`valoracions`**). 
  - les valoracions seran de tipus **`enter`**,
  - i els valors estaran entre **`0`** a **`10`**, i
  - inicialment la llista estarà buida.

---

## Classe <ins>**`Producte<PrimerCognomAlumne>`**</ins>

Dins del fitxer **`<primerCognomAlumne>_producte.py`**, cal que creïs una classe anomenada **`Producte<PrimerCognomAlumne>`**.

> [!CAUTION]
>
> ### On **`<primerCognomAlumne>`** és el **primer cognom de l'alumne**, sense el <u>nom</u>, ni el <u>simbol **`<`**</u>, ni el <u>simbol **`>`**</u>.
>
> ### Cal que el nom final de la classe **`<primerCognomAlumne>`** segueixi el format **`CamelCase`**!
>
> Per exemple en el meu cas, **`Joan Pardo`**, seguint el format **`Producte<PrimerCognomAlumne>`** el nom de la classe seria **`ProductePardo`**

> [!WARNING]
> #### En el cas dels alumnes **Adrià Garcia Fernández**, i **Arnau Garcia Romero**, si us plau afegiu també les tres primeres lletres del segon cognom.
>
> | Alumne                     | Nom classe                         |
> |----------------------------|------------------------------------|
> | **Adrià Garcia Fernández**   | **`ProducteGarciaFer`** |
> | **Arnau Garcia Romero** | **`ProducteGarciaRom`** |


## Crea els següents mètodes a la classe <ins>**`Producte<PrimerCognomAlumne>`**</ins>

La classe <ins>**`Producte<PrimerCognomAlumne>`**</ins> cal que tingui els següents mètodes:

### Mètode 1: Constructor

- Crea el mètode **constructor** **`__init__()`** que rebi el **nom**, el **preu** i les **unitats**, inicialitzi els atributs **nom**, **preu** i **unitats**, amb els parametres el **_nom**, el **_preu** i les **_unitats** rebuts i que la llista de valoracions .

> [!TIP]
> #### Descripció que cal que aparegui dins del constructor
>
>```python
>   """
>   Constructor de la classe Producte.
>   Inicialitza el nom, preu i unitats del producte
>       i crea la llista de valoracions buida.
>   :param _nom: Nom del producte
>   :param _preu: Preu del producte
>   :param _unitats: Unitats disponibles del producte
>   :return: No retorna res
>   """
>```

### Mètode 2: **`mostrar_dades`**

- un **mètode** amb el nom **`mostrar_dades()`** que imprimeixi per pantalla la informació del producte de manera clara, seguint el següent format:

<pre>
Del producte 'Bolígraf' que val 0.80€ hi ha 10 unitats.
</pre>

> [!TIP]
> #### Descripció que cal que aparegui dins del mètode **`mostrar_dades()`**
>
>```python
>   """
>   Mostra les dades del producte.
>   Format: Del producte 'Bolígraf' que val 0.80€ hi ha 10 unitats.
>   :param No rep cap paràmetre
>   :return: No retorna res
>   """
>```

### Mètode 3: **`torna_nom`**

- un **mètode** amb el nom **`torna_nom(self)`**, que retornarà una cadena amb el nom del producte.

> [!TIP]
> #### Descripció que cal que aparegui dins del mètode **`torna_nom(self)`**
>
>```python
> """
> Retorna el nom del producte.
> :param No rep cap paràmetre
> :return: Nom del producte
> """
>

### Mètode 4: **`canviar_preu`**

- un **mètode** amb el nom **`canviar_preu(self, nou_preu)`**, per actualitzar el preu amb el valor donat com a paràmetre.

> [!TIP]
> #### Descripció que cal que aparegui dins del mètode **`canviar_preu(self, nou_preu)`**
>
>```python
>   """
>   Canvia el preu del producte pel valor passat com a paràmetre.
>   El preu ha de ser un valor positiu.
>   Mostra un missatge d'error si el preu no és vàlid.
>   :param nou_preu: Nou preu del producte
>   :return: No retorna res
>   """
> ```

### Mètode 5: **`afegir_valoracio`**

- un **mètode** amb el nom **`afegir_valoracio(self, puntuacio_rebuda)`**, per afegir una puntuació (int de 0 a 10) a la llista de valoracions.

> [!TIP]
> #### Descripció que cal que aparegui dins del mètode **`afegir_valoracio(self, puntuacio_rebuda)`**
>
>```python
>    """
>    Afegeix una valoració a la llista de valoracions.
>    La puntuació ha de ser un valor entre 0 i 10.
>    :param puntuacio_rebuda: Puntuació a afegir
>    :return: No retorna res
>    """
> ```

Cal fer servir les constants **`NOTA_MIN = 0`** i **`NOTA_MAX = 10`**.

```python
# Declaració de constants
NOTA_MIN = 0
NOTA_MAX = 10
```

### Mètode 6: **`torna_valoracio_mitjana`**

- un **mètode** amb el nom **`mostrar_valoracio_mitjana(self)`**, per calcular i mostrar la mitjana de les valoracions. I, si no hi ha cap valoració, qeu mostri un missatge adequat.

> [!TIP]
> #### Descripció que cal que aparegui dins del mètode **`mostrar_valoracio_mitjana(self)`**
>
>```python
> """
> Mostra la valoració mitjana de totes les valoracions.
> Si no hi ha valoracions, mostra un missatge indicant-ho.
> :param No rep cap paràmetre
> :return: No retorna res
> """
> ```

---

### [Documentació del programa `main_producte.py`](./documentacio_main_producte.md)