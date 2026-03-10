valor = float(input("Digite o valor da compra: R$ "))
if valor >= 100:
    valor_com_desconto = valor * 0.9
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
else:
    print(f"Valor da compra: R$ {valor:.2f} (sem desconto)")