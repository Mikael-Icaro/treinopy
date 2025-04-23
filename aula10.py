#Aula 10 - Condições simples e compostas
#if e else 

#nome = str(input("Qual é o seu nome? ")).strip()
#if nome == "Gustavo":
#    print ('Que nome bonito você tem !')
#print ('Bom dia {} como você está ?'.format(nome))


#Exercicio28
#Escreva um programa que faça o computador "pensar" um numero inteiro entre 0 a 5 e peça para o usuario tentar descobrir-
#qual foi o numero escolhido pelo computador . O programa devera escrever na tela se o usuario venceu ou perdeu 
#import random 
#random.randint = gera um numero aleatorio entre dois numeros
#computador = random.randint(0, 5)  # computador escolhe um numero entre 0 e 5
#print ("Vou pensar em um numero entre 0 e 5. Tente adivinhar !!")
#jogador = int(input("Em que numero eu pensei ? "))
#if jogador == computador:
#    print("Parabéns, você acertou!")
#else:
#    print("Você errou! Eu pensei no numero {} e não no {}".format(computador, jogador))

# Exercicio 29 ver a explicação 
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre mensagem multado. A multa vai custar R$ 7,00 por cada Km acima de limite
#< = menor que 
#> = Maior que

#velocidade = int(input("Quantos km seu carro chegou ?"))
#if velocidade >= 80: 
#    print ('Você foi multado!!')
#    print ('Por cada km acima do permitido será cobrado R$7,00.')
#    print ('Como você utrapassou o permitido será cobrado R$ {:.2f}'.format(velocidade + 7))
#else:
#    print ('Você não foi multado !')

#Exercicio 30 
#Crie um programa que leia um numero inteiro e mostre na tela se é par ou impar 

#numero = int(input("Digite um numero: "))
#if numero % 2 == 0: #Um numero é par se o resto de divisão por 2 for 0
#    print ('É um numero par ')
#else:
#    print('Não é um numero par')

#exercicio31
#Programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem cobrando R$ 0,50 por km para viagens até 200km e 0,45 para viagens mais longas

#viagem = float(input('Quantos km tem sua viagem ? '))
#if viagem >= 200:
#    print('Sua viagem será R$ {:.2f}'.format(viagem + 0.45 ))
#else:
#    print('Sua viagem custará R$ {:.2f}'.format(viagem + 0.50))

#exercicio32
#faça um programa que leia um ano qualquer e mostre se é bissexto. 
#ano = int(input('Digite um ano: '))
#if ano % 4 == 0 and ano == 100!= or ano % 400 ==00
#    print ('O ano {} é bissexto'.format(ano))
#else:
#    print('O ano {} não é bissexto'.format(ano))

#exercico33 - Leia 3 numeros e mostre qual é o maior e qual é o menor 
#< = menor que 
#> = Maior que

#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite o segundo numero: '))
#n3 = int(input('Digite o terceiro numero: '))
#menor = n1
#if n2<n1 and n2<n3: 
#    menor =  n2
#if n3<n1 and n3<n2:
#    menor = n3
    

#exercicio34 - Pergunte o salario de um funcionario e calcule o valor do seu aumento. Salarios que passe a R$ 1.250,00 calcule um aumento de 10%
#inferior ou iguais aumento de 15%

#salario = float(input('Quanto você ganha ? '))
#print('Certo, você ganha R$ {:.2f}, agora vamos verificar seu seu aumento !!'.format(salario))
#if salario <= 1250:
#    novo = salario + (salario * 15 / 100)
#else:
#    novo = salario + (salario *10 / 100)
#print ('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f} agora'.format (salario, novo))

#exercicio35 - Leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo

#print('-='*20)
#print('Analisador de triangulos')
#print('-='*20)
#r1 = float(input('primeiro seguimento: '))
#r2 = float(input('segundo seguimento:  '))
#r3 = float(input('terceiro seguimento: '))
#if r1 < + r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print ('Os seguimentos acima podem formar um triangulo')
#else:
#    print('Os seguimentos acima não podem formar um triangulo')

