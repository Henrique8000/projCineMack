#Nome: Henrique Flávio Guimarães
#RA: 10427920

#Projeto: Sistema de Gestão do CineMack

#Este projeto simula um sistema de gerenciamento para o CineMack que exibe múltiplas sessões para vários filmes,
#com controle de vendas de diferentes tipos de ingressos (inteira, meia, VIP) e coleta de avaliações dos
#espectadores. O sistema deve gerenciar a venda de ingressos para várias sessões do mesmo filme, controlar a
#disponibilidade de assentos em cada sessão e calcular a receita separadamente para cada tipo de ingresso.

menu_main = True
menuF1S1 = True

Qtd_total_ing = 0
Val_total_ing = 0.00

# variaveis opçao 1
Qtd_LugarF1S1 = 50

Qtd_ingVipF1S1 = 0
Qtd_ingIntF1S1 = 0
Qtd_ingMeiaF1S1 = 0

Val_ingVipF1S1 = 0.00
Val_ingIntF1S1 = 0.00
Val_ingMeiaF1S1 = 0.00

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
                    print("Retornando ao menu principal...")
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
                            else:
                                print(
                                "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis"
                                )
                        else:
                            print("Insira uma opção válida!!!")

                    else:
                        print("\nSessão esgotada! Tente outra opção.\n")
                        break

    elif opcao_main == 2:
        menu_main = False
    elif opcao_main == 8:
        print("*******  Relatório Final *******\n")

        print("<<<<<< Filme 1 - Sessão 1: >>>>>>\n")
        print("Quantidade de ingressos vendidos:")
        print(f"- Inteira:{Qtd_ingIntF1S1}")
        print(f"- VIP:{Qtd_ingVipF1S1}")
        print(f"- Meia:{Qtd_ingMeiaF1S1}\n")
        print("Receita por tipo (Sessão 1):")
        print(f"- Inteira:{Val_ingIntF1S1:.2f}")
        print(f"- VIP:{Val_ingVipF1S1:.2f}")
        print(f"- Meia:{Val_ingMeiaF1S1:.2f}\n")

        print(f"Total de ingressos vendidos: {Qtd_total_ing}")

        print(f"Receita total do dia: R${Val_total_ing:.2f}")
        break

