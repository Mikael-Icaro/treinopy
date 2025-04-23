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