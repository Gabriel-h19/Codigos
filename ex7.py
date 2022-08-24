carro = float(input("qual a sua velocidade? "))
multa = (carro-80)*7
if carro > 80:
    print("excesso de velocidade, multa de R${:.2f}".format(multa))
else:
    print("velocidade dentro do limite")