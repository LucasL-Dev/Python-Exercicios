valor = int(input("Qual o valor da compra?"))
Programa = str(input("Você está cadastrado no programa fidelidade?"))
Programa = Programa.lower()
Programa = Programa.strip() 

if valor >= 100 and Programa == "sim":
    print ("Está disponível pra frete grátis")
else:
    print ("Não pode frete grátis")
