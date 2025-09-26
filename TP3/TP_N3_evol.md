
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## TP3: Asignación por homología y filogenia molecular

**Profesora**: Dra. Ana Julia Velez Rueda


# Trabajo Práctico: Evolución y Anotación Funcional de Proteínas

## Introducción

Las albúminas son las proteínas sanguíneas más abundantes en los mamíferos y cumplen la función principal de unir y transportar diversos compuestos endógenos y exógenos, en su mayoría hidrofóbicos. Esta proteína globular está compuesta por tres dominios homólogos (I, II y III), cada uno de los cuales contiene dos subdominios similares (A y B).  Esto la hace una una proteína de interés farmacológico ya que se encuentra involucrada en el en el reparto (delivery) de fármacos.

A lo largo de los vertebrados, las albúminas se conservan evolutivamente, aunque muestran una notable diversidad estructural.


**🧗🏻‍♀️ DESAFÍO I: Asignación por homología**


Utiliza la secuencia de albúmina humana (HSA) como consulta en **BLASTp** contra la base de datos de proteínas de vertebrados.  
 
  a. ¿Qué especies presentan ortólogos más cercanos a la HSA?  

  Gorilla gorilla gorilla → 99.01% identidad.
  Pan paniscus (bonobo) → 98.85% identidad.
  Pongo abelii (orangután de Sumatra) → 98.52% identidad.
  Pongo pygmaeus (orangután de Borneo) → 98.36% identidad.
  Nomascus leucogenys (gibón de mejillas blancas) → 97.21% identidad.
  Hylobates moloch (gibón de Java) → 97.04% identidad.

  b. ¿Qué criterios utilizaste para identificarlos?  

  Mayor % de identidad --> Es la proporción de aminoácidos idénticos entre la secuencia humana y la de otra especie. Cuanto mayor el % identidad, más cercanas son evolutivamente las secuencias.
  
  Cobertura completa de la proteína (100%) --> Indica qué porcentaje de la secuencia humana está alineada con la de la otra especie.En todos los casos es 100%, lo que significa que las proteínas comparadas son homólogas a lo largo de toda su longitud.
  
  E-value = 0.0 (significancia máxima) --> Representa la probabilidad de que el alineamiento se produzca al azar. Un E-value cercano a 0 (como en todos los resultados) significa que la similitud es biológicamente significativa.
  
  Altos scores de alineamiento --> Resume la calidad del alineamiento (considera identidad, gaps, penalizaciones).

  c. ¿Podrías identificar al menos **dos ortólogos** y **dos parálogos** en la familia de albúminas?

  Ortólogos → genes/proteínas homólogos en especies diferentes, originados por especiación.
  Parálogos → genes/proteínas homólogos dentro de la misma especie, originados por duplicación génica.

  Los ortólogos lo veo muy claro porque veo que son de otras especies: gorila, bonobo. Estos son ortólogos porque cumplen la misma función en diferentes especies de primates y derivan de un ancestro común.

  En BLASTp cambiamos el organismo a homo sapiens y ponemos el database en nr. Los resultados dieron: Dos parálogos dentro de la familia de albúminas humanas son AFP (alfa-fetoproteína) y GC (vitamina D–binding protein).
  
  d. **Obtené secuencias de albúminas** de al menos 8–10 especies diferentes de mamíferos desde **UniProt** y construí un alineamiento de proteínas ortólogas usando [Clustal Omega]. 

  el alineamiento esta el el archivo de nombre: clustal.txt

  e. ¿Qué porcentaje de identidad comparten?  

  Percent Identity  Matrix - created by Clustal2.1 

     1: XP_055153340.1  100.00   99.34   99.01   97.04   96.88   96.72   97.04   97.21
     2: XP_003265777.1   99.34  100.00   98.85   97.21   97.04   97.04   97.21   97.37
     3: XP_032006209.1   99.01   98.85  100.00   96.88   96.72   96.55   97.04   96.72
     4: NP_001127106.2   97.04   97.21   96.88  100.00   99.84   97.87   98.52   98.52
     5: XP_054342130.1   96.88   97.04   96.72   99.84  100.00   97.70   98.36   98.36
     6: XP_003832390.1   96.72   97.04   96.55   97.87   97.70  100.00   98.85   98.69
     7: NP_000468.1      97.04   97.21   97.04   98.52   98.36   98.85  100.00   99.01
     8: XP_004038851.3   97.21   97.37   96.72   98.52   98.36   98.69   99.01  100.00


  f. ¿Qué regiones se encuentran más conservadas?  

  Los tramos con asteriscos continuos ******** indican identidad absoluta:

  Residuos de cisteína (C) → esenciales para los puentes disulfuro que mantienen la estructura.
  Hélices alfa estructurales internas de la albúmina.
  Motivos de unión conservados como “KVPQVSTPTLVEVSRNL”.

  g. ¿Qué diferencias observas en las regiones cercanas a los sitios de unión?

  En el alineamiento se ven sustituciones conservativas (ej. cambios entre aminoácidos similares: E ↔ D, K ↔ R, I ↔ V).
  Estas variaciones se concentran en residuos periféricos alrededor de los sitios de unión → no alteran la estructura general, pero sí pueden explicar diferencias en afinidad por ligandos entre especies.

