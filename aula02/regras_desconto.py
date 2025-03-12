def calcular_INSS(sal_bruto):
    return sal_bruto * 0.11 

def calcular_VA(sal_bruto):
    return sal_bruto * 0.06

def calcular_VT(sal_bruto):
    return sal_bruto * 0.05

def calcular_CRECHE(sal_bruto, filhos):
    if filhos == "S":
     return sal_bruto * 0.15
    
    return 0.0

def calcular_salario_liquido(sal_bruto, val_INSS, val_VA, val_VT, val_CRECHE):
    return sal_bruto - calcular_descontos(val_INSS,val_VA, val_VT, val_CRECHE)                                #(val_INSS + val_VA + val_VT + val_CRECHE)

def calcular_descontos (val_INSS, val_VA, val_VT, val_CRECHE):
    return val_INSS + val_VA + val_VT + val_CRECHE
