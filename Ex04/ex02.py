Idade = int(input("Digite sua idade:"))

if (Idade >=0 and Idade <=11):
    print ("Você é criança")
elif (Idade >=12 and Idade <=17):
    print ("Você é Adolescente")
elif (Idade >=18 and Idade <=59):
    print ("Você é Adulto")
    print ("Você já pode votar!")
elif (Idade >=60):
    print ("Você é Idoso")
    print ("Você já pode dirigir!")
else: 
    print ("Idade Inválida!")