#Sistema de Notas - Recuperação

nota01 = int(input("Digite sua primeira nota:"))
nota02 = int(input("Digite sua segunda nota:"))
nota03 = int(input("Digite sua terceira Nota:"))

Media = (nota01 + nota02 + nota03) / 3 

if (Media >= 7 ):
    print ("Aprovado(a)")
elif (Media >= 5 and Media < 7):
    print ("Recuperação paizão")
    recupera = int(input("Qual foi a nota da recuperação:"))
    if (recupera >= 6):
        print ("Aprovado")
    else:
        print ("Reprovado rapaz")
elif (Media < 5): 
    print ("Reprovado")
else:
    print ("Nota Inválida")