aux = input().split()
j = int(aux[0])
r = int(aux[1])

pontuacao = []
for i in range(j):
    pontuacao.append(0)

pontos = input().split()

for i in range(len(pontos)):
    pontos[i] = int(pontos[i])

jogador = 0
for i in range(len(pontos)):
    pontuacao[jogador] += pontos[i]
    if jogador != j-1:
        jogador += 1
    else:
        jogador = 0

maior = 0
index = 0
for i in range(len(pontuacao)):
    if pontuacao[i] >= maior:
        maior = pontuacao[i]
        index = i

print(index+1)