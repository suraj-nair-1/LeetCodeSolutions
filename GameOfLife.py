class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board)):
            print board[i]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                neighbors = 0
                if i > 0:
                    if (board[i-1][j] == 1 or board[i-1][j] == 3):
                        neighbors += 1
                if i < len(board)-1:
                    if (board[i+1][j] == 1 or board[i+1][j] == 3):
                        neighbors += 1
                if j > 0:
                    if (board[i][j-1] == 1 or board[i][j-1] == 3):
                        neighbors += 1
                if j < len(board[0])-1:
                    if (board[i][j+1] == 1 or board[i][j+1] == 3):
                        neighbors += 1
                if i > 0 and j > 0:
                    if (board[i-1][j-1] == 1 or board[i-1][j-1] == 3):
                        neighbors += 1
                if i < len(board)-1 and j < len(board[0])-1:
                    if (board[i+1][j+1] == 1 or board[i+1][j+1] == 3):
                        neighbors += 1
                if i < len(board)-1 and j > 0:
                    if (board[i+1][j-1] == 1 or board[i+1][j-1] == 3):
                        neighbors += 1
                if j < len(board[0])-1 and i > 0:
                    if (board[i-1][j+1] == 1 or board[i-1][j+1] == 3):
                        neighbors += 1
                #print board[i][j]
                #print neighbors
                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2
                    
        
        for i in range(0, len(board)):
            print board[i]
            
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
                    
        for i in range(0, len(board)):
            print board[i]
