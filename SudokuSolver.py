import tkinter as tk
from tkinter import messagebox, simpledialog

import mathimport tkinter as tk
from tkinter import messagebox, simpledialog

import math

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.size = self.get_grid_size()
        self.grid = [[tk.Entry(root, width=3, font=('Arial', 18), justify='center') for _ in range(self.size)] for _ in range(self.size)]
        self.create_grid()
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=self.size, columnspan=self.size, pady=10)

    def get_grid_size(self):
        while True:
            size = tk.simpledialog.askinteger("Input", "Enter grid size (4, 9, or 16 for Sudoku):")
            if size in [4, 9, 16]:
                return size
            else:
                messagebox.showerror("Error", "Invalid grid size! Must be 4, 9, or 16.")

    def create_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].grid(row=i, column=j, padx=2, pady=2)

    def solve_sudoku(self):
        board = [[self.grid[i][j].get() if self.grid[i][j].get() else '.' for j in range(self.size)] for i in range(self.size)]
        solver = Solution(self.size)
        if solver.solve_sudoku(board):
            self.update_board(board)
        else:
            messagebox.showerror("Error", "No solution exists!")

    def update_board(self, board):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].delete(0, tk.END)
                if board[i][j] != '.':
                    self.grid[i][j].insert(0, board[i][j])

class Solution:
    def __init__(self, size):
        self.size = size
        self.grid_size = int(math.sqrt(size))

    def is_safe(self, board, row, col, num):
        num = str(num)
        for i in range(self.size):
            if board[i][col] == num or board[row][i] == num:
                return False
        sr, sc = (row // self.grid_size) * self.grid_size, (col // self.grid_size) * self.grid_size
        for i in range(sr, sr + self.grid_size):
            for j in range(sc, sc + self.grid_size):
                if board[i][j] == num:
                    return False
        return True

    def helper(self, board, row, col):
        if row == self.size:
            return True
        nrow, ncol = (row + 1, 0) if col == self.size - 1 else (row, col + 1)
        if board[row][col] != '.':
            return self.helper(board, nrow, ncol)
        for num in range(1, self.size + 1):
            if self.is_safe(board, row, col, num):
                board[row][col] = str(num)
                if self.helper(board, nrow, ncol):
                    return True
                board[row][col] = '.'
        return False

    def solve_sudoku(self, board):
        return self.helper(board, 0, 0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()


class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.size = self.get_grid_size()
        self.grid = [[tk.Entry(root, width=3, font=('Arial', 18), justify='center') for _ in range(self.size)] for _ in range(self.size)]
        self.create_grid()
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=self.size, columnspan=self.size, pady=10)

    def get_grid_size(self):
        while True:
            size = tk.simpledialog.askinteger("Input", "Enter grid size (4, 9, or 16 for Sudoku):")
            if size in [4, 9, 16]:
                return size
            else:
                messagebox.showerror("Error", "Invalid grid size! Must be 4, 9, or 16.")

    def create_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].grid(row=i, column=j, padx=2, pady=2)

    def solve_sudoku(self):
        board = [[self.grid[i][j].get() if self.grid[i][j].get() else '.' for j in range(self.size)] for i in range(self.size)]
        solver = Solution(self.size)
        if solver.solve_sudoku(board):
            self.update_board(board)
        else:
            messagebox.showerror("Error", "No solution exists!")

    def update_board(self, board):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].delete(0, tk.END)
                if board[i][j] != '.':
                    self.grid[i][j].insert(0, board[i][j])

class Solution:
    def __init__(self, size):
        self.size = size
        self.grid_size = int(math.sqrt(size))

    def is_safe(self, board, row, col, num):
        num = str(num)
        for i in range(self.size):
            if board[i][col] == num or board[row][i] == num:
                return False
        sr, sc = (row // self.grid_size) * self.grid_size, (col // self.grid_size) * self.grid_size
        for i in range(sr, sr + self.grid_size):
            for j in range(sc, sc + self.grid_size):
                if board[i][j] == num:
                    return False
        return True

    def helper(self, board, row, col):
        if row == self.size:
            return True
        nrow, ncol = (row + 1, 0) if col == self.size - 1 else (row, col + 1)
        if board[row][col] != '.':
            return self.helper(board, nrow, ncol)
        for num in range(1, self.size + 1):
            if self.is_safe(board, row, col, num):
                board[row][col] = str(num)
                if self.helper(board, nrow, ncol):
                    return True
                board[row][col] = '.'
        return False

    def solve_sudoku(self, board):
        return self.helper(board, 0, 0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
