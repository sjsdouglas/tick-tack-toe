
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
from random import randint

class Game():
    def __init__(self, w: curses.window) -> None:
        self.w: curses.window = w
        self.coords: dict[tuple[int, int], str] = {
            (0, 0): "", (0, 2): "", (0, 4): "",
            (1, 0): "", (1, 2): "", (1, 4): "",
            (2, 0): "", (2, 2): "", (2, 4): ""
        }
        self.difficuty: bool = False # 0 easy, 1 hard
        self.vez: int
        self.vencedor: str = ""
        self.pos_cursor_y = self.pos_cursor_x = 0
        self.move: int = 0
        self.ch_pos_cursor: str = chr(self.w.inch(self.pos_cursor_y, self.pos_cursor_x))
        
        # curses.curs_set(0)

        self.draw_Board()
        # self.player_Actions()
        # self.w.getch()
        self.decide_Turn()

    def draw_Board(self) -> None:
        # 3x3
        for _ in range(3):
            board = "_|_|_\n"
            if _ == 2: board = " | | "
            
            self.w.addstr(board)
        self.w.refresh()

    def draw_Debug(self):
        self.w.addstr(4, 0, f"self.vez: {self.vez}")
        self.w.addstr(5, 0, f"pos_cursor: {(self.pos_cursor_x, self.pos_cursor_y)}")
        self.w.addstr(6, 0, f"keyname: {curses.keyname(self.move).decode():<20}")
        self.w.addstr(7, 0, f"move: {self.move:<20}")
        self.w.addstr(8, 0, f"ch_pos_cursor: {self.ch_pos_cursor:<20}")
        self.w.addstr(9, 0, f"coords: {self.coords}")
        self.w.addstr(10, 0, f"self.vencedor: {self.vencedor}")
        self.w.refresh()


    def player_Actions(self) -> None:
        self.w.move(self.pos_cursor_y, self.pos_cursor_x)
        
        while True:
            self.move = self.w.getch()
            

            # MOVIMENTOS 
            if self.move == curses.KEY_UP and self.pos_cursor_y != 0:
                    self.pos_cursor_y -= 1
            
            elif self.move == curses.KEY_DOWN and self.pos_cursor_y != 2:
                    self.pos_cursor_y += 1
            
            elif self.move == curses.KEY_RIGHT and self.pos_cursor_x != 4:
                    self.pos_cursor_x += 2

            elif self.move == curses.KEY_LEFT and self.pos_cursor_x != 0:
                    self.pos_cursor_x -= 2

            # JOGADAS
            elif self.move == 10 and self.ch_pos_cursor != "X" and self.ch_pos_cursor != "O": # 10: Enter
                self.w.addch(self.pos_cursor_y, self.pos_cursor_x, "X")
                self.coords[self.pos_cursor_y, self.pos_cursor_x] = "X"
                self.w.refresh()
                break
            
            elif self.move == curses.KEY_BACKSPACE:
                break

            # self.ch_pos_cursor = chr(self.w.inch(self.pos_cursor_y, self.pos_cursor_x))

            self.w.move(self.pos_cursor_y, self.pos_cursor_x)

            self.w.refresh()

    def cpu_Actions(self) -> None:
        # sem dificuldade a cpu aleatoriza as jogadas
        if not self.difficuty:
            coords_disponiveis: list[tuple[int, int]] = []
            escolha: int
            jogada_y: int; jogada_x: int

            # OBTEM AS CASAS VAZIAS
            for chave, valor in self.coords.items():
                if valor != "": continue
                coords_disponiveis.append(chave)

            # ESCOLHE UMA CASA VAZIA
            escolha = randint(0, len(coords_disponiveis) - 1)
            jogada_y, jogada_x = coords_disponiveis[escolha]

            # JOGA
            self.coords[jogada_y, jogada_x] = "O"
            self.w.addch(jogada_y, jogada_x, "O")
            self.w.refresh()

        # com dificuldade a cpu joga impedindo a vitoria do player
        else:
             ...

    def verify_Victory(self) -> None:
        possiveis_vitorias = [
            # linha
            [(0, 0), (0, 2), (0, 4)],
            [(1, 0), (1, 2), (1, 4)],
            [(2, 0), (2, 2), (2, 4)],
            # coluna
            [(0, 0), (1, 0), (2, 0)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 4), (1, 4), (2, 4)],
            # vertical
            [(0, 0), (1, 2), (2, 4)],
            [(2, 0), (1, 2), (0, 4)]
        ]

        for pv_coord in possiveis_vitorias:
            if self.coords[pv_coord[0]] == self.coords[pv_coord[1]] == self.coords[pv_coord[2]] != "":
                
                if self.coords[pv_coord[0]] == "X":
                    self.vencedor = "Player 1!"
                else:
                    self.vencedor = "CPU!"

                break

    def decide_Turn(self) -> None:
        # Começa aleatório  cpu: 0  player: 1
        self.vez = randint(0, 1)

        # comecou a cpu
        #   (loop)
        #   vez da cpu
        #   cpu jogou
        #       verifica vitória
        #   vez do player
        #   player jogou
        #       verifica vitória
        while True:
            if self.vez == 0: # CPU
                self.cpu_Actions()
            elif self.vez == 1:
                self.player_Actions()

            self.draw_Debug()

            self.verify_Victory()
            if self.vencedor != "": break

            # muda a vez
            # if vez == 0:
            #     vez = 1
            # else:
                # vez = 0

            self.vez = 0 if self.vez == 1 else 1
            

if __name__ == "__main__":
    game = Game
    curses.wrapper(game)
