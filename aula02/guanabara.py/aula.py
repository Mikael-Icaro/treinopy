#a = input("Digite algo:" )
#print ("O tipo primitivo desse valor é ", type(a))
#print ("Só tem espaços ? ", a.isspace())
#print ("É um número ? ", a.isnumeric())
#print ("É alfabético ? ", a.isalpha())
#print ("É alfanumérico ? ", a.isalnum())
#print ("Está em maiúsculas ? ", a.isupper())
#print ("Está em minúsculas ? ", a.islower())
#print ("Está capitalizada ? ", a.istitle())

#Ordem de Precedencia - aula 07
# 1 - () 
# 2 - ** 
# 3 - * / // % 
# 4 - + -  

#n1 = int(input("Digite um valor: "))
#n2 = int(input("Digite outro valor: "))
#s = n1 + n2
#print ("A soma entre {} e {} é igual a {}".format(s))
#\n = quebra a linha
# end = '' não quebra a linha

#Exercicio 5
#n1 = int(input("Digite um numero: "))
#a = n1 - 1
#s = n1 + 1 
#print ("O antecessor de {} é {} e o sucessor é {}".format(n1, a, s))

#Exercicio 6
#n1 = int(input("Digite um numero: "))
#a = n1 * 2
#b = n1 * 3
#c = n1 ** (1/2)
#print ("O dobro de {} é {}, \n  o triplo é {} e a raiz quadrada é {}".format(n1, a, b, c))

#exercicio 7
#n1 = float(input("Qual foi a primeira nota ? "))
#n2 = float(input("Qual foi a segunda nota ? "))
#m = (n1 + n2) / 2
#print ("A média entre {} e {} é igual a {}".format(n1, n2, m))

#exercicio 8

#n1 = float(input("Quantos metros você quer converter ? "))
#km = n1 / 1000
#hm = n1 / 100
#dam = n1 / 10
#dm = n1 * 10
#cm = n1 * 100
#mm = n1 * 1000
#print ("A medida de {}m corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm".format(n1, km, hm, dam, dm, cm, mm))

#exercicio 9 tabuada
#tab = int(input("Digite um número para ver a tabuada: "))
#print ("{} x 1 = {}".format(tab, tab*1))
#print ("{} x 2 = {}".format(tab, tab*2))
#print ("{} x 3 = {}".format(tab, tab*3))
#print ("{} x 4 = {}".format(tab, tab*4))
#print ("{} x 5 = {}".format(tab, tab*5))
#print ("{} x 6 = {}".format(tab, tab*6))
#print ("{} x 7 = {}".format(tab, tab*7))
#print ("{} x 8 = {}".format(tab, tab*8))
#print ("{} x 9 = {}".format(tab, tab*9))
#print ("{} x 10 = {}".format(tab, tab*10))

#============= ou =============

#def tabuada():
#    tab = int(input("Digite um número para ver a tabuada: "))
#    for i in range(1, 11):
#       print ("{} x {} = {}".format(tab, i, tab*i))
#tabuada()

# Modulos

#import bebida = importa o modulo inteiro
#from bebida import cerveja = importa apenas a função cerveja
