'''
km = int(input())

if(km>80):
    print("Você foi Multado!")
    print("Valor da multa R$"+str((km-80)*5)+",00")
'''

vel = float(input('Velocidade em km/h: '))

if vel > 80: 
  multa = (vel-80)*5
  print('*'*20)
  print(f'VOCÊ FOI MULTADO\n MULTA: R${multa:.1f}\n {vel:.0f} km/h')
  print('*'*20)
else:
  print('Tudo ok.')