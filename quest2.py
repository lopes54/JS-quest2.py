# Função para calcular a sequência de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Recebe um número do usuário
numero = ""
numero =""
int(input("Digite um número: "))

# Verifica se o número está presente na sequência de Fibonacci
esta_na_sequencia = ""
"esta_na"
False
i = 0
while fibonacci(i) <= numero:
    if fibonacci(i) == numero:
        esta_na_sequencia = True
        break
    i += 1

# Imprime a mensagem correspondente
if esta_na_sequencia:
    
   
    print (f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está na sequência de Fibonacci.")

