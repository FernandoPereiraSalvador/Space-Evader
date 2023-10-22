import os
import pickle
from clases.record import Record
def cargar_records():
    """
    Carga los registros (records).

    :return: Una lista de registros
    """

    # Crear una lista vacia para almacenar los comentarios
    records = []
    # Obtener la ubicación del archivo actual
    current_dir = os.path.dirname(__file__)

    archivo_punt_max = os.path.join(current_dir, os.path.join("data", "punt_max.txt"))

    # Comprobar si el archivo existe
    if os.path.exists(archivo_punt_max):
        # Abrimos el archivo en modo binario y leemos los records
        with open(archivo_punt_max, "rb") as file:  # Abrir en modo binario
            while True:
                try:
                    # Deserializa usando pickle y lo agrega a la lista "records"
                    record = pickle.load(file)
                    records.append(record)
                except EOFError:
                    # Captura la excepcion para comprobar el fin del archivo
                    break
    # Devuelve la lista
    return records


def guardar_records(records):
    """
    Guardar los registros

    :param records: Una lista con los records para guardar
    :return: None
    """

    # Abrimos el archivo en modo escritura binaria
    with open(os.path.join("data", "punt_max.txt"), "wb") as file:
        # Recorrer los records
        for record in records:
            # Serializar el registro y escribirlo en el archivo usando "pickle"
            pickle.dump(record, file)
