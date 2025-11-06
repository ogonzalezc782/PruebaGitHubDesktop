import pandas as pd
import numpy as np
import math

df = pd.read_csv("diabetes.csv")
print("Dimensión de la tabla:", df.shape)

# Función que retorna el menor de tres valores
def menor(A, B, C):
    return min(A, B, C)

def mayor(A, B):
    return max(A, B)

def mayor_3(A, B,C):
    return max(A, B, C)
