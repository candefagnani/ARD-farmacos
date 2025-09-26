
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
  La albúmina humana está formada por **tres dominios homólogos (I, II y III)**, y cada dominio se divide en dos subdominios (A y B). Esa arquitectura de tres repeticiones corresponde a la familia Serum_albumin (Pfam PF00273 / InterPro) [InterPro](https://www.ebi.ac.uk/interpro/entry/pfam/PF00273/) —es decir, el “módulo albumina” aparece repetido tres veces a lo largo de la proteína.
  ![Imagen dominios albúmina](Dominios_HSA.png)

  b. ¿Coinciden con los sitios conocidos de unión a ligandos? 
  Sí. Los dos sitios de unión principales descritos clásicamente (Sudlow site I y Sudlow site II) se localizan en cavidades hidrofóbicas de **subdominio IIA (site I) y subdominio IIIA (site II)** respectivamente. Estas cavidades corresponden exactamente a porciones de los dominios/ subdominios ya anotados por UniProt/Pfam y están bien caracterizadas por estructuras cristalográficas.
  ![Imagen](subdominios_pregunta4b.png)

  c. ¿Qué residuos resultan altamente conservados en ortólogos y podrían ser críticos para la función?
  Del alineamiento de albúminas emergen varios residuos que son recurrentemente señalados como **críticos** para unión de ligandos y función:
  1. Trp214 --> única triptófano de HSA, se encuentra en el bolsillo del Sudlow I y participa fuertemente en reconocimiento y fluorescencia del sitio.
  2. Tyr150 --> contribuye al entorno de Site I (ambiente polar/hidrofóbico).
  3. Cluster de carga en la entrada del Site I: Lys195, Lys199, Arg218, Arg222 --> suelen formar una "boca" polar/positiva que regula la entrada de ligandos.
  4. His242, Arg257 --> también asociados con la química interna del Site I.
  5. Cys34 --> única cisteína libre en la molécula (las demás forman disulfuros) y es redox-activa; conserva una función antioxidante y su modificación afecta regiones de unión. Es un residuo altamente conservado y funcionalmente importante.

  d. ¿Cómo se distribuyen los dominios principales a lo largo del árbol?
  --> La arquitectura de 3 dominios es conservada en vertebrados: la mayoría de las albúminas de mamíferos y otros vertebrados muestran las 3 repeticiones (PF00273), por eso los orthólogos se alinean a lo largo de toda la longitud proteica.
  --> Los parálogos dentro de la familia (por ejemplo APF - alfa-fetoproteína, GC – vitamin D–binding protein, afamin) comparten el mismo marco de dominio pero se separan en clados distintos en árboles filogenéticos (duplicaciones antiguas y luego divergencia funcional). Esa separación es visible cuando haces un árbol con las secuencias completas: los clados reflejan tanto la historia de especiación como las duplicaciones génicas que originaron paralogías.

  ![ortologos](ortologos.png)

  ![paralogos](paralogos.png)

  e. ¿Existen evidencias de interferencias farmacológicas o promiscuidad proteica de impacto farmacológico para la HSA?
  Sí. HSA es altamente promiscuo: transporta ácidos grasos, hormonas, bilirrubina y una enorme variedad de fármacos (warfarin, ibuprofeno, muchos AINEs, antibióticos, etc.). La unión de fármacos a HSA modifica la fracción libre de fármaco en plasma y puede causar interacciones farmacológicas (competencia por sitios, efectos alostéricos, desplazamiento por ácidos grasos). Ejemplos clásicos: warfarin (probe de Sudlow I) y ibuprofeno (preferentemente Site II; aunque ibuprofeno puede mostrar múltiples modos/ sitios de unión). Además existen formulaciones farmacéuticas que aprovechan albumina como vehículo (por ejemplo: nab-paclitaxel / Abraxane)

## 💡 Para investigar

Lee [investigación](https://www.sciencedirect.com/science/article/abs/pii/S0300908422000426) realizada en la **Universidad Nacional de Quilmes (UNQ)** por el **Grupo de Bioinformática Estructural** sobre la evolución de albúminas y contrastá tus observaciones bioinformáticas con los hallazgos reportados en la literatura.
Al analizar la evolución de las albúminas, se observa un árbol filogenético donde dos secuencias (XP_032006209 y XP_055153340.1) descienden directamente de la raíz, mientras que el resto se agrupa en un clado. Esta organización refleja lo que también reporta Rueda et al. (2022), quienes describen que algunas secuencias mantienen una cercanía notable al nodo ancestral, lo que sugiere una conservación relativamente alta de características estructurales y funcionales. Dentro del clado, XP_003832390.1 presenta una rama relativamente corta, lo que indica menor acumulación de cambios y, por lo tanto, mayor conservación. Este hallazgo es coherente con lo señalado en el artículo, donde se destaca que ciertos linajes han retenido regiones altamente conservadas, en particular aquellas asociadas a dominios funcionales críticos. Además, la similitud de esta secuencia con XP_032006209 y, en mayor medida, con XP_055153340.1 coincide con la idea de que algunas ramas permanecen más próximas a la raíz original. En contraste, las últimas cinco hojas del árbol muestran múltiples nodos internos y ramas con divergencia considerable en la escala de 0.01, lo que evidencia mayor variabilidad entre ellas. El trabajo de Rueda et al. también describe esta coexistencia entre conservación y divergencia: mientras algunas secuencias retienen su conformación esencial, otras acumulan cambios que, aunque generan distancias filogenéticas notables, no alteran necesariamente la función de la proteína. En particular, XP_003832390.1 y XP_004038851.3 comparten un ancestro inmediato con NP_000468.1. Sin embargo, la primera converge más hacia dicho ancestro, mientras que XP_004038851.3 muestra mayor identidad directa con NP_000468.1. Esta observación es consistente con lo reportado en el artículo, donde se señala que ciertas secuencias se aproximan más a la albúmina humana de referencia, reflejando un grado mayor de conservación evolutiva. Conviene aclarar que este “acercamiento” no implica evolución convergente, sino simplemente una menor divergencia acumulada. Finalmente, las secuencias NP_001127106.2 y XP_054342130.1 exhiben poca variabilidad respecto a su ancestro inmediato, aunque mantienen suficiente divergencia con las demás como para no alcanzar un 99% de identidad compartida. Esta situación coincide con la descripción de Rueda et al., donde se señala que existen ramas evolutivas que conservan estabilidad interna, pero que al compararse con otros linajes muestran diferencias significativas, reforzando la idea de una evolución balanceada entre conservación de la estructura funcional y diversificación entre especies.