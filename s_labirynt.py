lab = '''
#####################
#                   #
#            #      #
#######      #  C   #
#            #      #
#     #             #
#     #             #
#     #             #
#     #             #
#     #             #
#     ###########   #
#             S #   #
#               #   #
#####################
'''

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __repr__(self):
        return "({},{})".format(self.row, self.col)

t = [x for x in lab.split('\n') if len(x) > 0]
lcol = len(t[0])
lrow = len(t)

def read_lab() -> []:
    tab = [[0 for i in range(lcol)] for j in range(lrow)]

    for i in range(lrow):
        for j in range(lcol):
            if t[i][j] == '#':
                tab[i][j] = 8
            elif t[i][j] == 'S':
                tab[i][j] = 1
            elif t[i][j] == 'C':
                tab[i][j] = 2
    return tab



tab = read_lab()

def get_point(t:[], l:int) -> Point:
    for i in range(lrow):
        for j in range(lcol):
            if t[i][j] == l:
                return Point(i, j)
    raise Exception("Point not found error")

def mark_point(t:[], p:Point):
    t[p.row][p.col] = '3'
    return

def find_points(t:[], p:Point) -> []:
    '''
    find any valid spaces around point
    :param t: labirynth table
    :param p: point
    :return: list of valid points around point
    '''
    ret = []
    if t[p.row][p.col] == 8:
        raise Exception("Point in wrong position")
    if t[p.row - 1][p.col] in (0, 2):
        ret.append(Point(p.row - 1, p.col))
    if t[p.row + 1][p.col] in (0, 2):
        ret.append(Point(p.row + 1, p.col))
    if t[p.row][p.col - 1] in (0, 2):
        ret.append(Point(p.row, p.col - 1))
    if t[p.row][p.col + 1] in (0, 2):
        ret.append(Point(p.row, p.col + 1))
    return ret

def is_exit(t:[], p:Point) -> bool:
    return t[p.row][p.col] == 2


is_finished = False
paths = [[get_point(tab, 1)]]

while not is_finished:
    temp_paths = paths.copy()
    for p in paths:
        l = find_points(tab, p[-1])
        if len(l) > 0:
            for i in l:
                r = p.copy()
                r.append(i)
                temp_paths.append(r)
                if is_exit(tab, i):
                    is_finished = True
                else:
                    mark_point(tab, i)
    paths = temp_paths.copy()


def print_path(tab:[], path:[]) -> str:
    t = tab.copy()
    ret = ""

    for p in path:
        if t[p.row][p.col] == 0:
            t[p.row][p.col] = 3

    for i in range(lrow):
        s = ""
        for j in range(lcol):
            if t[i][j] == 8:
                s += '#'
            elif t[i][j] == 3:
                s += '*'
            elif t[i][j] == 1:
                s += 'S'
            elif t[i][j] == 2:
                s += 'C'
            else:
                s += ' '
        s += '\n'
        ret += s
    return ret



for p in paths:
    tab = read_lab()

    if is_exit(tab, p[-1]):
        print(print_path(tab, p))


def funkcja_1(lab:str) -> []:
    t = [x for x in lab.split('\n') if len(x) > 0]
    lcol = len(t[0])
    lrow = len(t)

    def read_lab() -> []:
        tab = [[0 for i in range(lcol)] for j in range(lrow)]

        for i in range(lrow):
            for j in range(lcol):
                if t[i][j] == '#':
                    tab[i][j] = 8
                elif t[i][j] == 'S':
                    tab[i][j] = 1
                elif t[i][j] == 'C':
                    tab[i][j] = 2
        return tab

    tab = read_lab()

    def get_point(t: [], l: int) -> Point:
        for i in range(lrow):
            for j in range(lcol):
                if t[i][j] == l:
                    return Point(i, j)

    def mark_point(t: [], p: Point):
        t[p.row][p.col] = '3'
        return

    def find_points(t: [], p: Point) -> []:
        ret = []
        if t[p.row][p.col] == 8:
            raise Exception("Point in wrong position")
        if t[p.row - 1][p.col] in (0, 2):
            ret.append(Point(p.row - 1, p.col))
        if t[p.row + 1][p.col] in (0, 2):
            ret.append(Point(p.row + 1, p.col))
        if t[p.row][p.col - 1] in (0, 2):
            ret.append(Point(p.row, p.col - 1))
        if t[p.row][p.col + 1] in (0, 2):
            ret.append(Point(p.row, p.col + 1))
        return ret

    def is_exit(t: [], p: Point) -> bool:
        return t[p.row][p.col] == 2

    is_finished = False
    paths = [[get_point(tab, 1)]]

    while not is_finished:
        temp_paths = paths.copy()
        for p in paths:
            l = find_points(tab, p[-1])
            if len(l) > 0:
                for i in l:
                    r = p.copy()
                    r.append(i)
                    temp_paths.append(r)
                    if is_exit(tab, i):
                        is_finished = True
                    else:
                        mark_point(tab, i)
        paths = temp_paths.copy()

    for p in paths:
        if is_exit(tab, p[-1]):
            return p[1:-1]

    pass

print(funkcja_1(lab))


def funkcja_2(lab:str, path:[]):

    pass