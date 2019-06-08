from collections import Counter
class Solution:
    #Runtime: O(n^3)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            #Get numbers from curr row
            currRow = [x for x in board[r] if x.isnumeric()]
            #Return false if dupes
            if len(set(currRow)) < len(currRow):
                print('dupe0')
                return False
            for c in range(len(board[0])):
                #If greater than 9 or less than 1
                if board[r][c].isnumeric() and (int(board[r][c])>9 or int(board[r][c])<1):
                    print('dupe1')
                    return False
                #Get numbers from curr col
                if r == 0:
                    currCol = [x[c] for x in board if x[c].isnumeric()]
                #Return false if dupes
                if len(set(currCol)) < len(currCol):
                    print('dupe2')
                    return False
                mini = []  #If on 3x3 boundary, add to mini grid
                if not c % 3 and not r % 3:
                    for row in range(r, r+3):
                        for col in range(c, c+3):
                            if board[row][col].isnumeric(): 
                                mini.append(board[row][col])
                    print('mini', mini)
                    if len(set(mini)) < len(mini):
                        print('mini:', mini)
                        return False
        return True
                
                
                
                
            
        
                
                