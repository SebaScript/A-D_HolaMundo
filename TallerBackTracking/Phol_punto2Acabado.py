#Phol Castañeda Henao
#ejercicio 2. Programacion Dinamica
import random


def maxPathSum(matrix,col,memo,row=0):
    print("row es:",row)
    print("col es",col)
    if row == len(matrix)-1:
        return matrix[row][col]
    
    
    if memo[row][col] != "":
        print("tomó el valor")
        return memo[row][col]
    
    maxSum = 0
    movements = [(1,0),(1,-1),(1,1)]
    for move in movements:
        if col+move[1] < 0 or col+move[1] == len(matrix):
            continue
        returnedsum = maxPathSum(matrix,col+move[1],memo,row+move[0])
        print("returnedSum es: ",maxSum)
        if returnedsum > maxSum:
            maxSum = returnedsum
    memo[row][col] = maxSum
    
    return matrix[row][col] + maxSum
        


n = 3
matrix = [ [random.randint(15,400) for j in range (n)] for i in range (n)]
#print(matrix)

#matrix = [[12, 35, 2, 1], 
#          [20,  1,  35,6], 
 #         [89, 40,  80,  60],
  #        [78, 10, 98,36]
   #      ]

#movements = [(1,0),(1,-1),(1,1)]

memo = [ ["" for j in range (n)] for i in range (n)]

#memo =  [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
print(memo)

    
print(maxPathSum(matrix,1,memo))

print(memo)
