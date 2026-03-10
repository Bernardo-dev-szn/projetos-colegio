nota = float(input("Digite a nota do aluno: "))

nota_minima = 6.0

if nota >= nota_minima:
    print(f"Nota: {nota} - Aprovado")
else:
    print(f"Nota: {nota} - Reprovado")