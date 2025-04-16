# Utilizando o módulos 
# import math
# ceil = arredonda para cima ex: 6.7 = 7
# floor = arredonda para baixo  ex: 6.7 = 6
# trunc = elimina a parte fracionária ex: 6.78547 = 6
# pow = potência ex: pow(4, 2) = 16
# sqrt = raiz quadrada ex: sqrt(81) = 9
# factorial = fatorial ex: factorial(5) = 120

#exercico 16 = Crie um programa que leia um numero
#real qualquer pelo teclado e mostre na tela a sua porção inteira.
#import math

#n1 = float(input("Digite um numero: "))

#truncar = math.trunc(n1)
#print ("O numero inteiro é {}".format(truncar))


#Exercicio 17
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


#import math

#catOp = float(input("Digite o valor do primeiro Cateto:"))
#CatAdj = float(input("Digite o valor do Cateto Adjacente:"))

#calculo = math.hypot(catOp, CatAdj)
#print ("A hipotenusa é {}".format(calculo)) 


#Exercicio 18
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#import math 

#angulo = float(input("Digite o angulo:" ))
#seno = math.sin(math.radians(angulo))
#cos = math.cos(math.radians(angulo))
#tan = math.tan(math.radians(angulo))   
#print (f"O angulo de {angulo} tem o SENO de {seno:.2f}")
#print (f"O  angulo de {angulo} tem o COSSENO de {cos:.2f}")
#print (f"O angulo de a {angulo}  tem a TANGENTE de {tan:.2f}")

#Exercicio 19
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

#import random 

#def alunos():
#    n1 = str(input("Qual é o primeiro aluno ?"))
#    n2 = str(input("Qual é o segundo aluno ?"))
#    n3 = str(input("Qual é o terceiro aluno ?"))
#    n4 = str(input("Qual é o quarto aluno ?"))
#    lista = [n1 , n2, n3, n4]
#    sorteio = random.choice(lista) #choice escolhe um item da lista
#    print("O aluno escolhido foi {}".format(sorteio))
#alunos()

#Exercicio 20
#O mesmo professor do desafio anterior quer sortear um dos alunos para apresentar um trabalho que ele fez. Faça um programa que leia o nome dos quatro alunos e mostre o nome do escolhido.

#import random 
#n1 = str(input("Qual é o primeiro aluno ?"))
#n2 = str(input("Qual é o segundo aluno ?"))
#n3 = str(input("Qual é o terceiro aluno ?"))
#n4 = str(input("Qual é o quarto aluno ?"))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)   #shuffle embaralha a lista
#print("A ordem de apresentação será:")
#print(lista)

#exercicio 21
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Para importar o módulo pygame, certifique-se de que ele está instalado no ambiente.
# Você pode instalá-lo usando o comando: pip install pygame
#para instalar o pygame no terminal do VSCode, use o comando: pip install pygame
#import pygame #pygame é um módulo para jogos, mas também pode ser usado para reproduzir áudio.
#pygame.init()
#pygame.mixer.music.load('caminho/para/o/seu/arquivo.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()  # Aguarda até que a música termine de tocar

#FATIANDO STRINGS 
#frase[9] = mostra a letra que está no indice 9
#frase[9:13] = mostra do indice 9 ao 12
#frase[9:21:2] = mostra do indice 9 ao 20 de 2 em 2
#frase[:5] = mostra do começo até o indice 4
#frase[15:] = mostra do indice 15 até o final
#frase[9::3] = mostra do indice 9 até o final de 3 em 3
#ANALISE
#LEN (FRASE) = conta quantos caracteres tem na string
#FRASE.COUNT("O") = conta quantas vezes aparece a letra O
#FRASE.COUNT("O", 0, 13) = conta quantas vezes aparece a letra O do indice 0 ao 13
#FRASE.find("DEO") = mostra o indice onde começa a palavra DEO
#FRASE.FIND("ANDROID") = mostra o indice onde começa a palavra ANDROID, SENÃO ENCONTRAR RETORNA -1
#TRANSFORMAÇÃO 
#frase.replace("Python","Android") = troca a palavra Python por Android
#frase.upper() = transforma tudo em maiusculo
#frase.lower() = transforma tudo em minusculo
#frase.capitalize() = transforma a primeira letra em maiusculo
#frase.title() = transforma a primeira letra de cada palavra em maiusculo
#frase.strip() = remove os espaços do começo e do final
#frase.rstrip() = remove os espaços do final
#frase.lstrip() = remove os espaços do começo
#Divisão 
#frase.split() = divide a frase em palavras
#'-'.join(frase) = junta a frase com o caractere "-"

#exercicio 22
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
#nome = str(input("Qual seu nome ?")).strip()
#print ("Analisando seu nome...")
#print ("Seu nome em maiusculo é {}".format(nome.upper()))
#print ("Seu nome em minusculo é {}".format(nome.lower()))
#print ("Seu nome tem ao todo {} Letras".format(len(nome) - nome.count(" ")))
#print ("Seu primeiro nome é {} e ele tem {} letras".format(nome.split()[0], nome.find(" ")))

#exercicio 23
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Exemplo: digite um número: 1834, unidade: 4, dezena: 3, centena: 8, milhar: 1

#num = int(input("Digite um número de 0 a 9999: "))
#if 0 <= num <= 9999:
#    unidade = num // 1 % 10
#    dezena = num // 10 % 10
#    centena = num // 100 % 10
#    milhar = num // 1000 % 10
#    print(f"Unidade: {unidade}")
#    print(f"Dezena: {dezena}")
#    print(f"Centena: {centena}")
#    print(f"Milhar: {milhar}")
#else:
#    print("Número fora do intervalo de 0 a 9999. Tente novamente.")

# Exercicio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

#cidade = str("Onde você nasceu ?").strip()
#print (cidade[:5].upper() == "SANTO")

# Exercicio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#nome = str(input("Qual é o seu nome ?")).strip()
#print ("Seu nome tem Silva ? {}".format(nome[:6] == 'Silva'))

# Exercicio 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

#frase = str(input("Digite uma frase: ")).upper().strip()
#print ("A letra A aparece {} vezes".format(frase.count("A")))
#print ("A primeira letra A aparece na posção {}".format(frase.find("A") + 1))
#print ("A ultima letra A aparece na posção {}".format(frase.rfind("A") + 1))

#exercio 27

#n = str(input('Digite seu nome completo: ')).strip()
#nome = n.split()
#print ('Muito prazer em te conhecer!')
#print ('Seu primeiro nome é {}'.format(nome[0]))
#print ('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

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


 

