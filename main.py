from graphics import *
from cell import *
from maze import *

# To fix later: white lines destroy maze walls - subtract a pixel or sth of the sort


def main():
    win = Window(700, 700)
    new_maze = Maze(100, 100, 5, 5, 100, 100, win)
    new_maze.solve()
    input("Press key to exit...")

if __name__ == "__main__":
    main()