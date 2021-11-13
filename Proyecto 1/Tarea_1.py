import pandas as pd
import numbers as np

def leer_csv (archivo):
    return pd.read_csv(archivo, sep = ';')