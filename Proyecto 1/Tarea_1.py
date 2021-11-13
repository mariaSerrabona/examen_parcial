import pandas as pd
import numbers as np
import csv

def leer_csv (archivo):
    df= pd.read_csv(archivo, sep = ';')

    return df


leer_csv('conversiones.py')