**🧗🏻‍♀️ DESAFÍO II:**


Usando el alineamiento del punto I.d construí un árbol filogenético mediante la herramienta [IQ-tree](https://iqtree.github.io/)

  a. Visualiza el árbol usando [iTOL](https://itol.embl.de/) o [FigTree](https://tree.bio.ed.ac.uk/software/figtree/)

  b. Estudiá los clados y relacionalo con las observaciones del punto anterior

  En el árbol podemos distinguir 2 hojas (XP_032006209 y XP_055153340.1) directamente descendientes de la raíz y un clado. El clado presenta 6 hojas, de las cuales XP_003832390.1 tiene una rama relativamente corta, lo que implica que es más conservado, siendo similar a XP_032006209 y aún más similar a XP_055153340.1, consistente con que el primero tiene mayor divergencia respecto a la raíz original. Para las últimos 5 hojas, podemos ver que aparecen varios nodos internos y ramas de divergencia considerable (dentro de la escala 0.01 del árbol) respecto a los primeros dos casos. Se aprecia que XP_003832390.1 a pesar de de venir del mismo ancestro inmediato que NP_000468.1 converge más que XP_004038851.3, el cual preseta mayor porcentaje de identidad respecto a NP_000468.1 y es consistente con que estos últimos dos tengan mayor conservación. Por último, analizando las dos hojas NP_001127106.2 y XP_054342130.1 vemos que tienen baja variabilidad desde su ancestro inmediato, pero respecto a los demás presetan la suficiente divergencia como para no llegar a un 99% de identidad compartida. 

<details>
<summary>Instrucciones de instalación de IQ-TREE</summary>

**Instalación de IQ-TREE**
   - En **Linux/macOS**:  
     ```bash
     conda install -c bioconda iqtree
     ```
     o descargar binarios desde [https://iqtree.org](https://iqtree.org).  

   - En **Windows**:  
     Descargar el ejecutable precompilado desde la misma página.  

**Ejecución básica**
   Una vez que tengas el alineamiento (`alignment.fasta`):  
   ```bash
   iqtree -s alignment.fasta -m AUTO -bb 1000 -nt AUTO
   ```
 Esto generará archivos de salida, incluyendo:
    * Alignment.fasta.treefile → el árbol filogenético en formato Newick.
    * Alignment.fasta.iqtree → información sobre el modelo y parámetros usados.
</details>


**🧗🏻‍♀️ DESAFÍO III: Anotación de blancos moleculares**


1. Consulta en bases de datos **ChEMBL** y **DrugBank** para identificar fármacos que se unan a la **albúmina humana (HSA)**.  

   a. ¿Qué tipo de moléculas suelen interactuar con la HSA?  

    Buscando en ChEMBL. Se encuentran moleculas pequeñas con anillos no polares

   b. ¿Qué importancia biomédica tiene esta interacción? 

    Esto sirve saber para saber que si tenemos la albumina como target nuestro farmaco tiene que tener partes hidrofobicas, en particular con anillos
     
   c. ¿Qué diferencias se reportan entre la unión de fármacos en la albúmina humana y la bovina?  

    (no estoy muy seguro)
    Comparando con el de Bos taurus vemos que los que se unen bien tienen tambien la parte hidrofobica pero solo se une bien el ibuprofeno, las moleculas mas grandes no se unen tan bien


   d. ¿Cuáles son las principales diferencias entre especies en dichas regiones de interés?

    Mayor tamaño de molecula admitido en humana y admite mas de un anillo

2. **Identificar características comunes**  
A partir de los compuestos encontrados:

     a. ¿Qué **motivo estructural (“andamiaje” o scaffold común)** comparten?  Podés usar el módulo admet:
     ```python
        moleculas = {
            'CMP-1': 'CC1=CC=CC=C1O',
            'CMP-2': 'CCOc1ccc2nc(SCc3ccccc3)sc2c1',
        }

        resultados = analisis_completo(moleculas)

        print(resultados['scaffolds'])
     ```
     Ambas comparten un núcleo aromático (anillo bencénico). Este tipo de scaffold es muy frecuente en fármacos que se unen a albúmina humana (HSA), ya que la proteína tiene bolsillos hidrofóbicos que estabilizan bien sistemas aromáticos planos mediante interacciones hidrofóbicas.
   Este patrón es recurrente en ligandos de HSA reportados en ChEMBL/DrugBank, como ibuprofeno, warfarina y diazepam, lo que confirma que el motivo aromático es un rasgo estructural clave

     b. ¿Qué **sustituyentes (grupos químicos)** están presentes en diferentes posiciones?
CMP-1 (fenol): Un –OH en posición aromática → le da polaridad y capacidad de puente de hidrógeno.
CMP-2 (benzotiazol):
-  –OCH2CH3 (etoxi): grupo polar moderado que aumenta solubilidad.
-  –SC–fenilo: un sustituyente voluminoso y muy hidrofóbico, aporta interacción π adicional.
-  Heteroátomos en el anillo (N, S) que pueden dar sitios de interacción específicos con residuos polares de la proteína.
     
     c. ¿Qué diferencias y similitudes estructurales hay entre estos compuestos? ¿Cómo crees que deben ser las distintas proteínas en los sitios capaces de transportarlos?
Similitudes:
- Ambos tienen anillos aromáticos como núcleo principal.
- Los dos incluyen sustituyentes que modulan polaridad (–OH, –OCH2CH3).
Diferencias:
- CMP-1 es mucho más simple, pequeño y con solo un anillo.
- CMP-2 es más grande y complejo, con varios anillos aromáticos conectados y heteroátomos.
- CMP-2 puede ocupar bolsillos más grandes de HSA, mientras que CMP-1 solo interacciones más superficiales.

Deben tener bolsillos hidrofóbicos amplios para alojar anillos aromáticos. Al mismo tiempo, necesitan residuos polares estratégicos (ej. Tyr, Arg, Lys, His) cerca para interaccionar con grupos –OH o heteroátomos.
Sitios flexibles: la HSA humana admite moléculas más grandes y con varios anillos (ej. ibuprofeno, warfarina), mientras que la bovina se ajusta mejor a compuestos más chicos y menos voluminosos.


**🧗🏻‍♀️ DESAFÍO IV: Identificación de sitios de interés**

Utilizando las bases de datos [Uniprot](https://www.uniprot.org/) e [InterPro](https://www.ebi.ac.uk/interpro/) para identificar dominios y motivos conservados en la HSA.  
  
  a. ¿Cuáles son los dominios principales identificados?  

  b. ¿Coinciden con los sitios conocidos de unión a ligandos?  

  c. ¿Qué residuos resultan altamente conservados en ortólogos y podrían ser críticos para la función?

  d. ¿Cómo se distribuyen los dominios principales a lo largo del árbol?

  e. ¿Existen evidencias de interferencias farmacológicas o promiscuidad proteica de impacto farmacológico para la HSA?


## 💡 Para investigar

Lee [investigación](https://www.sciencedirect.com/science/article/abs/pii/S0300908422000426) realizada en la **Universidad Nacional de Quilmes (UNQ)** por el **Grupo de Bioinformática Estructural** sobre la evolución de albúminas y contrastá tus observaciones bioinformáticas con los hallazgos reportados en la literatura.
