while True:
    batata = input("Deseja saber o rank do seu herói? S/N\n").upper()
    if batata == "S":
        nome = input("Digite o nome do herói!\n")
        while True:  
            try:
                exp = int(input("Digite a quantidade de XP do herói e saiba seu rank: \n"))

                if exp < 1000:
                    exp = "Ferro"
                elif 1001 <= exp < 2000:
                    exp = "Bronze"
                elif 2001 <= exp < 5000:
                    exp = "Prata"
                elif 5001 <= exp < 7000:
                    exp = "Ouro"
                elif 7001 <= exp < 8000:
                    exp = "Platina"
                elif 8001 <= exp < 9000:
                    exp = "Ascendente"
                elif 9001 <= exp < 10000:
                    exp = "Imortal"
                elif exp >= 10001:
                    exp = "Radiante"

                print(f"O Herói de nome **{nome}** está no nível de **{exp}**")
                break  # Sai do loop interno quando um valor válido de XP é fornecido
            except ValueError:
                print("Digite o XP em números inteiros")

    elif batata == "N":
        print("Até a próxima!")
        break
    else:
        print("'S' para sim e 'N' para não.")
