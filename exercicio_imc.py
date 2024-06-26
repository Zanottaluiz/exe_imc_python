nome = 'Luiz'
altura = 1.70
peso = 75

imc= peso / (altura * altura)

linha_1 = 'O IMC de ' + nome + ' é:', imc
linha_2 = f'{nome} tem {altura:.1f} de altura'
linha_3 = f'O IMC é de: {imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)