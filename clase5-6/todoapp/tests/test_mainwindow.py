import pytest
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtCore import Qt

from ..todoapp.mainwindow import MainWindow
from ..todoapp.models import Tarea
from ..todoapp.operations import DataOps


@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_init_tasks(main_window):
    # Datos de prueba
    tasks = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]
    # Mockear la función get_tasks para devolver los datos de prueba
    DataOps.get_tasks = lambda: tasks

    main_window.init_tasks()

    # Verificar si se agregaron los elementos a la lista correctamente
    assert main_window.list_widget.count() == len(tasks)
    for i, task in enumerate(tasks):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.text() == f"{task.definition} - Responsible: {task.responsible}"
        assert item.checkState() == (Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked)

def test_add_task(main_window, qtbot):
    # Datos de prueba
    text = "Nueva tarea"
    responsible = "Juanito"
    tasks_before = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]
    tasks_after = tasks_before + [Tarea(id=3, definition=text, completed=False, responsible=responsible)]

    # Establecer el texto y la selección en los campos de entrada
    main_window.line_edit.setText(text)
    main_window.responsible_combo.setCurrentText(responsible)

    # Simular el clic en el botón "Add Item"
    qtbot.mouseClick(main_window.add_button, Qt.MouseButton.LeftButton)

    # Verificar si se agregó la tarea correctamente
    assert main_window.list_widget.count() == len(tasks_after)
    for i, task in enumerate(tasks_after):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.text() == f"{task.definition} - Responsible: {task.responsible}"
        assert item.checkState() == (Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked)

    # Verificar si los datos se guardaron correctamente
    assert main_window.tasks == tasks_after
    
def test_delete_selected_task(main_window, qtbot):
    # Datos de prueba
    tasks_before = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
        Tarea(id=3, definition="Hacer ejercicio", completed=False, responsible="Fulanito"),
    ]
    tasks_after = tasks_before[1:]
    print(tasks_after)
    print(tasks_before)
    # Establecer los datos de prueba en la ventana principal
    main_window.tasks = tasks_before
    main_window.init_tasks()

    # Seleccionar el primer elemento de la lista (index 0) TODO Esto aún falla
    item = main_window.list_widget.item(0)
    main_window.list_widget.setCurrentItem(item)

    # Obtener el índice del elemento seleccionado
    selected_index = main_window.list_widget.row(item)
    # Simular el clic en el botón "Delete"
    qtbot.mouseClick(main_window.delete_button, Qt.MouseButton.LeftButton)

    # Verificar si se eliminó la tarea correctamente
    assert main_window.list_widget.count() == len(tasks_after)
    for i, task in enumerate(tasks_after):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.checkState() == (Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked)

    # Verificar si los datos se guardaron correctamente en la lista de tareas

    #assert main_window.tasks == tasks_after

    # Verificar si el elemento seleccionado ha cambiado
    assert main_window.list_widget.currentRow() == selected_index if selected_index < len(tasks_after) else -1

def test_toggle_task_completion(main_window, qtbot):
    # Datos de prueba
    tasks_before = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]
    tasks_after = [
        Tarea(id=1, definition="Hacer la compra", completed=True, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]

    # Establecer los datos de prueba en la ventana principal
    main_window.tasks = tasks_before
    main_window.init_tasks()

    # Seleccionar el primer elemento de la lista (index 0)
    item = main_window.list_widget.item(0)
    main_window.list_widget.setCurrentItem(item)

    # Simular el clic en el botón "Toggle Done"
    qtbot.mouseClick(main_window.complete_button, Qt.MouseButton.LeftButton)

    # Verificar si se actualizó el estado de la tarea correctamente
    assert main_window.list_widget.count() == len(tasks_after)
    for i, task in enumerate(tasks_after):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.checkState() == (Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked)


def test_list_item_checked(main_window, qtbot):
    # Datos de prueba
    tasks_before = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]
    tasks_after = [
        Tarea(id=1, definition="Hacer la compra", completed=True, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]

    # Establecer los datos de prueba en la ventana principal
    main_window.tasks = tasks_before
    main_window.init_tasks()

    # Seleccionar el primer elemento de la lista (index 0)
    item = main_window.list_widget.item(0)
    main_window.list_widget.setCurrentItem(item)

    # Simular el cambio de estado del elemento de la lista
    qtbot.keyClick(main_window.list_widget, Qt.Key.Key_Space)

    # Verificar si se actualizó el estado de la tarea correctamente
    assert main_window.list_widget.count() == len(tasks_after)
    for i, task in enumerate(tasks_after):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.checkState() == (Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked)

def test_check_add_button_state(main_window, qtbot):
    # Establecer el texto en el campo de entrada y la selección en el combo box
    main_window.line_edit.setText("Nueva tarea")
    main_window.responsible_combo.setCurrentText("Juanito")

    # Verificar si el botón "Add Item" está habilitado
    assert main_window.add_button.isEnabled()

    # Borrar el texto en el campo de entrada
    main_window.line_edit.clear()

    # Verificar si el botón "Add Item" está deshabilitado
    assert not main_window.add_button.isEnabled()

    # Establecer el texto nuevamente en el campo de entrada
    main_window.line_edit.setText("Nueva tarea")

    # Borrar la selección en el combo box
    main_window.responsible_combo.setCurrentIndex(-1)

    # Verificar si el botón "Add Item" está deshabilitado
    assert not main_window.add_button.isEnabled()

def test_save_tasks(main_window):
    # Datos de prueba
    tasks = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]
    # Establecer los datos de prueba en la ventana principal
    main_window.tasks = tasks

    main_window.save_tasks()

    # Verificar si los datos se guardaron correctamente utilizando la función save_tasks de DataOps
    assert DataOps.saved_data == tasks


def test_toggle_all_done(main_window):
    # Datos de prueba
    tasks_before = [
        Tarea(id=1, definition="Hacer la compra", completed=False, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=False, responsible="Pepito"),
    ]
    tasks_after = [
        Tarea(id=1, definition="Hacer la compra", completed=True, responsible="Juanito"),
        Tarea(id=2, definition="Estudiar para el examen", completed=True, responsible="Pepito"),
    ]

    # Establecer los datos de prueba en la ventana principal
    main_window.tasks = tasks_before
    main_window.init_tasks()

    # Simular el clic en el botón "Toggle All Done"
    main_window.toggle_all_done()

    # Verificar si se actualizó el estado de todas las tareas a completado correctamente
    for i in range(main_window.list_widget.count()):
        item = main_window.list_widget.item(i)
        assert item is not None
        assert item.checkState() == Qt.CheckState.Checked


