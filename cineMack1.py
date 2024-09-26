#Nome: Henrique Flávio Guimarães
#RA: 10427920

#Projeto: Sistema de Gestão do CineMack

#Este projeto simula um sistema de gerenciamento para o CineMack que exibe múltiplas sessões para vários filmes,
#com controle de vendas de diferentes tipos de ingressos (inteira, meia, VIP) e coleta de avaliações dos
#espectadores. O sistema deve gerenciar a venda de ingressos para várias sessões do mesmo filme, controlar a
#disponibilidade de assentos em cada sessão e calcular a receita separadamente para cada tipo de ingresso.

menu_main = True
menuF1S1 = True
menuF1S2 = True
menuF2S1 = True
menuF2S2 = True
menuF3S1 = True
menuF3S2 = True
menu_avaliacao = True

# variáveis para o total de ingresos vendidos e do lucro total
Qtd_total_ing = 0
Val_total_ing = 0.00

# variaveis de lugar por filme e sessão
Qtd_LugarF1S1 = 50
Qtd_LugarF1S2 = 50

Qtd_LugarF2S1 = 40
Qtd_LugarF2S2 = 40

Qtd_LugarF3S1 = 30
Qtd_LugarF3S2 = 30

# variaveis opçao 1 (Filme 1 Sessão 1)
Qtd_ingVipF1S1 = 0
Qtd_ingIntF1S1 = 0
Qtd_ingMeiaF1S1 = 0

Val_ingVipF1S1 = 0.00
Val_ingIntF1S1 = 0.00
Val_ingMeiaF1S1 = 0.00

# variaveis opcao 2 (Filme 1 Sessão 2)
Qtd_ingVipF1S2 = 0
Qtd_ingIntF1S2 = 0
Qtd_ingMeiaF1S2 = 0

Val_ingVipF1S2 = 0.00
Val_ingIntF1S2 = 0.00
Val_ingMeiaF1S2 = 0.00

# variaveis opcao 3 (Filme 2 - Sessão 1)
Qtd_ingVipF2S1 = 0
Qtd_ingIntF2S1 = 0
Qtd_ingMeiaF2S1 = 0

Val_ingVipF2S1 = 0.00
Val_ingIntF2S1 = 0.00
Val_ingMeiaF2S1 = 0.00

# variaveis opcao 4 (Filme 2 - Sessão 2)
Qtd_ingVipF2S2 = 0
Qtd_ingIntF2S2 = 0
Qtd_ingMeiaF2S2 = 0

Val_ingVipF2S2 = 0.00
Val_ingIntF2S2 = 0.00
Val_ingMeiaF2S2 = 0.00

# variaveis opcao 5 (Filme 3 - Sessão 1)
Qtd_ingVipF3S1 = 0
Qtd_ingIntF3S1 = 0
Qtd_ingMeiaF3S1 = 0

Val_ingVipF3S1 = 0.00
Val_ingIntF3S1 = 0.00
Val_ingMeiaF3S1 = 0.00

# variaveis opcao 6 (Filme 3 - Sessão 2)
Qtd_ingVipF3S2 = 0
Qtd_ingIntF3S2 = 0
Qtd_ingMeiaF3S2 = 0

Val_ingVipF3S2 = 0.00
Val_ingIntF3S2 = 0.00
Val_ingMeiaF3S2 = 0.00

# variaveis opcao 7 (Avaliaçao)
cont_Ava_Filme1 = 0
cont_Ava_Filme2 = 0
cont_Ava_Filme3 = 0

divisorMediF1 = 0
divisorMediF2 = 0
divisorMediF3 = 0

