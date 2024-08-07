import math
import os

def limpar_terminal():
    """Limpa o terminal dependendo do sistema operacional."""
    os.system('cls')  # Para Windows. Use 'clear' para Unix/Linux/Mac.
    
def produtoEscalar(vet1, vet2):
    """Calcula o produto escalar (ou produto interno) entre dois vetores."""
    result = []
    for i, value in enumerate(vet1):
        # Multiplica elementos correspondentes dos vetores e adiciona ao resultado
        result.append(vet1[i] * vet2[i])
        
    # Retorna a soma dos produtos
    return sum(result)

def norma(vet):
    """Calcula a norma (ou magnitude) de um vetor."""
    # Soma dos quadrados dos elementos e calcula a raiz quadrada
    x = sum(x**2 for x in vet)
    return math.sqrt(x)
        
def anguloVetores():
    """Calcula o ângulo entre dois vetores e exibe os resultados."""
    vet1 = []
    vet2 = []
    print("Insira os 2 vetores pressionando enter a cada eixo\n")
    
    def preencheVetor(vet):
        """Preenche um vetor com 3 valores inseridos pelo usuário."""
        for i in range(3):
            vet.append(int(input()))  # Adiciona um valor inteiro ao vetor
        return vet
    
    vet1 = preencheVetor(vet1)
    vet2 = preencheVetor(vet2)
    
    escalar = produtoEscalar(vet1, vet2)  # Calcula o produto escalar
    
    normas = []
    normas.append(norma(vet1))  # Calcula a norma do primeiro vetor
    normas.append(norma(vet2))  # Calcula a norma do segundo vetor
    
    produto_normas = normas[0] * normas[1]  # Produto das normas dos vetores
    
    cos = escalar / produto_normas  # Cálculo do cosseno do ângulo
    arccos = math.acos(cos)  # Calcula o arco cosseno (em radianos)
    graus = math.degrees(arccos)  # Converte o ângulo de radianos para graus
    
    # Exibe os resultados
    print("cos: {}\nArccos: {}\nGraus: {}".format(cos, arccos, graus))
    
def menu():
    """Exibe um menu e permite ao usuário escolher uma opção."""
    while True:
        try:
            print("1 - Angulo entre vetores\n")
            choice = int(input())  # Solicita a escolha do usuário
            
            if choice == 1:
                anguloVetores()  # Chama a função para calcular o ângulo entre vetores
                return  # Encerra o menu após a execução
        except ValueError:
            print("Insira um valor adequado\n")  # Mensagem de erro para entrada inválida

menu()  # Chama a função para exibir o menu
