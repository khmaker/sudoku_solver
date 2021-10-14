# coding=utf-8
import sys


class SudokuSolver:
    def __init__(self, nums):
        self.grid = self.nums_to_grid(nums)
        self.find_solution()
    
    def puzzle(self):
        for row in self.grid:
            print(*row, sep='\t')
    
    def solve(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def sudoku(self, row=0, col=0):
        if row == 9 - 1 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if self.grid[row][col] > 0:
            return self.sudoku(row, col + 1)
        for num in range(1, 9 + 1):
            if self.solve(row, col, num):
                self.grid[row][col] = num
                if self.sudoku(row, col + 1):
                    return True
            self.grid[row][col] = 0
        return False
    
    @staticmethod
    def nums_to_grid(nums):
        try:
            nums = list(map(int, nums))
            grid = [nums[n:n + 9] for n in range(0, 9 * 9, 9)]
            return grid
        except (ValueError, IndexError) as e:
            print(e)
            sys.exit(0)

    def find_solution(self):
        return self.puzzle() if self.sudoku() else None


if __name__ == '__main__':
    SudokuSolver(input())
