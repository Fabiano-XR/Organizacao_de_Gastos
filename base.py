salario = total = 0.0
gastos = []
exe = 1
def alt_salario():
    while True:
        try:
            cache = float(input("Digite o salario (ou 0 para voltar): "))
            break
        except:
            print("Entrada invalida")
    if cache != 0:
        salario = cache
        return salario
def add_gasto():
    cache = []
    while True:
        while True:
            try:
                temp = float(input("Digite o novo gasto (ou 0 para encerrar): "))
                break
            except:
                print("Entrada invalida")

        if temp == 0:
            break
        cache.append(temp)
    return cache
def list_gasto():
    i = 1
    for gasto in gastos:
        print(f"{i} - {gasto}")
        i+=1
    print(f"Gasto Total = R${total}")

while True:
    while True:
        try:
            exe = int(input("\n 0 - Encerrar. \n 1 - Alterar o salario. \n 2 - Adicionar gasto. \n 3 - Mostrar atual salario. \n 4 - Mostrar atuais gastos. \n 5 - Excluir um gasto. \n Digite oque deseja fazer? "))
            break
        except:
            print("Entrada invalida. \n")
        print("\n")

    if (exe == 0): #encerra programa
        break
    elif (exe == 1): #altera o salario
        salario = alt_salario()
    elif (exe == 2): #adiciona um gasto
        gastos.extend(add_gasto())
        for gasto in gastos:
            total += gasto
    elif (exe == 3): #mostra o salario
        print(f"O atual salario é {salario:.2f}")
    elif (exe == 4): #mostra os gastos
        print("Os atuais gastos são:")
        list_gasto()
    elif (exe == 5): #exclui um gasto
        list_gasto()
        delete = int(input("\n Qual gasto gostaria de exluir? "))
        total -= gastos.pop((delete-1))
        print("Gastos atuais:")
        list_gasto()
    else: #se digitar um numero errado
        print("Opção Inexistente.")