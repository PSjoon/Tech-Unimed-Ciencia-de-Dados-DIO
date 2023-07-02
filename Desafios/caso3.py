salario = float(input())


if (salario >= 0 and salario <= 600.00):
    porcentagem = 17 / 100
    final = porcentagem * salario
    total = salario + final
    percentual = porcentagem * 100

elif (salario >= 600.01 and salario <= 900.00):
    porcentagem = 13 / 100
    final = porcentagem * salario
    total = salario + final
    percentual = porcentagem * 100

elif (salario >= 900.01 and salario <= 1500.00):
    porcentagem = 12 / 100
    final = porcentagem * salario
    total = salario + final
    percentual = porcentagem * 100

elif (salario >= 1500.01 and salario <= 2000.00):
    porcentagem = 10 / 100
    final = porcentagem * salario
    total = salario + final
    percentual = porcentagem * 100

else:
    porcentagem = 5 / 100
    final = porcentagem * salario
    total = salario + final
    percentual = porcentagem * 100

final = "%.2f" % final
total = "%.2f" % total
percentual = "%.0f" % percentual


print("Novo salario: ", str(total).replace('.', ','), "Reajuste ganho: ", str(
    final).replace('.', ','), "Em percentual: ", percentual, "%")


# print("Reajuste ganho: ", str(final).replace('.', ','))
# print("Em percentual: ", percentual, "%")
