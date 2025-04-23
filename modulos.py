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