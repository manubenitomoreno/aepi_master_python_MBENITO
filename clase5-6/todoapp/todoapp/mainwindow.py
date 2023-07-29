from PyQt6.QtWidgets import (
    QAbstractItemView, QHBoxLayout, QLineEdit, QComboBox,
    QListWidget, QMainWindow, QPushButton,
    QVBoxLayout, QListWidgetItem, QWidget
)
from PyQt6.QtCore import Qt

from .operations import DataOps
from .models import Tarea


class MainWindow(QMainWindow):
    """
    To-Do App Main Window. Instanciamos QMainWindow y vamos introduciendo los widgets
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do App")
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.list_widget.setAlternatingRowColors(True)

        self.delete_button = QPushButton('Delete')
        #self.complete_button = QPushButton('Toggle Done')
        self.complete_button = QPushButton('Toggle All Done')
        self.line_edit = QLineEdit()
        self.responsible_combo = QComboBox()  # New combo box for responsible person
        self.add_button = QPushButton("Add Item")
        self.add_button.setEnabled(False)  # Disable the button initially

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.complete_button)
        
        self.save_button = QPushButton("Save Changes")
        buttons_layout.addWidget(self.save_button)
        

        layout.addWidget(self.line_edit)
        layout.addWidget(self.responsible_combo)  # Add the combo box to the layout
        layout.addWidget(self.add_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.init_tasks()

        # Connect the signals to the slots
        self.list_widget.currentItemChanged.connect(self.list_item_checked)
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_selected_task)
        #self.complete_button.clicked.connect(self.toggle_task_completion)
        self.line_edit.textChanged.connect(self.check_add_button_state)  # Connect textChanged signal
        self.responsible_combo.currentIndexChanged.connect(self.check_add_button_state)  # Connect currentIndexChanged signal
        self.save_button.clicked.connect(self.save_tasks)
        self.complete_button.clicked.connect(self.toggle_all_done)


        # Populate the responsible combo box
        self.responsible_combo.addItems(['Juanito', 'Pepito', 'Fulanito'])

    def init_tasks(self) -> None:
        self.list_widget.clear()
        self.tasks = DataOps.get_tasks()

        for task in self.tasks:
            item = QListWidgetItem()
            item.setText(f"{task.definition} - Responsible: {task.responsible}")  # Display the responsible person
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            state = Qt.CheckState.Checked if task.completed else Qt.CheckState.Unchecked
            item.setCheckState(state)
            self.list_widget.addItem(item)

    def add_task(self) -> None:
        text = self.line_edit.text()
        responsible = self.responsible_combo.currentText()
        if text and responsible:
            task_id = max([c.id for c in self.tasks]) + 1
            task = Tarea(task_id, text, False, responsible)  # Include the responsible person
            self.tasks.append(task)
            DataOps.save_tasks(self.tasks)

            item = QListWidgetItem()
            item.setText(f"{task.definition} - Responsible: {task.responsible}")  # Display the responsible person
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.list_widget.addItem(item)

            self.line_edit.clear()
            self.responsible_combo.setCurrentIndex(0)  # Reset the combo box selection
            
    def delete_selected_task(self) -> None:
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.list_widget.row(item)
            task = self.tasks[index]  # Obtener la tarea correspondiente al índice
            self.tasks.remove(task)  # Eliminar la tarea de la lista
            self.list_widget.takeItem(index)
            
            # Actualizar el índice seleccionado si corresponde
            if index < self.list_widget.count():
                self.list_widget.setCurrentRow(index)
            elif self.list_widget.count() > 0:
                self.list_widget.setCurrentRow(self.list_widget.count() - 1)
            else:
                # Si no hay elementos en la lista, deseleccionar cualquier ítem seleccionado anteriormente
                self.list_widget.setCurrentItem(None)
                
            DataOps.save_tasks(self.tasks)

    def toggle_task_completion(self) -> None:
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.list_widget.row(item)
            task = self.tasks[index]
            task.completed = not task.completed
            state = (
                Qt.CheckState.Checked
                if task.completed
                else Qt.CheckState.Unchecked
            )
            item.setCheckState(state)
            DataOps.save_tasks(self.tasks)

    def list_item_checked(self, current_item: QListWidgetItem, previous_item: QListWidgetItem) -> None:
        if previous_item is not None:
            index = self.list_widget.row(previous_item)
            task = self.tasks[index]
            task.completed = False if task.completed else True
            state = (
                Qt.CheckState.Checked
                if task.completed
                else Qt.CheckState.Unchecked
            )
            previous_item.setCheckState(state)
            DataOps.save_tasks(self.tasks)

    def check_add_button_state(self) -> None:
        text = self.line_edit.text()
        responsible = self.responsible_combo.currentText()
        self.add_button.setEnabled(bool(text) and bool(responsible))
        
    def save_tasks(self) -> None:
        DataOps.save_tasks(self.tasks)
        
    def toggle_all_done(self) -> None:
        for item in range(self.list_widget.count()):
            list_item = self.list_widget.item(item)
            list_item.setCheckState(Qt.CheckState.Checked)
            task = self.tasks[item]
            task.completed = True
        DataOps.save_tasks(self.tasks)



