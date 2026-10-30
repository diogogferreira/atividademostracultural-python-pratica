# EXPLICAÇÃO CÓDIGO ATIVIDADE

Esse código é um programa simples de entrada de dados, cálculo e decisão. Ele começa pedindo o nome do aluno com input(), que guarda o texto digitado em uma variável do tipo string.
Em seguida, pede as quatro notas. Cada float(input()) converte o que a pessoa digita em número decimal. Isso é essencial porque notas podem ter casas decimais e a média precisa ser precisa. Se usássemos só input(), o Python trataria tudo como texto e a conta não funcionaria.
A média é calculada somando as quatro notas e dividindo por 4. O resultado fica guardado na variável media. Essa é a forma mais direta e correta de obter a média aritmética.
Depois o programa mostra o nome e a média formatada com duas casas decimais usando uma f-string (f"..."). O :.2f força a exibição limpa, evitando números longos demais.
Por fim, o if verifica se a média é maior ou igual a 60. Se for, imprime “APROVADO”. Caso contrário, cai no else e imprime “REPROVADO”. É uma decisão binária simples: ou passou, ou não.
O código inteiro roda de cima para baixo, uma única vez. Não tem laços nem funções extras porque a tarefa é direta: coletar, calcular e informar.
