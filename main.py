
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
        self.w: curses.window = w
        self.coords = {
             (0, 0): "", (0, 2): "", (0, 4): "",
             (1, 0): "", (1, 2): "", (1, 4): "",
             (2, 0): "", (2, 2): "", (2, 4): ""
        }
        self.difficuty: bool = False # 0 easy, 1 hard
        
        # curses.curs_set(0)

        self.draw_Board()
        self.player_Actions()
        # self.w.getch()

    def draw_Board(self) -> None:
        # 3x3
        for _ in range(3):
            board = "_|_|_\n"
            if _ == 2: board = " | | "
            
            self.w.addstr(board)
        self.w.refresh()

    def player_Actions(self) -> None:
        pos_cursor_y = pos_cursor_x = 0

        ch_pos_cursor: str = ""

        self.w.move(pos_cursor_y, pos_cursor_x)
        
        while True:
            move = self.w.getch()
            

            # MOVIMENTOS 
            if move == curses.KEY_UP and pos_cursor_y != 0:
                    pos_cursor_y -= 1
            
            elif move == curses.KEY_DOWN and pos_cursor_y != 2:
                    pos_cursor_y += 1
            
            elif move == curses.KEY_RIGHT and pos_cursor_x != 4:
                    pos_cursor_x += 2

            elif move == curses.KEY_LEFT and pos_cursor_x != 0:
                    pos_cursor_x -= 2

            # JOGADAS
            elif move == 10 and ch_pos_cursor != "X" and ch_pos_cursor != "O": # 10: Enter
                self.w.addch(pos_cursor_y, pos_cursor_x, "X")
                self.coords[pos_cursor_y, pos_cursor_x] = "X"
            
            elif move == curses.KEY_BACKSPACE:
                break

            ch_pos_cursor = chr(self.w.inch(pos_cursor_y, pos_cursor_x))
            
            self.w.addstr(5, 0, f"pos_cursor: {(pos_cursor_x, pos_cursor_y)}")
            self.w.addstr(6, 0, f"keyname: {curses.keyname(move).decode():<20}")
            self.w.addstr(7, 0, f"move: {move:<20}")
            self.w.addstr(8, 0, f"ch_pos_cursor: {ch_pos_cursor:<20}")
            self.w.addstr(9, 0, f"coords: {self.coords}")

            self.w.move(pos_cursor_y, pos_cursor_x)

            self.w.refresh()

    def cpu_Actions(self) -> None:
        # sem dificuldade a cpu aleatoriza as jogadas
        if not self.difficuty:
            
            ...            
        # com dificuldade a cpu joga impedindo a vitoria do player
        else:
             ...
            

if __name__ == "__main__":
    game = Game
    curses.wrapper(game)
