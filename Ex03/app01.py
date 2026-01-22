print ("Esse é o nosso Menu:")
print ("1.Pizza")
print ("2.Sushi")
print ("3.Salada")

escolha = int(input("Qual a sua escolha?"))

match escolha:
    case 1:
        print ("A sua escolha foi Pizza, o valor é R$35")
    case 2:
        print ("A sua escolha foi Sushi, o valor é R45")
    case 3:
        print ("A sua escolha foi Pizza, o valor é R$10")