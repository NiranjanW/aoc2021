with open("./day13/data1.txt") as inp:
    dots = set()
    while True:
        line =   inp.readline().strip()
        if line == "":
            break
        dots.add( tuple([int(i)for i in line.split(",")]))
    print(dots)

    folds = []
    while True:
        line =   inp.readline().strip()
        if line == "":
            break
        fold = line[len("fold along "):]
        if fold[0] == "y":
            folds.append((0,int(fold[2:])))
        else:
            folds.append((int(fold[2:]),0))
print(folds)

def reflect(point,line):
    if line[0] != 0:
        return (2*line[0]-point[0] , point[1])
    return (point[0] ,2*line[1]-point[1])

for fold in folds:

    new_dots = set()
    for dot in dots:
        if fold[0] != 0:
            #Vertical fold
            if dot[0] > fold[0]:
                new_dots.add(reflect(dot,fold))
            else:
                new_dots.add(dot)
        else:
            #Horizontal fold
             if dot[1] > fold[1]:
                new_dots.add(reflect(dot,fold))
             else:
                new_dots.add(dot)

print(new_dots)