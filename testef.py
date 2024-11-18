def main():
    main_menu = True

    lugares1 = {"Filme1S1": 50, "Filme1S2": 50}
    lugares2 = {"Filme2S1": 40, "Filme2S2": 40}
    lugares3 = {"Filme3S1": 30, "Filme3S2": 30}

    ing_p_tp = {"Inteira": 0, "Meia": 0, "VIP": 0}

    lugares = [lugares1, lugares2, lugares3]

    print("==========BEM-VINDO(A) AO CINEMACK!!!==========")
    while main_menu:
        print("| 1. Comprar ingressos para Filme 1 - Sessão 1")
        print("| 2. Comprar ingressos para Filme 1 - Sessão 2")
        print("| 3. Comprar ingressos para Filme 2 - Sessão 1")
        print("| 4. Comprar ingressos para Filme 2 - Sessão 2")
        print("| 5. Comprar ingressos para Filme 3 - Sessão 1")
        print("| 6. Comprar ingressos para Filme 3 - Sessão 2")
        print("| 7. Avaliar um filme")
        print("| 8. Encerrar o dia, exibir o relatório e gerar arquivo.txt ")
        opcao_main = int(input(">>>"))

        if opcao_main == 1:
            compra_ing(lugares, ing_p_tp)

        elif opcao_main == 2:
            pass

        elif opcao_main == 8:
            break


def compra_ing(lugares, ing_p_tp):
    menu = True

    for a in lugares:
        if a["Filme1S1"] > 0:

            while menu:
                for l in lugares:
                    print(f'\nAssentos disponíveis para Filme 1 - Sessão 1: {l["Filme1S1"]}')
                    print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                    op_filmeX_sX = int(input(">>>"))

                    if op_filmeX_sX == 4:
                        print("Retornando ao menu principal...")
                        break

                    else:
                        if a["Filme1S1"] != 0:
                            if op_filmeX_sX == 1:
                                pass

                        else:
                            print("\nSessão esgotada! Tente outra opção.\n")
                            break