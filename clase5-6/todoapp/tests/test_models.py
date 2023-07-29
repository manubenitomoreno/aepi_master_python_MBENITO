from ..todoapp.models import Tarea


def test_tarea_creation():
    tarea = Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juan")
    assert tarea.id == 1
    assert tarea.definition == "Hacer la compra"
    assert tarea.completed == False
    assert tarea.responsible == "Juan"
