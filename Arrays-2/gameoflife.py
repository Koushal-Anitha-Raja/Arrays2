class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        
        #1--->0---1
        #0-->1--2
        
        
        m=len(board)
        n=len(board[0])
        
        #direction array for the live and dead cells count
        dirs=[[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        
    
        #iterating all the elements in the 2 dimensional matrix in first pass
        for i in range(m):
            for j in range(n):
                #count should re initialize for every element
                count=0
            
            #this is for direction array to check neibouring row and column
            #processing the neighbours
                for r,c in dirs:
                 #this row will hold the row at that moment
                    nr=r+i
                #this is for neibouring column
                    nc=c+j
                
                #boundary check as neibouring row should be greater than one not less than m and nc should be >0 and <n
                    if nr>=0 and nr<m and nc>=0 and nc<n:
                        if board[nr][nc]==-1 or board[nr][nc]==1:
                            count+=1
            
            #if the neighout is one 
                if board[i][j]==1:
                 #this is the condition to be dead
                    if count<2 or count>3:
                    #changing it to -1 if it is dead from alive
                        board[i][j]=-1
                    
                else:
                    #this is the condition when dead cells are becoming alive
                    if count==3:
                        board[i][j]=2
                    
        #second pass            
        for i in range (m):
            for j in range(n):
                #if the cells are dead then the cell value is -1
                if board[i][j]==-1:
                    board[i][j]=0
                #if the value it 2 then the cells are alive
                elif board[i][j]==2:
                    board[i][j]==1
                    
#time complexity:o(m*n)
#space complexity:o(1)
                    
                    
            