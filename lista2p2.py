import deflista

print("Bem vindo ao Menu!")
print("1. Soma de Dois Números.")
print("2. Conversor de Temperatura.")
print("3. Fatorial Recursivo.")
print("4. Verificador de Palíndromos.")
print("5. Sequência de Fibonacci até N.")
print("6. Números Primos em Intervalo.")
print("7. Prefixo Comum Mais Longo.")
print("8. Validador de CPF Simplificado.")
print("9. O Mistério dos Sinos.")
print("10. Sair.")
opcao = input("Escolha uma opção entre as que estão acima: ")

if opcao == "1":
    num1 = int(input("Digite o primeiro número da soma: "))
    num2 = int(input("Digite o segundo número da soma: "))
    somacao = deflista.soma(num1, num2)
elif opcao == "2":
    temp = float(input("Qual o valor da temperatura: "))
    conv = input("Para qual temperatura você deseja converter (Kelvin ou Fahrenheit): ").lower()
    conversao = deflista.conversor_temperatura(temp, conv)
elif opcao == "3":
    numero = float(input("Digite o valor para fazer o fatoramento: "))
    print(deflista.fatorial(numero))
elif opcao == "4":
    texto = input("Digite uma palavra: ")
    print(deflista.eh_palindromo(texto))
elif opcao == "5":
    n = int(input("Digite um número: "))
    print(deflista.fibonacci(n))
elif opcao == "6":
    a = int(input("Digite o número para o início do intervalo: "))
    b = int(input("Digite o número para o fim do invervalo: "))
    print(deflista.primos_entre(a, b))
elif opcao == "7":
    entrada = input("Digite as palavras seperadas por vírgulas: ")
    palavras = entrada.replace(" ", "").split(",")
    print(deflista.prefixo_comum(palavras))
elif opcao == "8":
    num = input("Digite o CPF a ser validado: ")
    print(deflista.valida_cpf(num))
elif opcao == "9":
    entradas = []
    while len(entradas) < 5:
        toque = input("Toque: ")
        entradas.append(toque)
    print(deflista.traduz_sinos(entradas))
elif opcao == "10":
    print("Saindo...")
