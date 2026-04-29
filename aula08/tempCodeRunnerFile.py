def calcula_multa(e):
    multa = e * 4
    return multa

LIMITE = 100
peso_pescado = float(input('Peso:'))
if peso_pescado > 100:
    excedente = peso_pescado - 100
    vl_multa = calcula_multa(excedente)
    print(f'Valor da Multa R$ {vl_multa}')
else:
   print(f'Peso {peso_pescado}, Sem Multa')