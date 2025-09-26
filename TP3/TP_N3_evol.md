
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

  e. ¿Qué porcentaje de identidad comparten?  

  f. ¿Qué regiones se encuentran más conservadas?  

  g. ¿Qué diferencias observas en las regiones cercanas a los sitios de unión?



**🧗🏻‍♀️ DESAFÍO II:**


Usando el alineamiento del punto I.d construí un árbol filogenético mediante la herramienta [IQ-tree](https://iqtree.github.io/)

  a. Visualiza el árbol usando [iTOL](https://itol.embl.de/) o [FigTree](https://tree.bio.ed.ac.uk/software/figtree/)

  b. Estudiá los clados y relacionalo con las observaciones del punto anterior

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

     b. ¿Qué **sustituyentes (grupos químicos)** están presentes en diferentes posiciones?  
     
     c. ¿Qué diferencias y similitudes estructurales hay entre estos compuestos? ¿Cómo crees que deben ser las distintas proteínas en los sitios capaces de transportarlos? 


**🧗🏻‍♀️ DESAFÍO IV: Identificación de sitios de interés**

Utilizando las bases de datos [Uniprot](https://www.uniprot.org/) e [InterPro](https://www.ebi.ac.uk/interpro/) para identificar dominios y motivos conservados en la HSA.  
  
  a. ¿Cuáles son los dominios principales identificados?  

  b. ¿Coinciden con los sitios conocidos de unión a ligandos?  

  c. ¿Qué residuos resultan altamente conservados en ortólogos y podrían ser críticos para la función?

  d. ¿Cómo se distribuyen los dominios principales a lo largo del árbol?

  e. ¿Existen evidencias de interferencias farmacológicas o promiscuidad proteica de impacto farmacológico para la HSA?


## 💡 Para investigar

Lee [investigación](https://www.sciencedirect.com/science/article/abs/pii/S0300908422000426) realizada en la **Universidad Nacional de Quilmes (UNQ)** por el **Grupo de Bioinformática Estructural** sobre la evolución de albúminas y contrastá tus observaciones bioinformáticas con los hallazgos reportados en la literatura.