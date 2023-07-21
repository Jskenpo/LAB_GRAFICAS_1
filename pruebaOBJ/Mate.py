def MultiplicarMatrices(M1, M2):
    #Multiplicacion de matrices 4x4
    resultado = [[0, 0, 0, 0] for _ in range(4)]  # Crear una matriz de 4x4 llena de ceros

    for i in range(4):
        for j in range(4):
            for k in range(4):
                resultado[i][j] += M1[i][k] * M2[k][j]
    return resultado

def Polaris(M1,V1):
    #Multiplicacion de matriz x vector
    resultado = [0] * len(M1)
    for i in range(len(M1)):
        for j in range(len(V1)):
            resultado[i] += M1[i][j] * V1[j]
    return resultado