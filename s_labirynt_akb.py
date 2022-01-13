lab1 = '''
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
lab2 = '''
###################
#        #  C     #
#######  ####  ####
# # #    #  # ##  #
# # ###  #  # #   #
#     # ## ## ##  #
###   # #  #   #  #
# S ### #  #   #  #
#   #   #  ##  #  #
#                 #
###################
'''
lab3 = '''
#######################################
# S #           #                    C#
#               ###########  ##########
#  ############ #         #  #        #
#  #          # ######### # ##     ####
#   #  ######## ##      # # #    ###  #
#    # #      #  #        # #    #    #
#      #      #  ######## # # # ##    #
#                                     #
#######################################
'''
lab4 = '''
#######################
#S                    #
####################  #
# C #                 #
#  ##             #####
#  #  ##########  #   #
#  #       #          #
#     #############   #
######             ####
'''
lab5 = '''
####################################
#    S ###     ####      ####     C#
# ######    ##      ####       #####
#        ##    ####      ####  #    
##########  #####              #####
'''
lab6 = '''
###############
#S#          C#
###############
'''
lab7 = '''
######################################################
# C #                  #                  #          #
#  ## ################ # ################   ###### S #
#     #                  #                  #        #
#####    ############# # # ############## #  ######  #
#                      #   #        #####         #  #
#####################################    #############
'''
lab8 = '''
####################################
#    S ###     ####      ####     C#
# ######    ##      #####      #####
#        ##    #### #    ####  #    
##########  #####              #####
'''
lab9 = '''
S   #   C
#     ###
'''
lab10 = '''
       #     #                     
    S ###     #####C     ###       
 ######    ##      #####      #### 
        ##    #### #    #######    
                                   
'''
lab11 = '''
# S   C#
'''
lab12 = '''
#
S
 
 
C
#
'''
lab13 = '''
                           #
S#########################  
                            
 ###########################
                            
########################### 
########################### 
                            
 ###########################
 ###########################
       C                    
'''
lab14 = '''
                           #
S#########################  

 ###########################

########################### 
########################### 

 ###########################
 ###########################
       C                    
'''

class Point:
    def __init__(self, row, col):
        '''
        Class Point constructor
        :param row: row
        :param col: col
        '''
        self.row = row
        self.col = col

def funkcja_1(lab: str) -> []:

    def read_lab(lab: str) -> []:
        '''
        func to read labyrinth
        :param lab: labyrinth string
        :return: array with labyrinth info
        '''
        t = [x for x in lab.split('\n') if len(x) > 0]
        return [[t[i][j] for j in range(len(t[0]))] for i in range(len(t))]

    def get_point(tab: [], l: chr) -> Point:
        '''
        func to locate
        :param tab: array with labyrinth info
        :param l: char to find in array
        :return: Point of finding char in array
        '''
        t = [(index, row.index(l)) for index, row in enumerate(tab) if l in row][0]
        return Point(t[0], t[1])

    def mark_point(tab: [], p: Point):
        '''
        func to mark element of tab as used in path
        :param tab: array with labyrinth info
        :param p: Point to mark as used
        '''
        tab[p.row][p.col] = '*'
        pass

    def find_points(tab: [], p: Point) -> []:
        '''
        func to locate not used points around the point
        :param tab: array with labyrinth info
        :param p: Point to find
        :return: list of found points
        '''
        ret = []
        if p.row - 1 >= 0:
            if tab[p.row - 1][p.col] in (' ', 'C'):
                ret.append(Point(p.row - 1, p.col))
        if p.row + 1 < len(tab):
            if tab[p.row + 1][p.col] in (' ', 'C'):
                ret.append(Point(p.row + 1, p.col))
        if p.col - 1 >= 0:
            if tab[p.row][p.col - 1] in (' ', 'C'):
                ret.append(Point(p.row, p.col - 1))
        if p.col + 1 < len(tab[0]):
            if tab[p.row][p.col + 1] in (' ', 'C'):
                ret.append(Point(p.row, p.col + 1))
        return ret

    def is_exit(tab: [], p: Point) -> bool:
        '''
        func to check if the point is exit
        :param tab: array with labyrinth info
        :param p: Point to check
        :return: True if Point is exit
        '''
        return tab[p.row][p.col] == 'C'

    # main part to find a path
    tab = read_lab(lab)
    is_finished = False
    paths = [[get_point(tab, 'S')]]

    while not is_finished:
        is_changed = False
        temp_paths = []
        for pa in paths:
            l = find_points(tab, pa[-1])
            if len(l) > 0:
                is_changed = True
                for i in l:
                    r = pa.copy()
                    r.append(i)
                    temp_paths.append(r)
                    if is_exit(tab, i):
                        is_finished = True
                    else:
                        mark_point(tab, i)
        paths = temp_paths
        if not is_changed:
            is_finished = True

    # return result
    for p in paths:
        if is_exit(tab, p[-1]):
            return p[1:-1]

    return []

def funkcja_2(lab: str, path: []) -> str:

    def read_lab(lab) -> []:
        '''
        func to read labyrinth
        :param lab: labyrinth string
        :return: array with labyrinth info
        '''
        t = [x for x in lab.split('\n') if len(x) > 0]
        return [[t[i][j] for j in range(len(t[0]))] for i in range(len(t))]

    def print_path(tab: [], path: []) -> str:
        '''
        func to print labyrinth with path
        :param tab: array with labyrinth info
        :param path: path to exit
        :return: string to print
        '''
        ret = ""
        for p in path:
            tab[p.row][p.col] = '*'
        for i in range(len(tab)):
            s = ""
            for j in range(len(tab[0])):
                s += tab[i][j]
            s += '\n'
            ret += s
        return ret

    return print_path(read_lab(lab), path)

if __name__ == "__main__":
    print(funkcja_2(lab1, funkcja_1(lab1)))
    print(funkcja_2(lab2, funkcja_1(lab2)))
    print(funkcja_2(lab3, funkcja_1(lab3)))
    print(funkcja_2(lab4, funkcja_1(lab4)))
    print(funkcja_2(lab5, funkcja_1(lab5)))
    print(funkcja_2(lab6, funkcja_1(lab6)))
    print(funkcja_2(lab7, funkcja_1(lab7)))
    print(funkcja_2(lab8, funkcja_1(lab8)))
    print(funkcja_2(lab9, funkcja_1(lab9)))
    print(funkcja_2(lab10, funkcja_1(lab10)))
    print(funkcja_2(lab11, funkcja_1(lab11)))
    print(funkcja_2(lab12, funkcja_1(lab12)))
    print(funkcja_2(lab13, funkcja_1(lab13)))