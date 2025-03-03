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

# =========== Exercicio 5 =========== 
#n1 = int(input("Digite um numero: "))
#a = n1 - 1
#s = n1 + 1 
#print ("O antecessor de {} é {} e o sucessor é {}".format(n1, a, s))

# =========== Exercicio 6 ===========
#n1 = int(input("Digite um numero: "))
#a = n1 * 2
#b = n1 * 3
#c = n1 ** (1/2)
#print ("O dobro de {} é {}, \n  o triplo é {} e a raiz quadrada é {}".format(n1, a, b, c))

# =========== exercicio 7 ===========
#n1 = float(input("Qual foi a primeira nota ? "))
#n2 = float(input("Qual foi a segunda nota ? "))
#m = (n1 + n2) / 2
#print ("A média entre {} e {} é igual a {}".format(n1, n2, m))

# =========== exercicio 8 ===========

#n1 = float(input("Quantos metros você quer converter ? "))
#km = n1 / 1000
#hm = n1 / 100
#dam = n1 / 10
#dm = n1 * 10
#cm = n1 * 100
#mm = n1 * 1000
#print ("A medida de {}m corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm".format(n1, km, hm, dam, dm, cm, mm))

# =========== exercicio 9 ===========
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

# =========== ou ===========

#def tabuada():
    #tab = int(input("Digite um número para ver a tabuada: "))
    #for i in range(1, 11):
        #print ("{} x {} = {}".format(tab, i, tab*i))
#tabuada()
#exercicio 10

#n1 = float(input("Quanto você tem na carteira  ? \n R$ "))
#dolar = n1 / 5.38 
#print ("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(n1, dolar))

# =========== exercicio 11 ===========

#n1 = float(input("Qual a Largura da sua paraede ? \n "))
#n2 = float(input("Qual a altura da sua parede ? \n "))
#area = n1 * n2 
#tinta = area / 2 
#print ("Sua parede tem a dimenssão de {:.2f}x{:.2f} e sua área é de {:.2f}m²".format(n1, n2, area))
#print ("Para pintar essa parede, você precisará de {:.2f}l de tinta".format(tinta))

# =========== exercicio 12 ===========

#n1 = float(input("Qual o preço do produto ? \n R$ "))
#desconto = n1 * 0.05
#preco = n1 - desconto 
#print ("O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}".format(n1, preco))

# =========== exercicio 13 ===========

#n1 = float(input("Qual o salário do funcionário ? \n R$ "))
#aumento = n1 * 0.15
#salario = n1 + aumento
#print ("Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}".format(n1, salario))

# =========== exercicio 14 ===========

#n1 = float(input("Quantos graus está fazendo ? \n "))
#f = ((9 * n1) / 5 ) + 32 
#print ("A temperatura de {:.2f}ºC corresponde a {:.2f}ºF".format(n1, f))

# =========== exercicio 15 ===========

#n1 = float(input("Quantos dias você alugou o carro ? \n "))
#n2 = float(input("Quantos km você rodou ? \n "))
#dias = n1 * 60
#km = n2 * 0.15
#total = dias + km
#print ("O total a pagar é de R$ {:.2f}".format(total))


