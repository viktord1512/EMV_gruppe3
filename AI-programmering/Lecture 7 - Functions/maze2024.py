import pygame
import random

def create_grid(width, height):
    grid = []
    # Mulighed 1:
    # for row in range(height):
    #     grid.append([])
    #     for col in range(width):
    #         grid[-1].append(0)

    # Mulighed 2:
    # for row in range(height):
    #     grid.append([0 for col in range(width)])
    
    # Mulighed 3:
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
                pygame.draw.rect(screen, (0, 0, 0), position+size)

def create_maze(grid):
    # Draw borders
    grid = draw_line(grid, (0, 0), (0, len(grid)-1))
    grid = draw_line(grid, (0, 0), (len(grid[0])-1, 0))
    grid = draw_line(grid, (0, len(grid)-1), (len(grid[0])-1, len(grid)-1))
    grid = draw_line(grid, (len(grid[0])-1, 0), (len(grid[0])-1, len(grid)-1))

    # Draw walls
    for col in range(2, len(grid[0])-1, 2):
        divide = random.randrange(5, len(grid)-5)
        grid = draw_line(grid, (col, 0), (col, divide))
        grid = draw_line(grid, (col, divide+2), (col, len(grid)-1))

    return grid

def main():
    grid = create_grid(64, 48)
    #grid = draw_line(grid, (15, 2), (15, 30))
    grid = create_maze(grid)

    pygame.init()
    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size)

    while True:
        screen.fill((255,255,255))

        draw_grid(screen, grid)

        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()


if __name__ == "__main__":
    main()