"""
Simulación de la Hormiga de Langton.

Autómata celular 2D donde una "hormiga" se mueve sobre una cuadrícula
cambiando el color de las casillas y girando según reglas simples,
generando un comportamiento emergente complejo.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---------------------------------------------------------------------------
# Variables de configuración
# ---------------------------------------------------------------------------
BOARD_SIZE = 100       # Tamaño de la cuadrícula (BOARD_SIZE x BOARD_SIZE)
ANIMATION_SPEED = 20  # Intervalo entre frames en milisegundos (menor = más rápido)
STEPS_PER_FRAME = 1   # Cantidad de pasos de la hormiga por frame renderizado

# Colores de casilla
BLACK = 0
WHITE = 1

# Colores RGB para dibujar
COLOR_BLACK = (0.0, 0.0, 0.0)
COLOR_WHITE = (1.0, 1.0, 1.0)
COLOR_ANT = (1.0, 0.0, 0.0)  # la casilla donde está la hormiga se pinta de rojo

# Direcciones: arriba, derecha, abajo, izquierda (sentido horario)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Board:
    """Representa la cuadrícula del tablero."""

    def __init__(self, size):
        self.size = size
        self.grid = [[BLACK for _ in range(size)] for _ in range(size)]

    def is_inside(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def get_color(self, row, col):
        return self.grid[row][col]

    def toggle_color(self, row, col):
        self.grid[row][col] = WHITE if self.grid[row][col] == BLACK else BLACK

    def to_rgb_array(self):
        """Convierte la grilla a un array RGB para su visualización."""
        array = np.zeros((self.size, self.size, 3))
        for row in range(self.size):
            for col in range(self.size):
                array[row][col] = COLOR_WHITE if self.grid[row][col] == WHITE else COLOR_BLACK
        return array


class Ant:
    """Representa la hormiga de Langton y su lógica de movimiento."""

    def __init__(self, board, row, col, direction_index=0):
        self.board = board
        self.row = row
        self.col = col
        self.direction_index = direction_index  # índice sobre DIRECTIONS
        self.alive = True  # False cuando la hormiga desaparece por completo

    def step(self):
        """Ejecuta un paso de la hormiga siguiendo las reglas del sistema.

        Al salir del tablero, la hormiga sigue moviéndose "fuera de cámara"
        durante un paso adicional (sin dibujarse) antes de desaparecer
        totalmente y detener la simulación.
        """
        if not self.alive:
            return

        if not self.board.is_inside(self.row, self.col):
            # Ya venía moviéndose fuera del tablero: ahora desaparece del todo.
            self.alive = False
            return

        current_color = self.board.get_color(self.row, self.col)

        if current_color == WHITE:
            self.board.toggle_color(self.row, self.col)  # -> negro
            self.turn_right()
        else:
            self.board.toggle_color(self.row, self.col)  # -> blanco
            self.turn_left()

        self.move_forward()

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % 4

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % 4

    def move_forward(self):
        d_row, d_col = DIRECTIONS[self.direction_index]
        self.row += d_row
        self.col += d_col


def run_simulation():
    board = Board(BOARD_SIZE)
    center = BOARD_SIZE // 2
    ant = Ant(board, center, center, direction_index=0)  # mirando hacia arriba

    iteration = 0

    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(board.to_rgb_array())
    title = ax.set_title(f"Hormiga de Langton — Iteración: {iteration}")
    ax.axis("off")

    def render():
        array = board.to_rgb_array()
        if ant.alive and board.is_inside(ant.row, ant.col):
            array[ant.row][ant.col] = COLOR_ANT
        im.set_data(array)
        title.set_text(f"Hormiga de Langton — Iteración: {iteration}")

    def update(frame):
        nonlocal iteration
        if ant.alive:
            for _ in range(STEPS_PER_FRAME):
                was_inside = board.is_inside(ant.row, ant.col)
                ant.step()
                iteration += 1
                if not ant.alive and was_inside:
                    print(f"La hormiga salió del tablero en el paso {frame}.")
                elif not ant.alive:
                    print(f"La hormiga desapareció totalmente en el paso {frame}. Simulación detenida.")
                    anim.event_source.stop()
                    break
            render()
        return [im, title]

    anim = animation.FuncAnimation(
        fig, update, interval=ANIMATION_SPEED, blit=False, cache_frame_data=False
    )
    plt.show()
    return anim


if __name__ == "__main__":
    run_simulation()
