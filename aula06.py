def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    valor_total = valor_conta + gorjeta
    return gorjeta, valor_total

valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta, valor_total = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"Valor da gorjeta: R${gorjeta:.2f}")
print(f"Valor total a ser pago: R${valor_total:.2f}")