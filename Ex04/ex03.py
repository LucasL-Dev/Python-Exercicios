user = "admin"
password = 1234
tentativa = 0

while (tentativa < 3 ): 
    
    Usuario = str(input("digite o Usuário"))
    Usuario = Usuario.lower()
    Usuario = Usuario.strip()
    Senha = int(input("Digite a senha"))

    if(Usuario == user and Senha == password):
        print("Aprovado")
    else: 
        tentativa = tentativa + 1 
        print("Tente novamente")
else: 
    print ("Número de tentativas excedidas")
    exit()
