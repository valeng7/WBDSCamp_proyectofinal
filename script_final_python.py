##Instalar librerias##
import pandas as pd
import numpy as np
import os

# Obtener la ruta del directorio actual
workspace = os.getcwd()

##Leer base de datos Tarbase en txt##
df = pd.read_csv('TarBase_v8_download.txt', sep='\t')

##Crear dataframe con las columnas de interes##
cols = ['geneName', 'mirna', 'species', 'method', 'positive_negative', 'direct_indirect']
df_sel = df.loc[:, cols]

## Importación de los micros
SERTAD4AS1 = pd.read_csv("miRNAs_SERTAD4AS1.txt", sep="\t", header=None)

SERTAD4AS1 = SERTAD4AS1.drop(SERTAD4AS1.index[0])
## FILTROS

# FILTRO 1: filtrar por metodos de interes
filtro_method = df_sel.loc[df_sel['method'].isin(['Degradome', 'HITS-CLIP', 'iCLIP', 'Luciferase Reporter Assay', 'PAR-CLIP', 'Western Blot'])]

# FILTRO 2: filtrar por especie y validacion
filtro_datatar = filtro_method.loc[(filtro_method['species'] == 'Homo sapiens') & (filtro_method['positive_negative'] == 'POSITIVE') & (filtro_method['direct_indirect'] == 'DIRECT')]

# FILTRO 3: FILTRO PARA USAR CON CADA MIRNA
def f_micros_filtros(micro): 
    # En este filtro se ingresa los miRNAs a analizar para asi hallar los mRNAs interactuantes con ellos
    print(micro)
    mirna_analizar_ind = filtro_datatar[filtro_datatar['mirna'].isin(micro)]
    # sacar genes unicos
    genes_unicos_ind = mirna_analizar_ind['geneName'].unique()

    return genes_unicos_ind

# Verificar si la carpeta ya existe y crearla si no
ruta = os.path.join(workspace, "Resultados")
if not os.path.exists(ruta):
    os.mkdir(ruta)

def f_micro_rutas(micro):
    #LLamado de funcion (ya filtrada y unica)#
    resultmicro = f_micros_filtros(micro)
    path_file = os.path.join(ruta, micro[0] + ".txt")
    #Debuggeo
    print(f"{pd.Timestamp.now().strftime('%H:%M:%S')} #Registros: {len(resultmicro)}")

    np.savetxt(path_file, resultmicro, delimiter=' ', newline='\n', fmt='%s')

# Recorrer los micros 
for micro in SERTAD4AS1.values:
    f_micro_rutas(micro)

print(f"{pd.Timestamp.now().strftime('%H:%M:%S')} #Archivos generados en Resultados/")
