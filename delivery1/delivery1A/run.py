"""
A.	Quieres hacer un juego de waterpolo sencillo y minimalista. Prepara las clases
    necesarias para poder identificar:
    i.	Un jugador en concreto
    ii.	Un equipo en concreto
    iii. Un partido entre dos equipos
    iv.	El resultado de un partido.
    v.	Un jugador debe poder marcar un gol afectando al resultado del partido.
    Para simplificar, la duración no será marcada por el tiempo sino por turnos.
    Un partido durará 10 turnos. Quien tenga más punto a final del partido habrá ganado.
"""

from dataclasses import dataclass, field


@dataclass
class Jugador:
    """Clase para cada jugador, componente de un equipo"""
    nombre: str
    goles: int = field(default=0)

    def marcar_gol(self):
        """Incrementa el número de goles del jugador en uno."""
        self.goles += 1
    
    
    def __post_init__(self):
        """Imprime las características del jugador al instanciarlo."""
        print(f"Jugador creado: {self}")

    def __str__(self):
        """Devuelve una representación del jugador y sus goles marcados en forma de string"""
        return f"Jugador: {self.nombre}, Goles: {self.goles}"


@dataclass
class Equipo:
    """Clase que representa a un equipo de waterpolo."""
    nombre: str
    jugadores: list = field(default_factory=list)

    def __post_init__(self):
        """Imprime las características del equipo al instanciarlo."""
        print(f"Equipo creado: {self}")

    def obtener_puntos_totales(self) -> int:
        """Obtiene el número total de puntos del equipo sumando los goles de sus jugadores."""
        return sum(jugador.goles for jugador in self.jugadores)

    def __str__(self):
        """Devuelve una representación en forma de cadena del equipo."""
        jugadores_str = "\n".join(str(jugador) for jugador in self.jugadores)
        return f"Equipo: {self.nombre}\nJugadores:\n{jugadores_str}"

    def __gt__(self, other):
        """Compara el puntaje del equipo con otro equipo."""
        return self.obtener_puntos_totales() > other.obtener_puntos_totales()


class Partido:
    """Clase que representa un partido de waterpolo entre dos equipos."""
    def __init__(self, equipo_local: Equipo, equipo_visitante: Equipo):
        """
        Inicializa una instancia de Partido.

        Args:
            equipo_local: Equipo local que participa en el partido.
            equipo_visitante: Equipo visitante que participa en el partido.
        """
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.turnos = 0

    def jugar_turno(self):
        """Simula el juego de un turno en el partido."""
        self.turnos += 1

    def obtener_resultado(self) -> str:
        """
        Obtiene el resultado del partido.

        Returns:
            El resultado del partido.
        """
        puntos_local = self.equipo_local.obtener_puntos_totales()
        puntos_visitante = self.equipo_visitante.obtener_puntos_totales()

        if puntos_local > puntos_visitante:
            return f"{self.equipo_local.nombre} ganó el partido"
        elif puntos_visitante > puntos_local:
            return f"{self.equipo_visitante.nombre} ganó el partido"
        else:
            return "El partido terminó en empate"

    def __str__(self):
        """Devuelve una representación en forma de cadena del partido."""
        return f"Partido:\n{self.equipo_local}\n{self.equipo_visitante}\nTurnos jugados: {self.turnos}"


def main():
    """Función principal que ejecuta el juego de waterpolo."""
    # Pedir número de jugadores por equipo
    num_jugadores = int(input("Ingrese el número de jugadores por equipo: "))

    # Crear jugadores
    jugadores_local = [Jugador(f"Jugador {i+1}") for i in range(num_jugadores)]
    jugadores_visitante = [Jugador(f"Jugador {i+1}") for i in range(num_jugadores)]

    # Crear equipos
    equipo_local = Equipo("Equipo Local", jugadores_local)
    equipo_visitante = Equipo("Equipo Visitante", jugadores_visitante)

    # Crear partido
    partido = Partido(equipo_local, equipo_visitante)

    # Jugar turnos
    for turno in range(1, 11):
        print(f"Turno número {turno}:")

        for jugador in equipo_local.jugadores:
            jugador.marcar_gol()
            print(f"Gol de {jugador.nombre} del equipo local")

        for jugador in equipo_visitante.jugadores:
            jugador.marcar_gol()
            print(f"Gol de {jugador.nombre} del equipo visitante")

        partido.jugar_turno()

    # Obtener resultado
    resultado = partido.obtener_resultado()
    print(resultado)


if __name__ == "__main__":
    main()