while menu_main:
    print("1. Comprar ingressos para Filme 1 - Sessão 1")
    print("2. Comprar ingressos para Filme 1 - Sessão 2")
    print("3. Comprar ingressos para Filme 2 - Sessão 1")
    print("4. Comprar ingressos para Filme 2 - Sessão 2")
    print("5. Comprar ingressos para Filme 3 - Sessão 1")
    print("6. Comprar ingressos para Filme 3 - Sessão 2")
    print("7. Avaliar um filme")
    print("8. Encerrar o dia e exibir o relatório ")
    opcao_main = int(input(">>>"))

    if opcao_main == 1:

        if Qtd_LugarF1S1 > 0:

            while menuF1S1:
                print(f'\nAssentos disponíveis para Filme 1 - Sessão 1: {Qtd_LugarF1S1}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF1S1 = int(input('>>>'))

                if opcaoF1S1 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break
                else:
                    if Qtd_LugarF1S1 != 0:
                        if opcaoF1S1 == 1: #ingressos Inteiros
                            inteiraF1S1 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF1S1 <= Qtd_LugarF1S1:
                                Qtd_LugarF1S1 -= inteiraF1S1
                                Qtd_ingIntF1S1 += inteiraF1S1
                                Val_ingIntF1S1 += inteiraF1S1 * 20.00
                                Qtd_total_ing += Qtd_ingIntF1S1
                                Val_total_ing += Val_ingIntF1S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis")

                        elif opcaoF1S1 == 2: #ingresso meia
                            meiaF1S1 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF1S1 <= Qtd_LugarF1S1:
                                Qtd_LugarF1S1 -= meiaF1S1
                                Qtd_ingMeiaF1S1 += meiaF1S1
                                Val_ingMeiaF1S1 += meiaF1S1 * 10.00
                                Qtd_total_ing += Qtd_ingMeiaF1S1
                                Val_total_ing += Val_ingMeiaF1S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        elif opcaoF1S1 == 3:
                            vipF1S1 = int(input("Quantos ingressos VIP você deseja comprar?"))
                            if vipF1S1 <= Qtd_LugarF1S1:
                                Qtd_LugarF1S1 -= vipF1S1
                                Qtd_ingVipF1S1 += vipF1S1
                                Val_ingVipF1S1 += vipF1S1 * 30.00
                                Qtd_total_ing += Qtd_ingVipF1S1
                                Val_total_ing += Val_ingVipF1S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        else:
                            print("\nInsira uma opção válida!!! (1 a 4)\n")

                    else:
                        print("\nSessão esgotada! Tente outra opção.\n")
                        break

    elif opcao_main == 2:

        if Qtd_LugarF1S2 > 0:

            while menuF1S2:
                print(f'\nAssentos disponíveis para Filme 1 - Sessão 2: {Qtd_LugarF1S2}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF1S2 = int(input(">>>"))

                if opcaoF1S2 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break
                else:
                    if Qtd_LugarF1S2 != 0:
                        if opcaoF1S2 == 1:
                            inteiraF1S2 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF1S2 <= Qtd_LugarF1S2:
                                Qtd_LugarF1S2 -= inteiraF1S2
                                Qtd_ingIntF1S2 += inteiraF1S2
                                Val_ingIntF1S2 += inteiraF1S2 * 20.00
                                Qtd_total_ing += inteiraF1S2
                                Val_total_ing += Val_ingIntF1S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        elif opcaoF1S2 == 2:
                            meiaF1S2 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF1S2 <= Qtd_LugarF1S2:
                                Qtd_LugarF1S2 -= meiaF1S2
                                Qtd_ingMeiaF1S2 += meiaF1S2
                                Val_ingMeiaF1S2 += meiaF1S2 * 10.00
                                Qtd_total_ing += meiaF1S2
                                Val_total_ing += Val_ingMeiaF1S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        elif opcaoF1S2 == 3:
                            vipF1S2 = int(input("Quantos ingressos VIP você deseja comprar? "))
                            if vipF1S2 <= Qtd_LugarF1S2:
                                Qtd_LugarF1S2 -= vipF1S2
                                Qtd_ingVipF1S2 += vipF1S2
                                Val_ingVipF1S2 += vipF1S2 * 30.00
                                Qtd_total_ing += vipF1S2
                                Val_total_ing += Val_ingVipF1S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        else:
                            print("Insira uma opção válida!!! (1 a 4)")

                    else:
                        print("\nSessão esgotada! Tente outra opção.\n")
                        break

    elif opcao_main == 3:

        if Qtd_LugarF2S1 > 0:

            while menuF2S1:
                print(f'\nAssentos disponíveis para Filme 2 - Sessão 1: {Qtd_LugarF2S1}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF2S1 = int(input('>>>'))

                if opcaoF2S1 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break
                else:
                    if Qtd_LugarF2S1 != 0:

                        if opcaoF2S1 == 1:
                            inteiraF2S1 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF2S1 <= Qtd_LugarF2S1:
                                Qtd_LugarF2S1 -= inteiraF2S1
                                Qtd_ingIntF2S1 += inteiraF2S1
                                Val_ingIntF2S1 += inteiraF2S1 * 15.00
                                Qtd_total_ing += inteiraF2S1
                                Val_total_ing += Val_ingIntF2S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        elif opcaoF2S1 == 2:
                            meiaF2S1 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF2S1 <= Qtd_LugarF2S1:
                                Qtd_LugarF2S1 -= meiaF2S1
                                Qtd_ingMeiaF2S1 += meiaF2S1
                                Val_ingMeiaF2S1 += meiaF2S1 * 7.5
                                Qtd_total_ing +=  meiaF2S1
                                Val_total_ing += Val_ingMeiaF2S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF2S1 == 3:
                            vipF2S1 = int(input("Quantos ingressos VIP você deseja comprar? "))
                            if vipF2S1 <= Qtd_LugarF2S1:
                                Qtd_LugarF2S1 -= vipF2S1
                                Qtd_ingVipF2S1 += vipF2S1
                                Val_ingVipF2S1 += vipF2S1 * 22.5
                                Qtd_total_ing += vipF2S1
                                Val_total_ing += Val_ingVipF2S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        else:
                            print("\nInsira uma opção válida!!! (1 a 4)\n")

                    else:
                        print("\nSessão esgotada! Tente outra opção.\n")
                        break

    elif opcao_main == 4:
        if Qtd_LugarF2S2 > 0:

            while menuF2S2:
                print(f'\nAssentos disponíveis para Filme 2 - Sessão 2: {Qtd_LugarF2S2}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF2S2 = int(input(">>>"))
                if opcaoF2S2 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break

                else:
                    if Qtd_LugarF2S2 != 0:

                        if opcaoF2S2 == 1:
                            inteiraF2S2 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF2S2 <= Qtd_LugarF2S2:
                                Qtd_LugarF2S2 -= inteiraF2S2
                                Qtd_ingIntF2S2 += inteiraF2S2
                                Val_ingIntF2S2 += inteiraF2S2 * 15.00
                                Qtd_total_ing += inteiraF2S2
                                Val_total_ing += Val_ingIntF2S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF2S2 == 2:
                            meiaF2S2 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF2S2 <= Qtd_LugarF2S2:
                                Qtd_LugarF2S2 -= meiaF2S2
                                Qtd_ingMeiaF2S2 += meiaF2S2
                                Val_ingMeiaF2S2 += meiaF2S2 * 7.5
                                Qtd_total_ing += meiaF2S2
                                Val_total_ing += Val_ingMeiaF2S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF2S2 == 3:
                            vipF2S2 = int(input("Quantos ingressos VIP você deseja comprar? "))
                            if vipF2S2 <= Qtd_LugarF2S2:
                                Qtd_LugarF2S2 -= vipF2S2
                                Qtd_ingVipF2S2 += vipF2S2
                                Val_ingVipF2S2 += vipF2S2 * 22.5
                                Qtd_total_ing += vipF2S2
                                Val_total_ing += Val_ingVipF2S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        else:
                            print("Insira uma opção válida!!! (1 a 4)")

        else:
            print("\nSessão esgotada! Tente outra opção.\n")

    elif opcao_main == 5:
        if Qtd_LugarF3S1 > 0:

            while menuF3S1:
                print(f'\nAssentos disponíveis para Filme 3 - Sessão 1: {Qtd_LugarF3S1}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF3S1 = int(input(">>>"))
                if opcaoF3S1 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break

                else:
                    if Qtd_LugarF3S1 != 0:
                        if opcaoF3S1 == 1:
                            inteiraF3S1 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF3S1 <= Qtd_LugarF3S1:
                                Qtd_LugarF3S1 -= inteiraF3S1
                                Qtd_ingIntF3S1 += inteiraF3S1
                                Val_ingIntF3S1 += inteiraF3S1 * 10.00
                                Qtd_total_ing += inteiraF3S1
                                Val_total_ing += Val_ingIntF3S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF3S1 == 2:
                            meiaF3S1 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF3S1 <= Qtd_LugarF3S1:
                                Qtd_LugarF3S1 -= meiaF3S1
                                Qtd_ingMeiaF3S1 += meiaF3S1
                                Val_ingMeiaF3S1 += meiaF3S1 * 5.00
                                Qtd_total_ing += meiaF3S1
                                Val_total_ing += Val_ingMeiaF3S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF3S1 == 3:
                            vipF3S1 = int(input("\nQuantos ingressos VIP você deseja comprar? "))
                            if vipF3S1 <= Qtd_LugarF3S1:
                                Qtd_LugarF3S1 -= vipF3S1
                                Qtd_ingVipF3S1 += vipF3S1
                                Val_ingVipF3S1 += vipF3S1 * 15.00
                                Qtd_total_ing += vipF3S1
                                Val_total_ing += Val_ingVipF3S1
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        else:
                            print("Insira uma opção válida!!! (1 a 4)")

        else:
            print("\nSessão esgotada! Tente outra opção.\n")

    elif opcao_main == 6:

        if Qtd_LugarF3S2 > 0:

            while menuF3S2:
                print(f'\nAssentos disponíveis para Filme 3 - Sessão 2: {Qtd_LugarF3S2}')
                print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
                opcaoF3S2 = int(input(">>>"))
                if opcaoF3S2 == 4:
                    print("\nRetornando ao menu principal...\n")
                    break

                else:
                    if Qtd_LugarF3S2 != 0:

                        if opcaoF3S2 == 1:
                            inteiraF3S2 = int(input("Quantos ingressos inteiros deseja comprar? "))
                            if inteiraF3S2 <= Qtd_LugarF3S2:
                                Qtd_LugarF3S2 -= inteiraF3S2
                                Qtd_ingIntF3S2 += inteiraF3S2
                                Val_ingIntF3S2 += inteiraF3S2 * 10.00
                                Qtd_total_ing += inteiraF3S2
                                Val_total_ing += Val_ingIntF3S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF3S2 == 2:
                            meiaF3S2 = int(input("Quantas meias você deseja comprar? "))
                            if meiaF3S2 <= Qtd_LugarF3S2:
                                Qtd_LugarF3S2 -= meiaF3S2
                                Qtd_ingMeiaF3S2 += meiaF3S2
                                Val_ingMeiaF3S2 += meiaF3S2 * 5.00
                                Qtd_total_ing += meiaF3S2
                                Val_total_ing += Val_ingMeiaF3S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break

                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        elif opcaoF3S2 == 3:
                            vipF3S2 = int(input("Quantos ingressos VIP você deseja comprar? "))
                            if vipF3S2 <= Qtd_LugarF3S2:
                                Qtd_LugarF3S2 -= vipF3S2
                                Qtd_ingVipF3S2 += vipF3S2
                                Val_ingVipF3S2 += vipF3S2 * 15.00
                                Qtd_total_ing += vipF3S2
                                Val_total_ing += Val_ingVipF3S2
                                print("Compra bem sucedida!!! Aproveite o filme\n")
                                break
                            else:
                                print(
                                    "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )

                        else:
                            print("\nInsira uma opção válida!!! (1 a 4)\n")

        else:
            print("\nSessão esgotada! Tente outra opção.\n")

    elif opcao_main == 7:

        while menu_avaliacao:
            print("\nEscolha um filme para avaliar: ")
            print("1. Avaliar Filme 1")
            print("2. Avaliar Filme 2")
            print("3. Avaliar Filme 3")
            print("4. Voltar")
            opcao_avaliacao = int(input(">>>"))
            if opcao_avaliacao > 4 or opcao_avaliacao < 1:
                print("\nInsira uma opção válida!!! (1 a 4)\n")

            elif opcao_avaliacao == 1:
                filme1Ava = int(input("Avalie o Filme 1 (1 a 5 estrelas): "))
                if filme1Ava < 1 or filme1Ava > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")
                else:
                    cont_Ava_Filme1 += filme1Ava
                    divisorMediF1 += 1

            elif opcao_avaliacao == 2:
                filme2Ava = int(input("Avalie o Filme 2 (1 a 5 estrelas): "))
                if filme2Ava < 1 or filme2Ava > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")
                else:
                    cont_Ava_Filme2 += filme2Ava
                    divisorMediF2 += 1

            elif opcao_avaliacao == 3:
                filme3Ava = int(input("Avalie o Filme 2 (1 a 5 estrelas): "))
                if filme3Ava < 1 or filme3Ava > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")
                else:
                    cont_Ava_Filme3 += filme3Ava
                    divisorMediF3 += 1

            elif opcao_avaliacao == 4:
                break

    elif opcao_main == 8:
        print("\n*******  Relatório Final *******\n")

        print("<<<<<< Filme 1 - Sessão 1: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF1S1}")
        print(f"- VIP:{Qtd_ingVipF1S1}")
        print(f"- Meia:{Qtd_ingMeiaF1S1}\n")

        print("Receita por tipo (Filme 1 - Sessão 1):")
        print(f"- Inteira: R${Val_ingIntF1S1:.2f}")
        print(f"- VIP: R${Val_ingVipF1S1:.2f}")
        print(f"- Meia: R${Val_ingMeiaF1S1:.2f}\n")

        print("<<<<<< Filme 1 - Sessão 2: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF1S2}")
        print(f"- VIP:{Qtd_ingVipF1S2}")
        print(f"- Meia:{Qtd_ingMeiaF1S2}\n")

        print("Receita por tipo (Filme 1 - Sessão 2):")
        print(f"- Inteira: R${Val_ingIntF1S2:.2f}")
        print(f"- VIP: R${Val_ingVipF1S2}")
        print(f"- Meia: R${Val_ingMeiaF1S2:.2f}\n")

        print("\n<<<<<< Filme 2 - Sessão 1: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF2S1}")
        print(f"- VIP:{Qtd_ingVipF2S1}")
        print(f"- Meia:{Qtd_ingMeiaF2S1}")

        print("\nReceita por tipo (Filme 2 - Sessão 1):")
        print(f"- Inteira: R${Val_ingIntF2S1:.2f}")
        print(f"- VIP: R${Val_ingVipF2S1:.2f}")
        print(f"- Meia: R${Val_ingMeiaF2S1:.2f}")

        print("\n<<<<<< Filme 2 - Sessão 2: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF2S2}")
        print(f"- VIP:{Qtd_ingVipF2S2}")
        print(f"- Meia:{Qtd_ingMeiaF2S2}")

        print("\nReceita por tipo (Filme 2 - Sessão 2):")
        print(f"- Inteira: R${Val_ingIntF2S2:.2f}")
        print(f"- VIP: R${Val_ingVipF2S2:.2f}")
        print(f"- Meia: R${Val_ingMeiaF2S2:.2f}")

        print("\n<<<<<< Filme 3 - Sessão 1: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF3S1}")
        print(f"- VIP:{Qtd_ingVipF3S1}")
        print(f"- Meia:{Qtd_ingMeiaF3S1}")

        print("\nReceita por tipo (Filme 3 - Sessão 1):")
        print(f"- Inteira: R${Val_ingIntF3S1:.2f}")
        print(f"- VIP: R${Val_ingVipF3S1:.2f}")
        print(f"- Meia: R${Val_ingMeiaF3S1:.2f}")

        print("\n<<<<<< Filme 3 - Sessão 2: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF3S2}")
        print(f"- VIP:{Qtd_ingVipF3S2}")
        print(f"- Meia:{Qtd_ingMeiaF3S2}")

        print("\nReceita por tipo (Filme 3 - Sessão 2):")
        print(f"- Inteira: R${Val_ingIntF3S2:.2f}")
        print(f"- VIP: R${Val_ingVipF3S2:.2f}")
        print(f"- Meia: R${Val_ingMeiaF3S2:.2f}")

        print("\nMédia de avaliações:")
        print(f"Filme 1: {cont_Ava_Filme1 / divisorMediF1}")
        print(f"Filme 2: {cont_Ava_Filme2 / divisorMediF2}")
        print(f"Filme 3: {cont_Ava_Filme3 / divisorMediF3}")

        print(f"\nTotal de ingressos vendidos: {Qtd_total_ing}")

        print(f"Receita total do dia: R${Val_total_ing:.2f}")

        print("Fim do programa!!!")
        break

    else:
        print("\nDigite uma opção válida!(1 - 8)\n")
