valor =[]
soma = 0
for i in range(4):
    valor.append(int(input("entre com a nota: ")))
    soma += valor[i]
media = soma/4

print(media)


