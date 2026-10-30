# Programa para calcular a média de um aluno

# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as notas das quatro matérias
matematica = float(input("Digite a nota de Matemática: "))
portugues = float(input("Digite a nota de Português: "))
geografia = float(input("Digite a nota de Geografia: "))
ciencias = float(input("Digite a nota de Ciências: "))

# Calcula a média
media = (matematica + portugues + geografia + ciencias) / 4

# Exibe o resultado
print(f"\nAluno: {nome}")
print(f"Média final: {media:.2f}")

# Verifica se foi aprovado ou reprovado
if media >= 60:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")
