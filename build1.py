import pandas as pd
from datetime import datetime
import re
import os
import time
import tarfile
import requests
from io import StringIO
import pickle





state_file_path = 'ultima_descarga.pkl'
dict_picklet = {"TA_PersonalPlanta_pickle":5332967810,
    "TA_PersonalContratohonorarios_pickle":5088589288,
    "TA_PersonalCodigotrabajo_pickle":3719386149,
    "TA_PersonalContrata_pickle":8726203526
    }
# Guardar el estado de la última descarga usando pickle
def guardar_estado_ultima_descarga(state_file, byte_position):
    with open(state_file, 'wb') as file:
        pickle.dump(byte_position, file)
        
# Leer el estado de la última descarga usando pickle
def leer_estado_ultima_descarga(state_file):
    if os.path.exists(state_file):
        with open(state_file, 'rb') as file:
            return pickle.load(file)
    return 0

class BaseDatos:
    def init(self, name,namePickle):
        self.name = name
        self.file = f"{name}.csv"
        self.url = f"https://www.cplt.cl/transparencia_activa/datoabierto/archivos/{name}.csv"
        self.namePickle = namePickle
        self.sizePickle = leer_estado_ultima_descarga(namePickle)

lista = [BaseDatos("TA_PersonalPlanta","TA_PersonalPlanta_pickle"),
        BaseDatos("TA_PersonalContratohonorarios","TA_PersonalContratohonorarios_pickle"),
        BaseDatos("TA_PersonalCodigotrabajo","TA_PersonalCodigotrabajo_pickle"),
        BaseDatos("TA_PersonalContrata","TA_PersonalContrata_pickle")]


if __name__ == '__main__':
    for i in lista:
        print(i.url)
    
