
Transporte = str(input("Digite o seu meio de transporte"))
Transporte = Transporte.lower()
Transporte = Transporte.strip()

match Transporte:
    case "carro":
        print ("Veículo terrestre")
    case "Bicicleta":
        print ("Transporte sustentável")
    case "Avião" | "helicópeto":
        print ("Transporte aéreo")
    case _:
        print ("Transporte desconhecido")