from dataclasses import dataclass


@dataclass
class Tarea:
    '''
    Una tarea por completar
    '''
    id: int
    definition: str
    completed: bool
    responsible: str = ""

