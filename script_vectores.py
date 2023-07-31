import math

def producto_escalar(v1, v2):

    ''' 
    Calculo del producto escalar entre dos vectores
    
    '''
    
    return 

def son_ortogonales(v1, v2):
    
    '''
    Verificar si dos vectores dados son ortogonales. 
    
    '''
        
    return

def son_paralelos(v1, v2):

    '''
    Verificar si dos vectores dados son paralelos 
    '''
    
    return 

def calcular_norma(vector):
    
    '''
    Calcular la norma de un vector
    '''

    return 


if __name__ == '__main__': 

    # 1 # Escribir una función que reciba dos vectores y devuelva su producto escalar.
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    resultado = producto_escalar(vector1, vector2)
    print(resultado)


    # 2 # Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
    vector1 = [1, 0, 0]
    vector2 = [0, 0, -2]
    resultado = son_ortogonales(vector1, vector2)
    print(resultado) 

    # 3 # Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
    vector1 = [1, 2, -1]
    vector2 = [2, 4, -2]
    resultado = son_paralelos(vector1, vector2)
    print(resultado)  

    # 4 # Escribir una función que reciba un vector y devuelva su norma.
    vector = [3, 4]
    norma = calcular_norma(vector)
    print(norma) 
