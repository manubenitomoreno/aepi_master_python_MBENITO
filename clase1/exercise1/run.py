"""
A.	Queremos hacer un juego de cartas sencillo con la baraja de póker. 
    El jugador 1, escoge una carta. El jugador 2, escoge otra. 
    Gana quien tiene la carta más alta entendiendo que:
i.	  No hay jokers
ii.	  El 2 es la carta más baja
iii.  En caso de dos números iguales gana el palo según el orden: 
      corazones, rombos, flores y picas.
"""

from game import Game
if __name__ == "__main__":
    this_game = Game()
    this_game.game()