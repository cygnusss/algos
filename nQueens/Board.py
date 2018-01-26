class Board(object):
    def __init__(self,n):
        self.board = []
        self.size = n

        for i in range(0, n):
          self.board.append([])

          for j in range(0, n):
            self.board[i].append(0)

    def printBoard(self):
      print(self.board)

    def placeQueen(self, row, column):
      self.board[row][column] = 1

    def hasAnyRowConflicts(self, i):
      
      row = self.board[i]
      queens = 0

      for column in range(0, self.size - 1):
        
        piece = row[column]

        if piece == 1:
          queens += 1
        
        if queens > 1:
          return True

      return False

    def hasColumnConflicts(self, column):

      queens = 0

      for row in range(0, self.size - 1):

        piece = self.board[row][column]

        if piece == 1:
          queens += 1
        
        if queens > 1:
          return True
      
      return False
    
    def hasDiagonalConflicts(self, row, column):
      True

test = Board(4)

test.placeQueen(0, 1)
test.placeQueen(1, 1)

test.printBoard()