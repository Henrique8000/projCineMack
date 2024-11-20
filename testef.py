def main():
    main_menu = True

    lugares1 = {"Filme1S1": 50, "Filme1S2": 50}
    lugares2 = {"Filme2S1": 40, "Filme2S2": 40}
    lugares3 = {"Filme3S1": 30, "Filme3S2": 30}

    filme1_ing = {'preco_int': 20, 'preco_meia': 10, 'preco_vip': 30}
    filme2_ing = {'preco_int': 15, 'preco_meia': 7.5, 'preco_vip': 22.5}
    filme3_ing = {'preco_int': 10, 'preco_meia': 5, 'preco_vip': 15}

    ing_p_tp = {"Inteira": 0, "Meia": 0, "VIP": 0}
    list_filme_ing = [filme1_ing, filme2_ing, filme3_ing]

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
            compra_ing(lugares1, ing_p_tp)

        elif opcao_main == 2:
            compra_ing(lugares1, ing_p_tp)

        elif opcao_main == 3:
            compra_ing(lugares2, ing_p_tp)

        elif opcao_main == 4:
            compra_ing(lugares2, ing_p_tp)

        elif opcao_main == 5:
            compra_ing(lugares3, ing_p_tp)

        elif opcao_main == 6:
            compra_ing(lugares3, ing_p_tp)

        elif opcao_main == 7:
            pass

        elif opcao_main == 8:
            break


def compra_ing(lugares, ing_p_tp):
    menu = 10

    while menu == 10:
        for x in lugares:
            print(f'\nAssentos disponíveis para Filme 1 - Sessão 1: {lugares.get(x)}')
            print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
            op_filmex_sx = int(input(">>>"))

            if op_filmex_sx == 4:
                print("Retornando ao menu principal...")
                menu = 3
                break

            elif op_filmex_sx == 3 or op_filmex_sx == 2 or op_filmex_sx == 1:
                if lugares.get(x) != 0:
                    if op_filmex_sx == 1:  #ingresso Inteiro
                        inteira = int(input("Quantos ingressos inteiros deseja comprar? "))
                        if inteira <= lugares.get(x):
                            ing_p_tp["Inteira"] += inteira
                            lugares[x] -= inteira

                            print("Compra bem sucedida!!! Aproveite o filme\n")
                            menu = 3
                            break

                        else:
                            print(
                                "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis")
                            menu = 3
                            break

                    elif op_filmex_sx == 2:  #ingresso meia
                        meia = int(input("Quantas meias você deseja comprar? "))
                        if meia <= lugares[x]:
                            ing_p_tp["Meia"] += meia
                            lugares[x] -= meia

                            print("Compra bem sucedida!!! Aproveite o filme\n")
                            menu = 3
                            break

                        else:
                            print(
                                "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis")
                            menu = 3
                            break

                    elif op_filmex_sx == 3:  # ingresso vip
                        vip = int(input("Quantos ingressos VIP você deseja comprar?"))
                        if vip <= lugares[x]:
                            ing_p_tp["VIP"] += vip
                            lugares[x] -= vip

                            print("Compra bem sucedida!!! Aproveite o filme\n")
                            menu = 3
                            break

                        else:
                            print(
                            "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis")
                            menu = 3
                            break

                else:
                    print("\nSessão esgotada! Tente outra opção.\n")
                    menu = 3
                    break

            else:
                print(
                    "\nInsira uma opção válida de 1 a 4!\n")
                menu = 3
                break


main()
