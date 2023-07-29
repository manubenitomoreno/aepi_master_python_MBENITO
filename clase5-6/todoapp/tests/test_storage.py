import json
import os
from ..todoapp.storage import Storage


def test_store_in_json(tmpdir):
    # Crear una ruta temporal para el archivo de prueba
    file_path = tmpdir.join("test_storage.json")
    # Establecer el nombre del archivo en la clase Storage
    Storage.file_name = str(file_path)

    # Datos de prueba
    data = {"id": 1, "name": "John"}

    # Almacenar en JSON
    Storage.store_in_json(data)

    # Verificar si el archivo existe
    assert file_path.exists()

    # Leer el contenido del archivo
    with open(str(file_path), "r") as file:
        stored_data = json.load(file)

    # Verificar si los datos almacenados son correctos
    assert stored_data == data


def test_retrieve_from_json(tmpdir):
    # Crear una ruta temporal para el archivo de prueba
    file_path = tmpdir.join("test_storage.json")
    # Establecer el nombre del archivo en la clase Storage
    Storage.file_name = str(file_path)

    # Datos de prueba
    data = {"id": 1, "name": "John"}

    # Escribir datos en el archivo JSON
    with open(str(file_path), "w") as file:
        json.dump(data, file)

    # Recuperar datos del archivo JSON
    retrieved_data = Storage.retrieve_from_json()

    # Verificar si los datos recuperados son correctos
    assert retrieved_data == data


def test_storage_config_mapper():
    # Obtener el mapeo de configuración de almacenamiento
    mapper = Storage.storage_config_mapper()

    # Verificar si el mapeo es correcto
    assert "JSON" in mapper
    assert "CSV" in mapper
    assert "read" in mapper["JSON"]
    assert "write" in mapper["JSON"]
    assert "read" in mapper["CSV"]
    assert "write" in mapper["CSV"]
