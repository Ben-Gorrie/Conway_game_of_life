
import copy


from time import sleep
def get_number_of_neighbours(grid, row_index, col_index):
    number = 0
    try:
        if grid[row_index + 1][col_index] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index + 1][col_index + 1] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index + 1][col_index - 1]  == 1:
            number += 1
    except:
        pass 
    try:
        if grid[row_index - 1][col_index + 1] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index - 1][col_index] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index - 1][col_index - 1] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index][col_index - 1] == 1:
            number += 1
    except:
        pass
    try:
        if grid[row_index][col_index + 1] == 1:
            number += 1
    except:
        pass
    return number


def survive(grid, next_grid):
    for row_index in range(len(grid)):
        for col_index in range(len(grid)):
            if grid[row_index][col_index] == 1:
                neighbours = get_number_of_neighbours(grid, row_index, col_index)
                if neighbours == 2 or neighbours == 3:
                    next_grid[row_index][col_index] = 1
    return next_grid

def reproduce(grid, next_grid):
    for row_index in range(len(grid)):
        for col_index in range(len(grid)):
            neighbours = get_number_of_neighbours(grid, row_index, col_index)
            if neighbours == 3:
                next_grid[row_index][col_index] = 1
    return next_grid

def get_number_of_live_cells(grid):
    number = 0
    for row_index in range(len(grid)):
        for col_index in range(len(grid)):
            if grid[row_index][col_index] == 1:
                number += 1
    return number

def main():
    size = 8
    grid = [[0 for x in range(size)] for x in range(size)]

    next_grid = [[0 for x in range(size)] for x in range(size)]

    
    grid[3][2] = 1
    grid[3][3] = 1

    for row in grid:
        print(row)

    print("-"*50)
    while get_number_of_live_cells(grid) != 0:

        next_grid = survive(grid, next_grid)

        next_grid = reproduce(grid, next_grid)
        for row in next_grid:
            print(row)

        print("-"*50)

        grid = next_grid

        next_grid = [[0 for x in range(size)] for x in range(size)]
        sleep(1)


    
main()

