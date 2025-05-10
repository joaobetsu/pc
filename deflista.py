def soma(num1, num2 : int):
    print(num1 + num2)
 
def conversor_temperatura(temp : float, conv):
    if conv == "kelvin":
        print(f"{temp + 273}")
    elif conv == "fahrenheit":
        print(f"{(temp * 1.8) + 32}")

def fatorial(numero : float):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero -1)

def eh_palindromo(texto : str):
    texto1 = texto.replace(" ", "").lower()
    t = texto1.replace("", ".")
    pal = t.split(".")
    pal.remove(pal[-1])
    pal.remove(pal[-1])
    rever = pal[::-1]
    if pal == rever:
        return True
    else:
        return False
    
def fibonacci(n):
    lista = [0, 1]
    while True:
        proximo = lista[-1] + lista[-2]
        if proximo > n:
            break
        lista.append(proximo)
    return lista if n >= 1 else [0]

def primos_entre(a, b):
    primos = []
    for i in range(a, b + 1):
        if i > 1:
            for x in range(2, int(i **  0.5) + 1):
                if i % x == 0:
                    break
            else:
                primos.append(i)
    return primos

def prefixo_comum(palavras):
    if len(palavras) == 0:
        return ""
    prefixo = palavras[0]
    for i in palavras[1:]:
        while i[:len(prefixo)] != prefixo:
            prefixo = prefixo[:-1]
            if len(prefixo) == 0:
                return ""
    return prefixo

def valida_cpf(num : str):
    cpf = num
    ultimo = cpf.replace("", ".")
    lista_cpf = ultimo.split(".")
    lista_cpf.remove(lista_cpf[-1])
    lista_cpf.remove(lista_cpf[-1])
    lista_validacao = [int(lista_cpf[-2]), int(lista_cpf[-1]) ]
    lista = []
    for n in range(len(lista_cpf) - 2):
        lista.append(lista_cpf[n])

    multiplicacoes = []
    for n in range(2, 11):
       multi = n * int(lista[-1])
       multiplicacoes.append(multi)
       lista.pop() #tira o ultimo indice da lista
    soma = 0
    for numero in multiplicacoes:
        soma += numero
    div1 = soma % 11 
    digito1 = 11 - div1
    if digito1 >= 10:
        digito1 = 0
    cpf2 = num
    ultimo2 = cpf2.replace("", ".")
    lista_cpf2 = ultimo2.split(".")
    lista_cpf2.remove(lista_cpf2[-1])
    lista_cpf2.remove(lista_cpf2[-1])
    lista_validacao2 = [lista_cpf2[-2], lista_cpf2[-1] ]
    lista2 = []
    for n in range(len(lista_cpf2) - 1):
        lista2.append(lista_cpf2[n])
    multiplicacoes2 = []
    for n in range(2, 12):
        multi2 = n * int(lista2[-1])
        multiplicacoes2.append(multi2)
        lista2.pop()
    soma2 = 0
    for numero2 in multiplicacoes2:
        soma2 += numero2
    div2 = soma2 % 11 
    digito2 = 11 - div2
    if digito2 >= 10:
        digito2 = 0
    verificacao = []
    verificacao.append(digito1)
    verificacao.append(digito2)

    if verificacao == lista_validacao:
        return "Cpf valido!"
    else:
        return "Cpf Invalido!"