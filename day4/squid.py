
from colorama import init, Fore, Back, Style
init()


class Board:

    def __init__(self, nums):
        self.board = [[nums[i, j], False] for j in range(5) for i in range(5)
                      ]

    def __str__(self):
        res = ""
        for row in self.board:
            for e1 in row:
                num = str(e1[0].rjust(3))
                if e1[1]:
                    res += f"{Back.Whie}{Fore.Black}{num}{Style.RESET_ALL}"
                else:
                    res += f"{num}"
            res += "\n"
        return res

    def detect_win(self):
        pass

    def get_score(self, last_called):
        pass

    def mark(self, num):
        pass


def parse_board(lines):
    """
    lines: a list of 5 strings
    """
    return [[int(i) for i in re.split(" +", line.strip())] for line in lines]


with open("./day4/data.txt") as inp:
    data = inp.read().strip().split("\n")

nums = [int(i) for i in data[0].split(",")]
boards = []
i = 2
while i < len(data):
    i = 2
while i < len(data):
    x = parse_board(data[i:i+5])
    boards.append(Board(x))
    i += 6

# Run the simulation!
ans = None
for x in nums:
    for b in boards:
        b.mark(x)
    for b in boards:
        if b.detect_win():
            ans = b.get_score(x)
            break

    if ans != None:
        break

print(ans)
