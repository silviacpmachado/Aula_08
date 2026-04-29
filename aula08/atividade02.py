# função - o que eu crio e só eu vejo
def calculo_da_multa (p):
    r = (peso - 100) * 4
    return r      
       
# inicio - o que vai rodar

peso = float(input('Digite o peso em kg: '))

if peso > 100:
    multa = calculo_da_multa(peso)
    print(f'Peso excedido e o valor da multa é de R$ {multa:.2f}')
else:
    print('Sem peso excedente')