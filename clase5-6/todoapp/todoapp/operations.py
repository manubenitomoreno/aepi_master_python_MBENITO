from typing import Iterable
from .models import Tarea
from .storage import Storage

class DataOps:
    
    saved_data = None 
    
    @classmethod
    def get_tasks(cls) -> list[Tarea]:
        storage_data = Storage.read()
        tasks = cls.transform_storage_to_data(storage_data)
        return tasks

    @classmethod
    def transform_storage_to_data(cls, storage_data: dict) -> list[Tarea]:
        return [
            Tarea(
                int(task_id),
                task_data["definition"],
                task_data["completed"],
                task_data["responsible"],  # Retrieve the responsible field from the dictionary
            )
            for task_id, task_data in storage_data.items()
        ]

    @classmethod
    def transform_data_to_storage(cls, data: Iterable[Tarea]) -> dict:
        return {
            str(task.id): {
                "definition": task.definition,
                "completed": task.completed,
                "responsible": task.responsible,  # Add the responsible field to the dictionary
            }
            for task in data
        }

    @classmethod
        
    def save_tasks(cls, tasks) -> None:
        data = cls.transform_data_to_storage(tasks)
        #print([c.id for c in tasks])
        #print(data)
        Storage.write(data)
        cls.saved_data = tasks  # Actualizar el atributo saved_data
