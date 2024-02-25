#Dar boas-vindas 
print("Bem-vindo ao calculador de gorjetas!")
conta = float(input("Qual o valor total da conta?"))
gorjeta = int(input("Quanto você gostaria de dar de gorjeta, 10, 12 ou 15 por cento?"))
pessoas = int(input("Quantas pessoas vão dividir?"))

gorjeta_percentual = gorjeta / 100
ValorGorjeta = conta * gorjeta_percentual
totalConta = conta + ValorGorjeta
conta_por_pessoa = round((totalConta / pessoas),2)

print(f"Cada pessoa pagará: R${conta_por_pessoa}, sendo que o valor total da gorjeta foi de: R${ValorGorjeta}")
