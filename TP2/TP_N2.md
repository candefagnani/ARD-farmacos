
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## TP2: Evaluación in silico de propiedades ADMET y filtros de selección de candidatos a fármaco

**Profesora**: Dra. Ana Julia Velez Rueda

En el diseño de fármacos, una de las principales causas de fracaso en fases clínicas es la falta de propiedades farmacocinéticas adecuadas o la aparición de toxicidad inesperada. Para minimizar costos y tiempo, se aplican métodos in silico que permiten predecir la Absorción, Distribución, Metabolismo, Excreción y Toxicidad (ADMET) de moléculas candidatas.

Además, se utilizan filtros de “drug-likeness”, como las reglas de Lipinski y Veber, junto con los filtros de PAINS, para descartar compuestos con baja probabilidad de éxito o con estructuras problemáticas.

### CONSIGNAS PRÁCTICOS
1. Selección de compuestos:
    a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov). 
    Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

* aspirin --> SMILES: CC(=O)OC1=CC=CC=C1C(=O)O
* paracetamol --> SMILES: CC(=O)NC1=CC=C(C=C1)O
* caffeine --> SMILES: CN1C=NC2=C1C(=O)N(C(=O)N2C)C  

    b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

FDA Approved:
* Teniposide
* Ecteinascidins  
* Imatinib

Experimental:
* Luteolin-7-O-glucoside
* (10E)-9-oxo-10-octadecenoic acid



2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:
    a. Peso molecular --> 
    b. LogP (índice de lipofilicidad) --> Medida del índice de lipofilicidad de una sustancia, que cuantifica su afinidad por una fase lípidica (no polar) frente a una fase acuosa (polar).
    c. H-bond acceptors
    d. H-bond donors
    e. TPSA (Superficie polar) --> Cuantifica la suma de la superficie de los átomos polares en una molécula.
    f. Rotatable bonds

aspirin:
    Peso molecular --> 180.16 g/mol
    LogP (índice de lipofilicidad) --> 1.30
    H-bond acceptors --> 4
    H-bond donors --> 1
    TPSA (Superficie polar) --> 63.60 Å²
    Rotatable bonds --> 3

paracetamol:
    Peso molecular --> 151.16 g/mol
    LogP (índice de lipofilicidad) --> 1.21
    H-bond acceptors --> 2
    H-bond donors --> 2
    TPSA (Superficie polar) --> 49.33 Å²
    Rotatable bonds --> 2

caffeine:
    Peso molecular --> 194.19 g/mol
    LogP (índice de lipofilicidad) --> 1.79
    H-bond acceptors --> 3
    H-bond donors --> 0
    TPSA (Superficie polar) --> 61.82 Å²
    Rotatable bonds --> 0

3. Identificar subestructuras indeseables de los compuestos del punto 1.ay 1.b usando la la siguiente módulo de python creado para tal fin siguiendo el tutorial:

```python
$ pip install rdkit-pypi molvs requests pandas numpy matplotlib seaborn
$ pip install deepchem 
$ python
Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from admet_module import analisis_completo
>>> mis_moleculas = {'molecula': 'COc1ccccc1C=O'}
>>> resultados = analisis_completo(mis_moleculas)
>>> print(resultados.keys())
>>> print(resultados['propiedades'])
```

4. Realizar la predicción de toxicidad in silico utilizando ProTox-II (https://tox-new.charite.de/protox_II/). Utilizando los SMILES de moléculas del punto 1.a y 1.b, obtener: 

    a. Predicted LD50 (mg/kg) y clase de toxicidad (I–VI).
* Aspirin: CC(=O)OC1=CC=CC=C1C(=O)O
    * LD50 (mg/kg): 250
    * Clase de Toxicidad: III
* Paracetamol: CC(=O)NC1=CC=C(C=C1)O
    * LD50 (mg/kg): 338
    * Clase de Toxicidad: IV
* Caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C
    * LD50 (mg/kg): 127
    * Clase de Toxicidad: III
   
    b. Riesgo de hepatotoxicidad, mutagenicidad, carcinogenicidad.
* Aspirin:
    * Hepatotoxicidad: Probabilidad 0.51
    * Carcinogenicidad: Probabilidad 0.86
    * Mutagenicidad: Probabilidad 0.97
* Paracetamol:
    * Hepatotoxicidad: Probabilidad 0.74
    * Carcinogenicidad: Probabilidad 0.51
    * Mutagenicidad: Probabilidad 0.90
* Caffeine:
    * Hepatotoxicidad: Probabilidad 0.97
    * Carcinogenicidad: Probabilidad 0.93
    * Mutagenicidad: Probabilidad 0.94
   
    ¿Cuál de las moléculas seleccionadas muestra menor toxicidad según ProTox-II?
Teniendo en cuenta:
* Class I: fatal if swallowed (LD50 ≤ 5)
* Class II: fatal if swallowed (5 < LD50 ≤ 50)
* Class III: toxic if swallowed (50 < LD50 ≤ 300)
* Class IV: harmful if swallowed (300 < LD50 ≤ 2000)
* Class V: may be harmful if swallowed (2000 < LD50 ≤ 5000)
* Class VI: non-toxic (LD50 > 5000)
Y siendo LD50 la dosis necesaria para causar la muerte en el 50% de la población de prueba. Por tanto, un valor más bajo significa una molécula más tóxica, porque basta con menos cantidad para producir el mismo efecto. Por eso, la molécula menos tóxica es el paracetamol. 



6. Construir una ficha técnica de cada compuesto que considere las respuestas a las siguientes preguntas: ¿Qué compuestos cumplen mejor con los filtros de Lipinski y Veber? ¿Aparecieron moléculas con alertas PAINS? ¿Cuál es su toxicidad?

aspirin
    Lipinski: Si
    Veber: Si
    Pains:
    Toxicidad:clase 3 (toxica si se ingiere)
paracetamol
    Lipinski: Si
    Veber: Si
    Pains:
    Toxicidad:clase 4 (Nocivo por ingestión)
caffeine
    Lipinski: Si
    Veber: Si
    Pains:
    Toxicidad:clase 3 (toxica si se ingiere)
