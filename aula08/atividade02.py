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

# Solução do professor
def calcula_multa(e):
    multa = e * MULTA_VALOR
    return multa


#Ao invés de colocar multa = e * 4 e escreve Multa_valor e só muda o 4. Esse valor pode sofrer alterações contantes.
MULTA_VALOR = 4.00
LIMITE = 100
peso_pescado = float(input('Peso:'))
if peso_pescado > 100:
    excedente = peso_pescado - 100
    vl_multa = calcula_multa(excedente)
    print(f'Valor da Multa R$ {vl_multa}')
else:
   print(f'Peso {peso_pescado}, Sem Multa')