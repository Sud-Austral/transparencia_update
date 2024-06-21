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


if __name__ == '__main__':
    ultima_posicion_byte = leer_estado_ultima_descarga(state_file_path)
    print(f"leer {ultima_posicion_byte}")
    
