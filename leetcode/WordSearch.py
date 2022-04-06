def letterCombinations(board, word):
    column = len(board[0])
    row= len(board)
    wordcount= len(word)

    def dfs(r, c, index):
        #print("Board row: "  + str(i)  + " column: " + str(j) + " board letter: " + board[i][j] + " word: " + word[index])
        #if word scan ended 
        if index>=wordcount:
            return True
        # check if it is out of boundary
        # and not match with word
        # and already checked(just in case)
        elif 0<=r<row and 0<=c<column and board[r][c]==word[index]:
            #mark visited avoid it scan it again
            temp = board[r][c]
            board[r][c] = None
            #check if found match
            if dfs(r-1, c, index+1) or dfs(r+1, c, index+1) or dfs(r, c-1, index+1) or dfs(r, c+1,index+1) :
                return True
            #reverse back to original letter
            board[r][c] = temp
        return False

    for r in range(row):
        for c in range(column):
            # 0 mean it restart from first letter in word
            if dfs(r, c, 0):
                return True
    return False

print(letterCombinations([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))