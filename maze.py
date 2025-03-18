from cell import Cell
import random
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            current_col = []
            for j in range(self._num_rows):
                current_col.append(Cell(self._win))
            self._cells.append(current_col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        last_col_index = self._num_cols - 1
        last_row_index = self._num_rows - 1
        self._cells[last_col_index][last_row_index].has_bottom_wall = False
        self._draw_cell(last_col_index, last_row_index)

    def _break_walls_r(self, i, j):
        # new lines of code
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # check if there is left:
            if i > 0 and not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            # check if there is right:
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            # check if there is top:
            if j > 0 and not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            # check if there is bottom:
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            # there is none to visit:
            if not to_visit:
                self._draw_cell(i, j)
                return
            else:
                next_i, next_j = random.choice(to_visit)
                # left cell
                if next_i == i - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                # right cell
                if next_i == i + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                # bottom cell
                if next_j == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                # top cell
                if next_j == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                
                
                self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
             for j in range(self._num_rows):
                  self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0,0)
    

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]
        self._cells[i][j].visited = True
        # found final cell
        if i == self._num_cols - 1 and j == self._num_rows - 1: # does this return when it should?
             return True
        # try left
        next_i = None
        next_j = None
        # try left
        if 0 < i and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(to_cell=self._cells[i-1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(to_cell=self._cells[i-1][j], undo=True)          
        # try right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(to_cell=self._cells[i+1][j])
            if self._solve_r(i + 1 ,j):
                return True
            else:
                self._cells[i][j].draw_move(to_cell=self._cells[i+1][j], undo=True)  
        # try down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(to_cell=self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(to_cell=self._cells[i][j+1], undo=True)
        # try up
        if 0 < j and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(to_cell=self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(to_cell=self._cells[i][j-1], undo=True)
        # false else
        return False
        
