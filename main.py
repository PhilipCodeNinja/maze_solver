from graphics import *
from cell import *
from maze import *

def main():
    win = Window(700, 700)
    new_maze = Maze(100, 100, 5, 5, 100, 100, win)
    input("Press key to exit...")

if __name__ == "__main__":
    main()