# Author: Alexander Hatfield, ahatfield2016@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Save the Manatee(Game)

from sys import *
from urllib import request
import re


def open_file(filename):

    file = open(filename, "r")              # .map file is imported
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    file.close()
    return grid                             # Grid is returned to main as a list of strings

def main():


    grid = open_file("contest1.map")

    boat_indices = []
    man_pos = (0, 0)
    gate_pos = (0, 0)
    flower_total = 0
    flower_count = 0
    # for i in grid:
    #   print(i)
    for i in range(len(grid)):
        # print(i)
        for j in range(len(grid)):
            # print(j)
            if grid[i][j] == '*':
                boat_tup = (i, j)
                #print(test_tup)
                boat_indices.append(boat_tup)
            if grid[i][j] == 'M':
                man_pos = (i, j)
                #print(test_tup)
            if grid[i][j] == 'G':
                gate_pos = (i, j)
            if grid[i][j] == '\\':
                flower_total += 1

    #for i in grid:
     #  print(i)
    man_inj = False
    score = 0
    man_dest = (0, 0)

    while not man_inj:
        for i in grid:
            print(i)
        man_move = stdin.readline()
        score -= 1
        if man_move == "A\n":
            score += (flower_count * 25)
            stdout.write("quit " + str(score) + "\n")
            quit()
        elif man_move == "L\n":
            man_dest = (man_pos[0], man_pos[1] - 1)
        elif man_move == "R\n":
            man_dest = (man_pos[0], man_pos[1] + 1)
            #new_man_pos = calc_man_posD(man_pos, man_dest, grid, boat_indices)
        elif man_move == "U\n":
            man_dest = (man_pos[0] - 1, man_pos[1])
            #new_man_pos = calc_man_pos(man_pos, man_dest, grid, boat_indices)
        elif man_move == "D\n":
            man_dest = (man_pos[0] + 1, man_pos[1])
            #new_man_pos = calc_man_pos(man_pos, man_dest, grid, flower_count)
        elif man_move == "W\n":
            continue
        new_man_pos = calc_man_pos(man_pos, man_dest, grid, flower_count, boat_indices)

        man_pos = new_man_pos[0]
        grid = new_man_pos[1]
        flower_count = new_man_pos[2]

        if flower_total == flower_count:
            grid[gate_pos[0]][gate_pos[1]] = 'O'

        if man_pos == gate_pos:
            score += (50 + flower_count * 25)
            stdout.write("win " + str(score) + "\n")
            exit()
        boat_indices = new_man_pos[3]
        new_pos = calc_boat_moves(grid, boat_indices)

        grid = new_pos[0]
        boat_indices = new_pos[1]
        man_inj = new_pos[2]

    stdout.write("injured " + str(score) + '\n')


def calc_man_pos(man_pos, man_dest, grid, flower_count, boat_indices):
    # print(man_pos)
    # print(man_dest)
    man_push = 0
    if man_pos[1] - man_dest[1] > 0:
        man_push = 0                                        # manatee moves left
    else:
        man_push = 1                                        # manatee moves right
    if (grid[man_dest[0]][man_dest[1]] == "#") | (grid[man_dest[1]][man_dest[1]] == "G"):
        return man_pos, grid, flower_count, boat_indices
    if grid[man_dest[0]][man_dest[1]] == "*":
        if man_push == 0:
            if grid[man_dest[0]][man_dest[1] - 1] == " ":
                grid[man_pos[0]][man_pos[1]] = " "
                grid[man_dest[0]][man_dest[1]] = "M"
                boat_indices = update_boat_indices((man_dest[0], man_dest[1]), boat_indices, (man_dest[0], man_dest[1] - 1))
        elif man_push == 1:
            if grid[man_dest[0]][man_dest[1] + 1] == " ":
                grid[man_pos[0]][man_pos[1]] = " "
                grid[man_dest[0]][man_dest[1]] = "M"
                boat_indices = update_boat_indices((man_dest[0], man_dest[1]), boat_indices, (man_dest[0], man_dest[1] + 1))

        return man_dest, grid, flower_count, boat_indices
    if grid[man_dest[0]][man_dest[1]] == ".":
        grid[man_pos[0]][man_pos[1]] = " "
        grid[man_dest[0]][man_dest[1]] = "M"
        return man_dest, grid, flower_count, boat_indices
    if grid[man_dest[0]][man_dest[1]] == "\\":
        flower_count = flower_count + 1
        grid[man_pos[0]][man_pos[1]] = " "
        grid[man_dest[0]][man_dest[1]] = "M"
        return man_dest, grid, flower_count, boat_indices
    if grid[man_dest[0]][man_dest[1]] == " ":
        grid[man_pos[0]][man_pos[1]] = " "
        grid[man_dest[0]][man_dest[1]] = "M"
        return man_dest, grid, flower_count, boat_indices
    if grid[man_dest[0]][man_dest[1]] == "O":
        grid[man_pos[0]][man_pos[1]] = " "
        grid[man_dest[0]][man_dest[1]] = "M"
        return man_dest, grid, flower_count, boat_indices


def update_boat_indices(orig_boat_pos, boat_indices, new_boat_pos):
    new_boat_ind = []
    for i in boat_indices:
        if (orig_boat_pos[0], orig_boat_pos[1]) != i:
            new_boat_ind.append(i)
    new_boat_ind.append(new_boat_pos)
    return new_boat_ind

def calc_boat_moves(grid, boat_indices):
    man_inj = False
    for i in boat_indices:
        if grid[i[0] + 1][i[1]] != "#":
            if grid[i[0] + 2][i[1]] == "M":
                man_inj = True
    i = len(boat_indices) - 1
    while i >= 0:
        if grid[boat_indices[i][0] + 1][boat_indices[i][1]] == " ":
            grid[boat_indices[i][0]][boat_indices[i][1]] = " "
            grid[boat_indices[i][0] + 1][boat_indices[i][1]] = "*"
            boat_indices[i] = (boat_indices[i][0] + 1, boat_indices[i][1])
        elif grid[boat_indices[i][0] + 1][boat_indices[i][1]] == "*":
            if grid[boat_indices[i][0] + 1][boat_indices[i][1] - 1] == " ":
                grid[boat_indices[i][0]][boat_indices[i][1]] = " "
                grid[boat_indices[i][0] + 1][boat_indices[i][1] - 1] = "*"
                boat_indices[i] = (boat_indices[i][0] + 1, boat_indices[i][1] - 1)
            elif grid[boat_indices[i][0] + 1][boat_indices[i][1] - 1] == " ":
                grid[boat_indices[i][0]][boat_indices[i][1]] = " "
                grid[boat_indices[i][0] + 1][boat_indices[i][1] + 1] = "*"
                boat_indices[i] = (boat_indices[i][0] + 1, boat_indices[i][1] + 1)
        else:
            return grid, boat_indices, man_inj
        i -= 1

    return grid, boat_indices, man_inj


main()
