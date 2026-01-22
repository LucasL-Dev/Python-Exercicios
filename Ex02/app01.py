NotaFilme = int(input("Digite a nota do filme"))

if (NotaFilme >=9 and NotaFilme <=10):
    print("O filme é Excelente!")
elif (NotaFilme >=7 and NotaFilme <=8):
    print("O filme é Muito bom")
elif (NotaFilme >=5 and NotaFilme <=6):
    print("O filme é regular")
elif (NotaFilme < 5):
    print("Esse bglh é uma merda")
else:
    print ("Deu erro ai patrão, coloca de 0 a 10")