import random

class Queens:
    def __init__(self):
        self.solutions = []
        self.queens = [-1] * 8 

    def find_solutions(self):
        self.backtrack(0)
        return self.solutions
    
    def print_solution(self, index):
        solution = self.solutions[index] 
        for row in range(8):
            for col in range(8):
                if solution[row] == col:
                    print('Q', end=' ')
                else:
                    print('-', end=' ')
            print()

    def safe_pos(self, row, col):
        for r in range(row):
            current_queen_col = self.queens[r]
            if current_queen_col == col:
                return False
            if current_queen_col + r - row == col:
                return False
            if current_queen_col - r + row == col:
                return False 
        return True 
    
    def backtrack(self, row):
        if row == 8:    # We have a solution
            self.solutions.append(self.queens[:])
            return 
        for col in range(8):
            if self.safe_pos(row, col):
                self.queens[row] = col
                self.backtrack(row + 1)
                self.queens[row] = -1


# Test safe_pos method    
# queens = Queens()
# queens.queens = [0, 4, 7, 5, -1, -1 -1, -1]
# print(queens.safe_pos(4, 3))

queens = Queens()
solutions = queens.find_solutions()
print(f"{len(solutions)} found")

rnd = random.randint(0, 91)
print(f"Solution no. {rnd}")
queens.print_solution(rnd)


