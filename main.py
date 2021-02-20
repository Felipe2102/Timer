from datetime import datetime
from time import sleep

print('Bem vindo!')
name = input('Qual o nome do evento?' + '\n')
dia = input('Qual o dia do evento?' + '\n')
mes = input('Qual o mês do evento?' + '\n')

while True:
    date = datetime.now()
    if str(date.month) == mes:
        if str(date.day) == dia:
            print(f'o dia do evento {name} chegou!')
            sleep(999)
