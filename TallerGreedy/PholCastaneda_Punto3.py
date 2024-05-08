#Phol Castañeda Henao
#Encontrar el mínimo de una lista (divide y vencerás)

def find_minimum(array):
    if len(array)==1:
        return array[0]
    
    izquierda = find_minimum(array[:len(array)//2])
    derecha = find_minimum(array[len(array)//2:])

    if izquierda < derecha:
        return izquierda
    return derecha


def control_find_minimum(a):
    if isinstance(a,list):
        for i in a:
            if ((isinstance(i,int) or isinstance(i,float)) and type(i)!=bool):
                pass
            else:
                return "La lista debe estar compuesta solo por numeros. Intenta nuevamente"
            
        return find_minimum(a) 
    else:
        return "Debes ingresar una lista en la función"


try:
    print(control_find_minimum([-10,4.458,5,2.5,-9,4.3,3,-800.45]))
except:
    print("Ingresa correctamente la lista de numeros")
#print(control_find_minimum(["True"]))

