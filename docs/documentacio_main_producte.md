# Documentació del programa `main_producte.py` <ins>2n grup</ins>

Aquest programa permet gestionar una petita llista de productes mitjançant un menú d'opcions.

Cada producte té un **nom**, un **preu**, una quantitat d'**unitats** i una llista de valoracions.

---

## Estructura general del programa

## 1. Imports

```python
from lector import *
from producte import Producte
```

S'importen les funcions definides a **`lector.py`** i la classe **`Producte`** que es troba dins del fitxer **`producte.py`**.

Recordeu:

> #### - El fitxer **`<primerCognomAlumne>_producte.py`** és a on haureu de crear la vostra **classe** **`Producte<PrimerCognomAlumne>`**

<pre>
&lt;primerCognomAlumne>5e-examen-2n-grup/
├── main_producte.py
├── lector.py
└── &lt;primerCognomAlumne>_producte.py
</pre>

> [!WARNING]
> ### En aquest punt cal que modifiqueu la línia `from producte_solucio import Producte` amb el nom del vostre fitxer i el nom de la vostra classe.
>

Per exemple en el meu cas, _**Joan Pardo**_ seria:

- El fitxer tindria el nom **`pardo_producte.py`**, el nom de la **classe** que heu de crear **`ProductePardo`**.

<pre>
pardo5e-examen-2n-grup/
├── main_producte.py
├── lector.py
└── pardo_producte.py
</pre>

> [!WARNING]
>
> ### També caldrà que substituiu totes les cadenes de Producte, pel nom de la vostra **classe** **`Producte<PrimerCognomAlumne>`**
>

Per tant, cal modificar el nom de la **Classe** a tres següents línies del fitxer **`main_producte.py`**:

**1.** La línia actual:

```python
from producte import Producte
```

per la nova línia

```python
from pardo_producte import ProductePardo
```

**2.** La línia actual:

```python
nou = Producte(nomProductes[i], preuProductes[i], unitatsProductes[i])
```

per la nova línia

```python
nou = ProductePardo(nomProductes[i], preuProductes[i], unitatsProductes[i])
```

**3.** i la línia:

```python
nou = Producte(nom, preu, unitats)
```

per la nova línia

```python
nou = ProductePardo(nom, preu, unitats)
```

> [!WARNING]
> #### Evidentment sempre amb el nom la vostra **classe** **`Producte<PrimerCognomAlumne>`**
> ----

---

## 2. Funcions auxiliars

S'han creat els següents mètodes per fer-los servir en aquest mateix programa.

### Mètode `mostrar_tots_els_productes(llista_productes)`

Mostra per pantalla tots els productes de la llista, fent servir el mètode **`.mostrar()`** de cada objecte.

> [!WARNING]
> Per tant, si no heu desenvolupat el mètode **`.mostrar()`**, no funcionarà.
> ----

```python
def mostrar_tots_els_productes(llista_productes_rebuda):
    """
    Mostra tots els productes disponibles.
    :param productes: Llista de productes
    :return: No retorna res
    NOTA: cal que la classe Producte tingui el mètode mostrar() implementat
    """
    if not llista_productes_rebuda:
        print("No hi ha productes disponibles.")
    else:
        print("\n--- LLISTA DE PRODUCTES ---")
        for i, producteActual2n in enumerate(llista_productes_rebuda):
            producteActual2n.mostrar()
```

### Mètode `seleccionar_producte(llista_productes)`

Permet a l'usuari triar un producte de la llista mitjançant el seu número. Retorna l’objecte seleccionat.

```python
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
```

---

## 3. Inicialització de dades

S’inicialitzen dos productes per defecte per començar:

```python
nomProductes = ["Bolígraf", "Llapis"]
preuProductes = [7.0, 4.0]
unitatsProductes = [15, 10]
```

Aquests productes es creen amb la classe `Producte` i s’afegeixen a la llista principal `llista_productes`.

---

## 4. Bucle principal desenvolupat amb **`match`**

A cada iteració del bucle es mostra un menú i es gestiona l’opció escollida per l’usuari:

```python
opcio = mostrar_menu()

match opcio:
```

### Opcions del menú:

| Opció | Acció |
|-------|-------|
| `1` | Afegeix un nou producte a la llista |
| `2` | Mostra tots els productes |
| `3` | Canvia el preu d’un producte seleccionat |
| `4` | Afegeix una valoració a un producte |
| `5` | Mostra la mitjana de valoracions de tots els productes |
| `0` | Surt del programa |

---

<details><summary>Pitja per veure un exemple de funcionament</summary>

```
--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 2

--- LLISTA DE PRODUCTES ---
Del producte 'Bolígraf' que val 7.0€ hi ha 15 unitats.
Del producte 'Llapis' que val 4.0€ hi ha 10 unitats.

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 1
Introdueix el nom del producte: Escaire de 20 cm.
Introdueix el preu del producte: 12
Introdueix el nombre d'unitats: 4
Producte Escaire de 20 cm. afegit correctament.

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 2

--- LLISTA DE PRODUCTES ---
Del producte 'Bolígraf' que val 7.0€ hi ha 15 unitats.
Del producte 'Llapis' que val 4.0€ hi ha 10 unitats.
Del producte 'Escaire de 20 cm.' que val 12.0€ hi ha 4 unitats.

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 3

--- SELECCIONA UN PRODUCTE ---
1. Bolígraf
2. Llapis
3. Escaire de 20 cm.
Número de producte: 1
Preu antic: 7.0
Introdueix el nou preu: 4.8

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 2

--- LLISTA DE PRODUCTES ---
Del producte 'Bolígraf' que val 4.8€ hi ha 15 unitats.
Del producte 'Llapis' que val 4.0€ hi ha 10 unitats.
Del producte 'Escaire de 20 cm.' que val 12.0€ hi ha 4 unitats.

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 4

--- SELECCIONA UN PRODUCTE ---
1. Bolígraf
2. Llapis
3. Escaire de 20 cm.
Número de producte: 1
Introdueix una valoració (0 a 10): 9

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 4

--- SELECCIONA UN PRODUCTE ---
1. Bolígraf
2. Llapis
3. Escaire de 20 cm.
Número de producte: 1
Introdueix una valoració (0 a 10): 8

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 4

--- SELECCIONA UN PRODUCTE ---
1. Bolígraf
2. Llapis
3. Escaire de 20 cm.
Número de producte: 2
Introdueix una valoració (0 a 10): 10

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 5

--- MITJANES DE VALORACIÓ ---
Bolígraf: Valoració mitjana: 8.50
Llapis: Valoració mitjana: 10.00
Escaire de 20 cm.: No hi ha valoracions disponibles.

--- MENÚ BOTIGA ---
1. Afegir un producte
2. Mostrar tots els productes
3. Canviar el preu d'un producte
4. Afegir la valoració d'un producte
5. Mostrar la valoració mitjana de TOTS els productes
0. Sortir
Tria una opció: 0
Sortint del programa...
```
</details>
