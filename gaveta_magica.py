def verificar(valor, soma_moedas):
    if valor == 1:
        soma_moedas += 1
    if valor < 0:
        soma_moedas += valor
    return soma_moedas


def gaveta(fluxo):
    soma_moedas = 0
    for i in fluxo:
        soma_moedas += i
        soma_moedas = verificar(i, soma_moedas)

    return soma_moedas

fluxo = [1, -1, 2, 0, 4]
print(gaveta(fluxo))
