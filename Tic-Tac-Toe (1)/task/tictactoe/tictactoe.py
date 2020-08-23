# write your code here
def coord_to_n(x, y):
    return (3 - y) * 3 + (x - 1)


class TicTacToe:
    def __init__(self, state):
        # convert string to list for better accessibility
        self.cells = list(state)

    def finished(self):
        return "_" not in self.cells

    def count_symbol(self, ch):
        return self.cells.count(ch)

    def player_win(self, ch):
        # horizontal
        for i in range(0, 7, 3):
            if self.cells[i] == ch and self.cells[i] == self.cells[i + 1] == self.cells[i + 2]:
                return True

        # vertical
        for i in range(0, 3):
            if self.cells[i] == ch and self.cells[i] == self.cells[i + 3] == self.cells[i + 6]:
                return True

        # diagonal
        return self.cells[0] == ch and self.cells[0] == self.cells[4] == self.cells[8] \
            or self.cells[2] == ch and self.cells[2] == self.cells[4] == self.cells[6]

    def get_status(self):
        if self.player_win("X") and self.player_win("O"):
            return "Impossible"

        if abs(self.count_symbol("X") - self.count_symbol("O")) > 1:
            return "Impossible"

        if self.player_win("X") and self.player_win("O"):
            return "Impossible"

        if self.player_win("X"):
            return "X wins"

        if self.player_win("O"):
            return "O wins"

        if self.finished():
            return "Draw"
        else:
            return "Game not finished"

    def set_point(self, pos_x, pos_y):
        if self.cells[coord_to_n(pos_x, pos_y)] in ["X", "O"]:
            return "This cell is occupied! Choose another one!"

        self.cells[coord_to_n(pos_x, pos_y)] = "X"

    def __str__(self) -> str:
        return "---------\n" \
               f"| {self.cells[0]} {self.cells[1]} {self.cells[2]} |\n" \
               f"| {self.cells[3]} {self.cells[4]} {self.cells[5]} |\n" \
               f"| {self.cells[6]} {self.cells[7]} {self.cells[8]} |\n" \
               "---------"


def parse_input(user_input):

    res = user_input.split()
    if not res[0].isdigit():
        return "You should enter numbers!", None, None

    if not res[1].isdigit():
        return "You should enter numbers!", None, None

    (x, y) = int(res[0]), int(res[1])

    if x not in [1, 2, 3] or y not in [1, 2, 3]:
        return "Coordinates should be from 1 to 3!", None, None

    return None, x, y


# intro
tic_tac = TicTacToe(input("Enter cells: "))
print(tic_tac)

# enter data
while True:
    (msg, x, y) = parse_input(input("Enter the coordinates: "))
    if msg is not None:
        print(msg)
        continue

    msg = tic_tac.set_point(x, y)
    if msg is not None:
        print(msg)
        continue
    else:
        break

print(tic_tac)
