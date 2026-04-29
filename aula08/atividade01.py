def dobro(a):
    r = a * 2
    return r    


n1 = int(input('Número 1: '))


resposta = dobro(n1)
print(f'O resultado é {resposta}')

#feito pelo professor - calculo o dobro
# def dobro(n):
#     d = n * 2
#     return d
    

# num = int(input('Informe o número:'))
# resp = dobro(num)
# print(resp)

#calculo o quadrado
def quadrado(n):
     d = n ** 2
     return d
    

num = int(input('Informe o número:'))
resp = quadrado(num)
print(resp)