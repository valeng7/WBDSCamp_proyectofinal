# WBDSCamp_proyectofinal
### Instalación
Paquetes requeridos: pandas, numpy, os

### Corrida
Los archivos de entrada que se deben emplear son la base de datos (db) en txt de la herramienta DIANA-TarBase v.8 y los txt con los miRNAs interactuantes con el lncRNA SERTAD4-AS1.

### Documentación
#### Finalidad
El filtro se construyó ya que la base de datos en cuestión no cuenta con la capacidad de descargar los genes obtenidos tras ingresar los miRNAs en ella. Aunque TarBase ofrece la opción de descargar la base de datos, no hay una forma automatizada de procesarlos para que los investigadores puedan obtener resultados de una manera más eficiente. Por lo tanto, el proyecto tiene como objetivo brindar a otros investigadores que usen esta db la posibilidad de obtener las interacciones miRNA-mRNA de forma más rápida y sencilla.

#### Material
Para este proyecto se usó el lenguaje de programación Python 3, con las bibliotecas pandas, numpy y os, ya que facilitan el tratamiento de datos biológicos y en gran cantidad. Se empleó de igual forma la base de datos DIANA-TarBase v.8 debido a que es una db ampliamente usada en la investigación de RNAs no codificantes y, a diferencia de otras db como ENCORI-StarBase, TarBase no permite descargar los resultados de las interacciones.
Debido al tamaño de la base de datos, no es posible alojarla en Github. Por lo tanto, se ha almacenado en OneDrive y se puede acceder a ella a través de este enlace: [DIANA-TarBase v.8](https://correouisedu-my.sharepoint.com/:t:/g/personal/valentina2170074_correo_uis_edu_co/EYByBfS44FVGsy2afVavtkgBMpWjo5NbnW0C81QVMCgQgA?e=WVUP7L)

### Ejecución de archivo de Python desde la consola

Para ejecutar un archivo de Python desde la consola, sigue los siguientes pasos:

1. Abre una terminal en tu sistema operativo.
2. Navega hasta la carpeta donde se encuentra el archivo script_final_python.py utilizando el comando `cd`.
3. Ejecuta el comando `python script_final_python.py` en la terminal.

Asegúrate de tener instalado Python en tu sistema operativo antes de seguir estos pasos.

### Ejecución del archivo script_final_python.py

Para ejecutar el archivo `script_final_python.py` de manera concisa, sigue los siguientes pasos:

1. Abre una terminal en tu sistema operativo.
2. Navega hasta la carpeta donde se encuentra el archivo `script_final_python.py` utilizando el comando `cd`.
3. Ejecuta el siguiente comando en la terminal: 

```
python script_final_python.py
```

#### Resultados
Una vez aplicado el filtro, se obtuvieron 5 archivos de texto con los genes regulados por los miRNAs que interactúan con el lncRNA SERTAD4-AS1. Se emplearon lncRNAs debido al papel regulador relevante que poseen las redes de regulación lncRNA-miRNA-mRNA.
De esta forma, empleando el filtro realizado, hubo la posibilidad de obtener las interacciones miRNA-mRNA de forma mucho más eficiente, lo cual permitirá avanzar con mayor velocidad en investigaciones que involucren esta clase de interacciones. Debido a esto, la aproximación utilizada fue adecuada y logró cumplir el objetivo. Sin embargo, para obtener interacciones miRNA-mRNA más confiables, sería recomendable comparar los resultados con otras bases de datos similares.

En conclusión, el proyecto desarrollado puede ser una herramienta útil para la comunidad científica que trabaja en el campo de RNAs no codificantes al permitir a los investigadores una opción más eficiente de obtener las interacciones miRNA-mRNA a partir de la base de datos DIANA-TarBase. Además, al obtener un archivo por miRNA con los genes regulados por cada uno, se facilita la interpretación de los resultados.
