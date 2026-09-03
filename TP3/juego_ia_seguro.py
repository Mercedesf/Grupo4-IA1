import pygame
import random
import math

class TicTacToeBoard:
    def __init__(self):
        self.board = [' '] * 9
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

    def get_available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def make_move(self, index, symbol):
        if self.board[index] == ' ':
            self.board[index] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for combo in self.winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == symbol:
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def copy(self):
        new_board = TicTacToeBoard()
        new_board.board = self.board.copy()
        return new_board

class SimulatedAnnealingAI:
    def __init__(self, ai_symbol, player_symbol):
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol

    def heuristic_evaluation(self, board, ai_symbol, player_symbol):
        if board.check_winner(ai_symbol): return 1000
        if board.check_winner(player_symbol): return -1000

        score = 0
        for combo in board.winning_combinations:
            ai_count = sum(1 for i in combo if board.board[i] == ai_symbol)
            pl_count = sum(1 for i in combo if board.board[i] == player_symbol)

            if ai_count == 2 and pl_count == 0: score += 50
            elif ai_count == 1 and pl_count == 0: score += 10
            if pl_count == 2 and ai_count == 0: score -= 100

        if board.board[4] == ai_symbol: score += 5
        for corner in [0, 2, 6, 8]:
            if board.board[corner] == ai_symbol: score += 2

        return score

    def get_best_move(self, current_board, initial_temp, cooling_rate, iterations=50):
        available_moves = current_board.get_available_moves()
        if not available_moves:
            return None, 0

        current_move = random.choice(available_moves)
        simulated_board = current_board.copy()
        simulated_board.make_move(current_move, self.ai_symbol)
        current_score = self.heuristic_evaluation(simulated_board, self.ai_symbol, self.player_symbol)

        T = initial_temp

        for _ in range(iterations):
            if T <= 0.001: break

            if len(available_moves) > 1:
                neighbor_move = random.choice([m for m in available_moves if m != current_move])
            else:
                neighbor_move = current_move

            neighbor_board = current_board.copy()
            neighbor_board.make_move(neighbor_move, self.ai_symbol)
            neighbor_score = self.heuristic_evaluation(neighbor_board, self.ai_symbol, self.player_symbol)

            delta = neighbor_score - current_score

            if delta > 0:
                current_move = neighbor_move
                current_score = neighbor_score
            else:
                try:
                    probability = math.exp(delta / T)
                except OverflowError:
                    probability = 0

                if random.random() < probability:
                    current_move = neighbor_move
                    current_score = neighbor_score

            T *= cooling_rate

        return current_move, T

