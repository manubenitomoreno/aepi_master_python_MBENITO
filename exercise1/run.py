"""
A.	Queremos hacer un juego de cartas sencillo con la baraja de póker. 
    El jugador 1, escoge una carta. El jugador 2, escoge otra. 
    Gana quien tiene la carta más alta entendiendo que:
i.	  No hay jokers
ii.	  El 2 es la carta más baja
iii.  En caso de dos números iguales gana el palo según el orden: 
      corazones, rombos, flores y picas.
"""
from dataclasses import dataclass
import random

@dataclass
class Palo:
    nombre: str
    ordenacion: int

    def __gt__(self, otro_palo):
        return self.ordenacion > otro_palo.ordenacion


@dataclass
class Carta:
    valor: int
    palo: Palo

@dataclass(order=True)
class Jugador:
    nickname: str
    puntos: int = 0
    


@dataclass
class Jugada:
    jugador: Jugador
    carta: Carta

    def __gt__(self, otra_jugada):
        if self.carta.valor == otra_jugada.carta.valor:
            return self.carta.palo > otra_jugada.carta.palo
        return self.carta.valor > otra_jugada.carta.valor


@dataclass
class Juego: 
    numero_jugadores: int = 2
    numero_jugadas: int = 5

    def preparar_baraja(self):
        baraja = []
        for nombre_palo, idx in enumerate(["Corazones",  "Diamantes",  "Tréboles","Picas"]):
            palo = Palo(nombre=nombre_palo, ordenacion=idx)
            for value in range(2, 15):
                carta = Carta(valor=value, palo=palo)
                baraja.append(carta)
        return baraja

    def generar_jugadores(self):
        jugadores = []
        for numero in range(self.numero_jugadores):
            jugadores.append(Jugador(nickname=f"Jugador {numero}"))
        return jugadores

    def asignar_carta(self, baraja, jugador):
        random.shuffle(baraja)
        carta = baraja.pop()
        jugada = Jugada(carta=carta, jugador=jugador)
        return jugada

    def comparar_jugadas(self, jugadas):
        ganador_parcial = jugadas[0]
        for jugada in jugadas[1:]:
            if jugada > ganador_parcial:
                ganador_parcial = jugada
        return ganador_parcial

    def juego(self):
        print(f"Principio del juego")
        baraja = self.preparar_baraja()
        jugadores = self.generar_jugadores()
        for jugada in range(self.numero_jugadas):
            print(f"Turno {jugada} principio")
            buffer = []
            for jugador in jugadores:
                print(f"Turno de jugador {jugador} principio")
                jugada = self.asignar_carta(baraja, jugador)
                buffer.append(jugada)
                print(f"Turno de jugador {jugador} final")
            jugada_ganadora = self.comparar_jugadas(buffer)
            jugada_ganadora.jugador.puntos += 1
            print(f"Ha ganado jugador {jugada_ganadora.jugador}")
            print(f"Turno {jugada} final")
        for jugador in sorted(jugadores):
            print(jugador.nickname, jugador.puntos)

        print("Final del juego")


if __name__ == "__main__":
    juego = Juego()
    juego.juego()