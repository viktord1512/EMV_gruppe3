from random import randrange

import pygame as py

def main():
    init_game()
    grid(64, 48)

def init_game():
    py.init()
    global screen
    screen = py.display.set_mode((640, 480))

# Grid der består af 64x48 celler, hver celle kan være 0 eller 1
def grid(width, height):
    grid = []
    grid = [[0 for col in range(width)] for row in range(height)]

    return grid

def draw_line(grid, start_coordinate, end_coordinate):
    assert(start_coordinate[0] == end_coordinate[0] or start_coordinate[1] == end_coordinate[1])

    coordinates = []
    if start_coordinate[0] == end_coordinate[0]:
        # Vertical line
        y_coordinates = range(start_coordinate[1], end_coordinate[1]+1)
        for y in y_coordinates:
            coordinates.append((start_coordinate[0], y))
    elif start_coordinate[1] == end_coordinate[1]:
        # Horizontal line
        x_coordinates = range(start_coordinate[0], end_coordinate[0]+1)
        for x in x_coordinates:
            coordinates.append((x, start_coordinate[1]))

    for c in coordinates:
        grid[c[1]][c[0]] = 1
    
    return grid

def draw_grid(screen, grid):
    size = (10, 10)
    screen.fill((255,255,255))

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 1:
                position = (x*size[0], y*size[1])
                py.draw.rect(screen, (0, 0, 0), position+size)

def create_maze(grid):
    # Draw borders
    grid = draw_line(grid, (0, 0), (0, len(grid)-1))
    grid = draw_line(grid, (0, 0), (len(grid[0])-1, 0))
    grid = draw_line(grid, (0, len(grid)-1), (len(grid[0])-1, len(grid)-1))
    grid = draw_line(grid, (len(grid[0])-1, 0), (len(grid[0])-1, len(grid)-1))

    # Draw walls
    for col in range(2, len(grid[0])-1, 2):
        divide = randrange(5, len(grid)-5)
        grid = draw_line(grid, (col, 0), (col, divide))
        grid = draw_line(grid, (col, divide+2), (col, len(grid)-1))
    return grid



if __name__ == "__main__":
    main()

# main loop
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
py.quit()

