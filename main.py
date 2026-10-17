
# tick tack toe - jogo da velha 

# PvP
# PvE (easy, hard)

# _ | _ | _
# _ | _ | _
#   |   | 

# Tabuleiro 3 x 3 
# X ou O

# 1. Desenha o tabuleiro
# 2. Sorteia o jogador que inicia
#   Primeiro jogador joga
#   Segundo jogador
# 3. A cada jogada, verificar o vencedor
#   3.1 linha (x)
#       xy (0, 0) (1, 0) (2, 0)
#       xy (0, 1) (1, 1) (2, 1)
#       xy (0, 2) (1, 2) (2, 2)
#   3.2 coluna (y)
#       xy (0, 0) (0, 1) (0, 2)
#       xy (1, 0) (1, 1) (1, 2)
#       xy (2, 0) (2, 1) (2, 2)
#   3.3 vertical ->
#       xy (0, 0) (1, 1) (2, 2)
#       xy (2, 2) (1, 1) (0, 0)

import curses

class Game():
    def __init__(self, w: curses.window) -> None:
        self.window: curses.window = w
        
        curses.curs_set(0)

        self.draw_Board()
        self.window.getch()

    def draw_Board(self) -> None:
        # 3x3
        for _ in range(3):
            board = "_|_|_\n"
            if _ == 2: board = " | | "
            
            self.window.addstr(board)

if __name__ == "__main__":
    game = Game
    curses.wrapper(game)
