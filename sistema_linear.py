def print_matrix(A):
    for row in A:
        print(["{:.2f}".format(x) for x in row])
    print()

def gauss(A, b):
    n = len(A)
    
    # junta A e b em uma única matriz aumentada
    for i in range(n):
        A[i].append(b[i])
    
    print("\nMatriz inicial (A|b):")
    print_matrix(A)
    
    # Etapa de escalonamento
    for i in range(n):
        # pivô não nulo → se for zero, troca de linha
        if A[i][i] == 0:
            for k in range(i+1, n):  # percorre linhas abaixo
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    break
        
        # normaliza a linha do pivô
        pivot = A[i][i]
        for j in range(i, n+1):
            A[i][j] /= pivot
        
        print(f"Após normalizar linha {i+1} (pivô = {pivot}):") # mostra linha divida pelo pivo
        print_matrix(A)
        
        # zera abaixo do pivô
        for k in range(i+1, n):
            factor = A[k][i]
            for j in range(i, n+1):
                A[k][j] -= factor * A[i][j]
            
            print(f"Zerando elemento da linha {k+1}, coluna {i+1}:") # mostra os valor zerado
            print_matrix(A)
    
    # Substituição regressiva
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1): # começa da ultima linha
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
    
    return x

# -------------------------
# Programa principal
# -------------------------
def main():
    n = int(input("Digite a ordem do sistema (até 10): "))
    if n < 1 or n > 10:
        print("Erro: a ordem deve estar entre 1 e 10.")
        return
    
    print("\nDigite os coeficientes da matriz A:")
    A = []
    for i in range(n):
        linha = list(map(float, input(f"Linha {i+1} (separe por espaço): ").split()))
        if len(linha) != n:
            print("Erro: número de coeficientes inválido.")
            return
        A.append(linha)
    
    print("\nDigite os termos independentes do vetor b:")
    b = list(map(float, input().split()))
    if len(b) != n:
        print("Erro: número de termos independentes inválido.")
        return
    
    sol = gauss(A, b)
    print("Solução final:", [round(val, 4) for val in sol])

if __name__ == "__main__":
    main()