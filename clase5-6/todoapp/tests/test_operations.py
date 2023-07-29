from ..todoapp.models import Tarea
from ..todoapp.operations import DataOps


def test_transform_storage_to_data():
    storage_data = {
        "1": {"definition": "Hacer la compra", "completed": False, "responsible": "Juan"},
        "2": {"definition": "Estudiar para el examen", "completed": True, "responsible": "Maria"},
    }
    expected_result = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juan"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Maria"),
    ]

    result = DataOps.transform_storage_to_data(storage_data)

    assert result == expected_result


def test_transform_data_to_storage():
    data = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juan"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Maria"),
    ]
    expected_result = {
        "1": {"definition": "Hacer la compra", "completed": False, "responsible": "Juan"},
        "2": {"definition": "Estudiar para el examen", "completed": True, "responsible": "Maria"},
    }

    result = DataOps.transform_data_to_storage(data)

    assert result == expected_result
