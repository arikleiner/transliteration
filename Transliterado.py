#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Recibe un archivo .txt con el hebreo y el transliterado 
# (Una linea en hebreo y una en transliterado)
# y devuelve un archivo con el mismo nombre .csv
# hay que abrir el archivo en una planilla del calculos
# Alinear la hoja de derecha a izquierda (hebreo)
# Marcar toda la hoja y centrear las palabras en la celdas

import csv
import sys

OriginalFile=sys.argv[1]
DestinoFile=OriginalFile[0:-3]+"cvs"

with open(DestinoFile,'w',newline='') as output:
    writer = csv.writer(output,delimiter=",")
    #f = open('ToldotOriginal.txt', "r")
    f = open(OriginalFile, "r")
    for linea in f:
        if len(linea) == 2:
            pass
        else:
            linea = linea.replace("HASHEM","Adonai")
            linea = linea.replace("-"," ")
            linea = linea.replace(".","")
            linea = linea.replace("'","")
            linea = linea.replace(";","")
            linea = linea.replace(":","")

            writer.writerow(linea.split())

    f.close()
output.close()

