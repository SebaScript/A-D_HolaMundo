#Dado la dimensión de una matriz cuadrada muestre los valores en forma de caracol o vórtice.
import random


def DisplayVortex(n,matrix,movements=None,contMovements=None,numdirection=0,row=0,col=0,array=[]):
    #print("Entered")
    #print(f"row:{row}\tcol:{col}")
    #print(f"row:{row}\tcol:{col}\tnumber:{matrix[row][col]}")
    #print(f"contMovements es: {contMovements}")
    #print(f"movements es: {movements}")
    #print(array)
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    if len(array) == n*n:
        return array
    array.append(matrix[row][col])

    #bottom left corner
    if row == n-1 and col == 0:
        movements = (n-1)*2
        numdirection=1
        row+=direction[numdirection][0]
        col+=direction[numdirection][1]
        return DisplayVortex(n,matrix,movements,1,numdirection,row,col,array)
    
    if not movements:
        return DisplayVortex(n,matrix,movements,None,0,row+1,col,array)
    
    if contMovements == movements/2:
        #print("Entró a el condicional del contador mitad")
        if numdirection == 3:
            numdirection = 0
        else:
            numdirection+=1
        row+=direction[numdirection][0]
        col+=direction[numdirection][1]
        return DisplayVortex(n,matrix,movements,contMovements+1,numdirection,row,col,array)
    
    elif contMovements == movements:
        #print("Entró a el condicional del contador igual")
        if numdirection == 3:
            numdirection = 0
        else:
            numdirection+=1
        row+=direction[numdirection][0]
        col+=direction[numdirection][1]
        movements= ((movements/2)-1)*2
        contMovements=1
        return DisplayVortex(n,matrix,movements,contMovements,numdirection,row,col,array)
    
    return DisplayVortex(n,matrix,movements,contMovements+1,numdirection,row+direction[numdirection][0],col+direction[numdirection][1],array)
    
    

#matriz = [[random.randint(0, 9) for _ in range(3)] for _ in range(3)]

"""matriz = [[8, 7, 8, 4, 3],
          [7, 6, 5, 0, 8],
          [9, 6, 0, 5, 6],
          [0, 7, 1, 4, 1],
          [5, 1, 7, 0, 5]]"""

matriz = [[1, 2, 3, 5 ],
          [4, 5, 6, 7],
          [7, 8, 9, 8 ],
          [2, 1, 4, 3 ]
         ]

#result : [1,4,7,2,1,4,3,8,7,5,3,2,5,8,9,6]
for fila in matriz:
    print(fila)

arrayResult = DisplayVortex(len(matriz),matriz)

print("result: ", arrayResult)




    

        




    