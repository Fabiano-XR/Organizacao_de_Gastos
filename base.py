salario = total = 0
gastos = []
exe = 1
i = 1
def alt_salario():
    cache = float(input("Digite o salario (ou 0 para voltar): "))
    if cache != 0:
        salario = cache
        return salario

def add_gasto():
    cache = []
    while True:
        temp = float(input("Digite o novo gasto (ou 0 para encerrar): "))
        if temp == 0:
            break
        cache.append(temp)
    return cache


while True:
    exe = int(input("\n 0 - Encerrar. \n 1 - Alterar o salario. \n 2 - Adicionar gasto. \n 3 - Mostrar atual salario. \n 4 - Mostrar atuais gastos. \n Digite oque deseja fazer? "))
    print("\n")

    if (exe == 0):
        break
    elif (exe == 1):
        salario = alt_salario()
    elif (exe == 2):
        gastos.extend(add_gasto())
        for gasto in gastos:
            total += gasto
    elif (exe == 3):
        print(f"O atual salario é {salario:.2f}")
    elif (exe == 4):
        print("Os atuais gastos são:")
        for gasto in gastos:
            print(f"{i} - {gasto}")
            i+=1
        print(f"Gasto Total = R${total}")
        i = 1
    else:
        print("Opção Inexistente.")