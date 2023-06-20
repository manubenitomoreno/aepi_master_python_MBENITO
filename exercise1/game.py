from cards import Card
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    hand: Card
    points: int = 0

@dataclass
class Game:
    
@dataclass
hand