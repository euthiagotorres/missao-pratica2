# Variável de controle do laço while
saida = ''

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço while para continuar ou sair do programa
while saida.lower() != 'n':
    # Solicitando entradas do usuário
    print('CALCULADORA')
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /) ou o nome da operação (adicao, subtracao, multiplicacao, divisao): ")
    
    # Chamando a função calculadora
    resultado = calculadora(num1, num2, operacao)
    
    # Exibindo o resultado
    print(f'Resultado da operação: {resultado}')
    
    # Perguntando ao usuário se deseja continuar
    saida = input("Deseja continuar? (S/N): ")