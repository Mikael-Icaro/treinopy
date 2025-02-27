
from regras_desconto import *

salario_bruto = float(input("Digite o salário bruto: "))

INSS = calcular_INSS(salario_bruto)               #salario_bruto * 0.11
VA = calcular_VA(salario_bruto)                   #salario_bruto * 0.06
VT = calcular_VT(salario_bruto)                   #salario_bruto * 0.05
#CRECHE = 0.0 

tem_filho = ''

tem_filho = input("Tem filho ? (S) Sim | (N) não: ")
while tem_filho != "S" and tem_filho != "N":
    tem_filho = input("Opção inválida. Digite (S) Sim | (N) não: ").upper()

#if tem_filho == "S":
CRECHE = calcular_CRECHE(salario_bruto, tem_filho)                                     #salario_bruto * 0.15 

salario_liquido = calcular_salario_liquido(salario_bruto, INSS, VA, VT, CRECHE)                  #salario_bruto - (INSS + VA +VT + CRECHE)

print (f"Seu salario é R$ {salario_liquido}") 

print (f"Total do seu desconto é R$ {calcular_descontos(INSS, VA, VT, CRECHE)}")

#f é uma cotenação de string, que permite a inserção de variáveis dentro de uma string