class Button:
    def __init__(self, x, y, w, h, text, font, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.action = action
        self.color = (220, 220, 220)
        self.hover_color = (180, 180, 180)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ta-te-ti con Recocido Simulado")
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 60, bold=True)
    font_med = pygame.font.SysFont("Arial", 24, bold=True)
    font_small = pygame.font.SysFont("Arial", 18)

    board = TicTacToeBoard()
    player_symbol = 'X'
    ai_symbol = 'O'
    game_active = False
    current_turn = 'X'

    initial_temp = 20.0
    cooling_rate = 0.85
    current_temp = 0.0
    status_msg = "Configura y presiona Iniciar"

    def toggle_player():
        nonlocal player_symbol
        player_symbol = 'O' if player_symbol == 'X' else 'X'

    def add_temp(): nonlocal initial_temp; initial_temp += 5.0
    def sub_temp(): nonlocal initial_temp; initial_temp = max(1.0, initial_temp - 5.0)
    def add_alpha(): nonlocal cooling_rate; cooling_rate = min(0.99, round(cooling_rate + 0.05, 2))
    def sub_alpha(): nonlocal cooling_rate; cooling_rate = max(0.1, round(cooling_rate - 0.05, 2))

    def start_game():
        nonlocal board, game_active, current_turn, ai_symbol, current_temp, status_msg
        board = TicTacToeBoard()
        ai_symbol = 'O' if player_symbol == 'X' else 'X'
        game_active = True
        current_turn = 'X'
        current_temp = initial_temp
        status_msg = "En Juego - Turno X"

    btn_player = Button(520, 50, 150, 40, "Cambiar: X", font_small, toggle_player)
    btn_t_sub = Button(520, 130, 40, 40, "-", font_med, sub_temp)
    btn_t_add = Button(650, 130, 40, 40, "+", font_med, add_temp)
    btn_a_sub = Button(520, 210, 40, 40, "-", font_med, sub_alpha)
    btn_a_add = Button(650, 210, 40, 40, "+", font_med, add_alpha)
    btn_start = Button(520, 280, 250, 50, "INICIAR PARTIDA", font_med, start_game)
    btn_start.color = (76, 175, 80)
    btn_start.hover_color = (56, 142, 60)

    buttons = [btn_player, btn_t_sub, btn_t_add, btn_a_sub, btn_a_add, btn_start]

    def draw_board(surface):
        pygame.draw.line(surface, (0,0,0), (166, 0), (166, 500), 4)
        pygame.draw.line(surface, (0,0,0), (333, 0), (333, 500), 4)
        pygame.draw.line(surface, (0,0,0), (0, 166), (500, 166), 4)
        pygame.draw.line(surface, (0,0,0), (0, 333), (500, 333), 4)

        for i, symbol in enumerate(board.board):
            if symbol != ' ':
                row, col = i // 3, i % 3
                x = col * 166 + 83
                y = row * 166 + 83
                color = (255, 87, 34) if symbol == 'X' else (33, 150, 243)
                text_surf = font_large.render(symbol, True, color)
                text_rect = text_surf.get_rect(center=(x, y))
                surface.blit(text_surf, text_rect)

    def check_endgame():
        nonlocal game_active, status_msg
        if board.check_winner(player_symbol):
            status_msg = "¡Has Ganado!"
            game_active = False
            return True
        elif board.check_winner(ai_symbol):
            status_msg = "¡La IA Gana!"
            game_active = False
            return True
        elif board.is_full():
            status_msg = "¡Es un Empate!"
            game_active = False
            return True
        return False

    running = True
    ai_delay_timer = 0

    while running:
        screen.fill((245, 245, 245))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_active:
                for btn in buttons:
                    btn.handle_event(event)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if current_turn == player_symbol:
                        mx, my = event.pos
                        if mx < 500:
                            col, row = mx // 166, my // 166
                            idx = row * 3 + col
                            if board.make_move(idx, player_symbol):
                                if not check_endgame():
                                    current_turn = ai_symbol
                                    status_msg = "IA Pensando..."
                                    ai_delay_timer = pygame.time.get_ticks()

        btn_player.text = f"Tu Ficha: {player_symbol}"

        if game_active and current_turn == ai_symbol:
            if pygame.time.get_ticks() - ai_delay_timer > 600:
                ai = SimulatedAnnealingAI(ai_symbol, player_symbol)
                best_move, final_t = ai.get_best_move(board, initial_temp, cooling_rate)
                if best_move is not None:
                    board.make_move(best_move, ai_symbol)
                    current_temp = final_t
                if not check_endgame():
                    current_turn = player_symbol
                    status_msg = f"Tu Turno ({player_symbol})"

        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 500, 500))
        draw_board(screen)
        pygame.draw.line(screen, (0,0,0), (500, 0), (500, 500), 4)

        screen.blit(font_med.render("Configuración IA", True, (0,0,0)), (520, 10))
        if not game_active:
            btn_player.draw(screen)

            screen.blit(font_small.render("Temp. Inicial:", True, (0,0,0)), (520, 100))
            btn_t_sub.draw(screen)
            screen.blit(font_med.render(f"{initial_temp:.1f}", True, (0,0,0)), (575, 135))
            btn_t_add.draw(screen)

            screen.blit(font_small.render("Factor Enfriamiento (α):", True, (0,0,0)), (520, 180))
            btn_a_sub.draw(screen)
            screen.blit(font_med.render(f"{cooling_rate:.2f}", True, (0,0,0)), (575, 215))
            btn_a_add.draw(screen)

            btn_start.draw(screen)

        pygame.draw.rect(screen, (230, 230, 230), (510, 360, 280, 130), border_radius=10)
        screen.blit(font_med.render("Monitor:", True, (0,0,0)), (520, 365))
        screen.blit(font_small.render(f"Temp. Inicial: {initial_temp:.1f}", True, (100,100,100)), (520, 400))
        screen.blit(font_small.render(f"Temp. Actual: {current_temp:.4f}", True, (100,100,100)), (520, 425))

        status_color = (255,0,0) if "Gana" in status_msg or "Empate" in status_msg else (0,150,0)
        screen.blit(font_med.render(status_msg, True, status_color), (520, 455))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
