

with open("./day10/data1.txt") as inp:
    data = inp.read().strip().split("\n")


pairs = ["[]", "()", "<>", "{}"]

# [print(p[0], p[1]) for p in pairs]


# def parse(line):
#     stack = []
#     for char in line:
#         good = False
#         for p in pairs:
#             if char == p[0]:
#                 stack.append(char)
#             elif char == p[1]:
#                 if stack[-1] == p[0]:
#                     stack.pop()
#                     good = True

#     return stack
data1 = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''


POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

FOWARD = {'{': '}', '[': ']', '(': ')', '<': '>'}
REVERSE = {v: k for k, v in FOWARD.items()}


def compute(s: str) -> int:
    lines = s.split("\n")
    total = 0

    for line in lines:
        stack = []
        for c in line:

            if c in FOWARD:
                stack.append(c)
            elif c in REVERSE:
                if stack[-1] != REVERSE[c]:
                    total += POINTS[c]
                    break
                else:
                    stack.pop()

        return total


for line in data1:
    compute(line)
