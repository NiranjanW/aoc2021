import string

with open("./day14/data.txt") as inp:
    raw_data = inp.read().strip().split("\n")

    template = raw_data[0]
    rules = [line.split(" -> ") for line in raw_data[2:]]

    # elements = string.ascii_uppercase
# replace string inplace

    def replace(s):
        new_str = ""
        i = 0
        while i < len(s):
            new_str += s[i]
            for start, end in rules:
                if s[i:i+2] == start:
                    new_str += end
                    break
            i += 1
        return new_str

    for i in range(3):
        template = replace(template)
    print(template)
