class Board(object):
    def __init__(self,n):
        self.board = []

        for i in range(0, n):
          self.board.append([])

          for j in range(0, n):
            self.board[i].append(0)

    def printBoard(self):
      print(self.board)


bd = Board(5)
bd.printBoard()