from graphics import *
from cell import*

def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(100,100,200,200)

    win.wait_for_close()

if __name__ == "__main__":
    main()