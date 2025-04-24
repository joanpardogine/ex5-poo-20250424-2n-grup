# Teoria que hem donat a classe

A classe hem vist els següents exemples:

## La classe **`Lluitador`**

La classe **`Lluitador`** que està definida en el fitxer [**`lluitador.py`**](./lluitador.py), i que el programa **`MainLluitador`** del fitxer [**`main_lluitador.py`**](./main_lluitador.py) fa servir per comprovar que tot és correcte.

I un exemple d'una possible execució seria:

<pre>
🗡️ COMENÇA EL COMBAT!

Ragnar ataca Ezio i li fa 17 punts de dany.
Ezio ha rebut 17 punts de dany.
Ezio ataca Ragnar i li fa 16 punts de dany.
Ragnar ha rebut 16 punts de dany.
Ragnar ataca Ezio i li fa 25 punts de dany.
Ezio ha rebut 25 punts de dany.
Ezio ataca Ragnar i li fa 27 punts de dany.
Ragnar ha rebut 27 punts de dany.
Ragnar ataca Ezio i li fa 10 punts de dany.
Ezio ha rebut 10 punts de dany.
Ezio ataca Ragnar i li fa 10 punts de dany.
Ragnar ha rebut 10 punts de dany.
Ragnar ataca Ezio i li fa 15 punts de dany.
Ezio ha rebut 15 punts de dany.
Ezio ataca Ragnar i li fa 30 punts de dany.
Ragnar ha rebut 30 punts de dany.
Ragnar ataca Ezio i li fa 14 punts de dany.
Ezio ha rebut 14 punts de dany.
Ezio ataca Ragnar i li fa 17 punts de dany.
Ragnar ha rebut 17 punts de dany.
</pre>

## La classe **`Llibre`**

La classe **`Llibre`** que està definida en el fitxer [**`llibre.py`**](./llibre.py), i que el programa **`MainLlibre`** del fitxer [**`main_llibre.py`**](./main_llibre.py) fa servir per comprovar que tot és correcte.

I un exemple d'una possible execució del fitxer [**`main_llibre.py`**](./main_llibre.py) seria:

<pre>
Llistat dels llibres
--------------------
El llibre 'Mecanoscrit del segon origen', de Manuel de Pedrolo està disponible.
El llibre 'La plaça del Diamant', de Mercè Rodoreda està disponible.
El llibre 'Llibre de les bèsties', de Ramon Llull està disponible.

Accions:

        Es presta el llibre 'Mecanoscrit del segon origen'
El llibre "Mecanoscrit del segon origen" ha estat prestat.

        Es presta el llibre 'La plaça del Diamant'
El llibre "La plaça del Diamant" ha estat prestat.

        S'intentar tornar a prestar el llibre 'La plaça del Diamant, que ja està prestat!'
El llibre "La plaça del Diamant" ja està prestat.

        Es retorna el llibre 'La plaça del Diamant'
El llibre "La plaça del Diamant" ha estat retornat.

        S'intentar retornar el llibre 'La plaça del Diamant', que ja està disponible!
El llibre "Llibre de les bèsties" ja estava disponible.

Llistat dels llibres
--------------------
El llibre 'Mecanoscrit del segon origen', de Manuel de Pedrolo no està disponible.
El llibre 'La plaça del Diamant', de Mercè Rodoreda està disponible.
El llibre 'Llibre de les bèsties', de Ramon Llull està disponible.
</pre>

## La classe **`Llibre2`**

La classe **`Llibre2`** que està definida en el fitxer [**`llibre2.py`**](./llibre2.py), i que el programa **`MainLlibre2`** del fitxer **`main_llibre2.py`** fa servir per comprovar que tot és correcte.

L'execució del fitxer [**`main_llibre2.py`**](./main_llibre2.py) és:

<pre>
Llistat dels llibres
--------------------
Títol: Mecanoscrit del segon origen (1984)
Autor: Manuel de Pedrolo
Exemplars totals: 3
En préstec: 0
Disponibles: 3
------------------------------
Títol: La plaça del Diamant (1962)
Autor: Mercè Rodoreda
Exemplars totals: 3
En préstec: 0
Disponibles: 3
------------------------------
Títol: Llibre de les bèsties (1492)
Autor: Ramon Llull
Exemplars totals: 2
En préstec: 0
Disponibles: 2
------------------------------
Títol: Mirall trencat (1962)
Autor: Mercè Rodoreda
Exemplars totals: 2
En préstec: 0
Disponibles: 2
------------------------------

Accions:

        Es presta un exemplar del llibre 'Mecanoscrit del segon origen'
S'ha prestat un exemplar de "Mecanoscrit del segon origen", i en queden 2 exemplars.

        Es tornar a prestar un exemplar del llibre 'Mecanoscrit del segon origen'
S'ha prestat un exemplar de "Mecanoscrit del segon origen", i en queden 1 exemplars.

        Es tornar a prestar un exemplar del llibre 'Mecanoscrit del segon origen'
S'ha prestat un exemplar de "Mecanoscrit del segon origen", i en queden 0 exemplars.

        Es tornar a prestar un exemplar del llibre 'Mecanoscrit del segon origen'
        pero ja no en queden exemplars disponibles!!
No hi ha exemplars disponibles de "Mecanoscrit del segon origen".

        Es mostra la informació del llibre 'Mecanoscrit del segon origen'
Títol: Mecanoscrit del segon origen (1984)
Autor: Manuel de Pedrolo
Exemplars totals: 3
En préstec: 3
Disponibles: 0
------------------------------

        Per provar el mètode 'mateix_autor', es comparen els llibres 1, 2
        Es farà servir la comanda llibre1.mateix_autor(llibre2) i serà False

Llibre 1 (Es farà servir la comanda llibre1.mostrar_info())
Títol: Mecanoscrit del segon origen (1984)
Autor: Manuel de Pedrolo
Exemplars totals: 3
En préstec: 3
Disponibles: 0
------------------------------

Llibre 2 (Es farà servir la comanda llibre2.mostrar_info())
Títol: La plaça del Diamant (1962)
Autor: Mercè Rodoreda
Exemplars totals: 3
En préstec: 0
Disponibles: 3
------------------------------
El llibre 1 i el llibre 2 tenen el mateix autor? False

        Per tornar a provar el mètode 'mateix_autor', es comparen els llibres 2, 4
        Es farà servir la comanda llibre2.mateix_autor(llibre4) i serà True

Llibre 2 (Es farà servir la comanda llibre2.mostrar_info())
Títol: La plaça del Diamant (1962)
Autor: Mercè Rodoreda
Exemplars totals: 3
En préstec: 0
Disponibles: 3
------------------------------

Llibre 4 (Es farà servir la comanda llibre4.mostrar_info())
Títol: Mirall trencat (1962)
Autor: Mercè Rodoreda
Exemplars totals: 2
En préstec: 0
Disponibles: 2
------------------------------
El llibre 2 i el llibre 4 tenen el mateix autor? True
</pre>