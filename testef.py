def main():
    main_menu = True

    filme1_ava = []
    filme2_ava = []
    filme3_ava = []

    lugares1 = [50, 50]
    lugares2 = [40, 40]
    lugares3 = [30, 30]

    qtd_filme1s1 = [0, 0, 0]  #Indices = 0 (Inteira); 1 (Meia); 2 (Vip)
    qtd_filme1s2 = [0, 0, 0]
    qtd_filme2s1 = [0, 0, 0]
    qtd_filme2s2 = [0, 0, 0]
    qtd_filme3s1 = [0, 0, 0]
    qtd_filme3s2 = [0, 0, 0]

    ing_p_tp = {"Total": 0}

    mediaf1 = 0
    mediaf2 = 0
    mediaf3 = 0

    msg_aviso("   ==================   BEM-VINDO(A) AO CINEMACK!!!   ================== ")
    while main_menu:

        print(f"| 1. Comprar ingressos para Filme 1 - Sessão 1 (Disponibilidade: {lugares1[0]} lugares)")
        print(f"| 2. Comprar ingressos para Filme 1 - Sessão 2 (Disponibilidade: {lugares1[1]} lugares)")
        print(f"| 3. Comprar ingressos para Filme 2 - Sessão 1 (Disponibilidade: {lugares2[0]} lugares)")
        print(f"| 4. Comprar ingressos para Filme 2 - Sessão 2 (Disponibilidade: {lugares2[1]} lugares)")
        print(f"| 5. Comprar ingressos para Filme 3 - Sessão 1 (Disponibilidade: {lugares3[0]} lugares)")
        print(f"| 6. Comprar ingressos para Filme 3 - Sessão 2 (Disponibilidade: {lugares3[1]} lugares)")
        print(f"| 7. Avaliar um filme")
        print(f"| 8. Encerrar o dia, exibir o relatório e gerar arquivo.txt ")
        opcao_main = int(input("\nEscolha uma opção >>> "))

        if opcao_main == 1:
            compra_ing(0, '1', '1', lugares1, qtd_filme1s1, ing_p_tp)

        elif opcao_main == 2:
            compra_ing(1, '1', '2', lugares1, qtd_filme1s2, ing_p_tp)

        elif opcao_main == 3:
            compra_ing(0, '2', '1', lugares2, ing_p_tp)

        elif opcao_main == 4:
            compra_ing(1, '2', '2', lugares2, ing_p_tp)

        elif opcao_main == 5:
            compra_ing(0, '3', '1', lugares3, ing_p_tp)

        elif opcao_main == 6:
            compra_ing(1, '3', '2', lugares3, ing_p_tp)

        elif opcao_main == 7:
            avaliar_filme(filme1_ava, filme2_ava, filme3_ava)
            pass

        elif opcao_main == 8:
            media_rf = relatorio_final(qtd_filme1s1, qtd_filme1s2, qtd_filme2s1, qtd_filme2s2, filme1_ava, mediaf1, filme2_ava, mediaf2, filme3_ava, mediaf3, ing_p_tp)
            relatorio_final_txt(media_rf, ing_p_tp)
            break


def compra_ing(n_indice, n_filme, n_sessao, lugares, qtd_filmexsx, ing_p_tp):
    if lugares[n_indice] != 0:
        menu = True
    else:
        msg_aviso("\nSessão esgotada! Tente outra opção.\n")
        menu = False

    while menu:
        print(f'\nAssentos disponíveis para Filme {n_filme} - Sessão {n_sessao}: {lugares[n_indice]}')
        print(f'Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Voltar):')
        op_filmex_sx = int(input(">>> "))

        if op_filmex_sx == 4:
            print("Retornando ao menu principal...")
            break

        elif op_filmex_sx == 3 or op_filmex_sx == 2 or op_filmex_sx == 1:
            if lugares[n_indice] != 0:
                if op_filmex_sx == 1:  #ingresso Inteiro
                    inteira = int(input("Quantos ingressos inteiros deseja comprar? "))
                    if inteira <= lugares[n_indice]:
                        qtd_filmexsx[0] += inteira
                        ing_p_tp["Total"] += inteira
                        lugares[n_indice] -= inteira

                        msg_aviso("Compra bem sucedida!!! Aproveite o filme\n")
                        break

                    else:
                        msg_aviso(
                            "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis\n")
                        break

                elif op_filmex_sx == 2:  #ingresso meia
                    meia = int(input("Quantas meias você deseja comprar? "))
                    if meia <= lugares[n_indice]:
                        qtd_filmexsx[1] += meia
                        ing_p_tp["Total"] += meia
                        lugares[n_indice] -= meia

                        msg_aviso("Compra bem sucedida!!! Aproveite o filme")
                        break

                    else:
                        msg_aviso(
                            "\nImpossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis\n")
                        break

                elif op_filmex_sx == 3:  # ingresso vip
                    vip = int(input("Quantos ingressos VIP você deseja comprar?"))
                    if vip <= lugares[n_indice]:
                        qtd_filmexsx[2] += vip
                        ing_p_tp["Total"] += vip
                        lugares[n_indice] -= vip

                        msg_aviso("Compra bem sucedida!!! Aproveite o filme\n")
                        break

                    else:
                        msg_aviso(
                            "Impossível realizar a compra! Tente comprar uma quantidade\nde ingresos proporcional ao total de lugares disponíveis\n")
                        break

            else:
                msg_aviso("\nSessão esgotada! Tente outra opção.\n")
                break

        else:
            msg_aviso("\nInsira uma opção válida de 1 a 4!\n")
            break


def msg_aviso(msg):
    print()
    print("~=~" * 25)
    print(msg)
    print("~=~" * 25)
    print()


def avaliar_filme(filme1_ava, filme2_ava, filme3_ava):
    menu_avaliacao = True

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
            filme1_ava.append(int(input("Avalie o Filme 1 (1 a 5 estrelas): ")))
            for a in filme1_ava:
                if a < 1 or a > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")

        elif opcao_avaliacao == 2:
            filme2_ava.append(int(input("Avalie o Filme 2 (1 a 5 estrelas): ")))
            for b in filme2_ava:
                if b < 1 or b > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")

        elif opcao_avaliacao == 3:
            filme3_ava.append(int(input("Avalie o Filme 3 (1 a 5 estrelas): ")))
            for c in filme3_ava:
                if c < 1 or c > 5:
                    print("\nAs notas devem estar dentro do intervalo de 1 a 5!\n")

        elif opcao_avaliacao == 4:
            break


def relatorio_final(qtd_filme1s1, qtd_filme1s2, qtd_filme2s1, qtd_filme2s2, filme1_ava, mediaf1, filme2_ava, mediaf2, filme3_ava, mediaf3, ing_p_tp):
    print("\n*******  Relatório Final *******\n")

    print("<<<<<< Filme 1 - Sessão 1: >>>>>>")
    print("Quantidade de ingressos vendidos:")
    print(f"- Inteiras:{qtd_filme1s1[0]}")
    print(f"- VIP:{qtd_filme1s1[2]}")
    print(f"- Meia:{qtd_filme1s1[1]}\n")

    print("Receita por tipo (Filme 1 - Sessão 1):")
    print(f"- Inteira: R${qtd_filme1s1[0] * 20:.2f}")
    print(f"- VIP: R${qtd_filme1s1[2] * 30:.2f}")
    print(f"- Meia: R${qtd_filme1s1[1] * 10:.2f}\n")

    print("<<<<<< Filme 1 - Sessão 2: >>>>>>")
    print("Quantidade de ingressos vendidos:")
    print(f"- Inteira:{qtd_filme1s2[0]}")
    print(f"- VIP:{qtd_filme1s2[2]}")
    print(f"- Meia:{qtd_filme1s2[1]}\n")

    print("Receita por tipo (Filme 1 - Sessão 2):")
    print(f"- Inteira: R${qtd_filme1s2[0] * 20:.2f}")
    print(f"- VIP: R${qtd_filme1s2[2] * 30:.2f}")
    print(f"- Meia: R${qtd_filme1s2[1] * 10:.2f}\n")

    print("\n<<<<<< Filme 2 - Sessão 1: >>>>>>")
    print("Quantidade de ingressos vendidos:")
    print(f"- Inteira:{qtd_filme2s1[0]}")
    print(f"- VIP:{qtd_filme2s1[2]}")
    print(f"- Meia:{qtd_filme2s1[1]}")

    print("\nReceita por tipo (Filme 2 - Sessão 1):")
    print(f"- Inteira: R${qtd_filme2s1[0] * 15:.2f}")
    print(f"- VIP: R${qtd_filme2s1[2] * 22.5:.2f}")
    print(f"- Meia: R${qtd_filme2s1[1] * 7.5:.2f}")

    print("\n<<<<<< Filme 2 - Sessão 2: >>>>>>\n")
    print("Quantidade de ingressos vendidos:")
    print(f"- Inteira:{qtd_filme2s2[0]}")
    print(f"- VIP:{qtd_filme2s2[2]}")
    print(f"- Meia:{qtd_filme2s2[1]}")

    print("\nReceita por tipo (Filme 2 - Sessão 2):")
    print(f"- Inteira: R${qtd_filme2s2[0] * 15:.2f}")
    print(f"- VIP: R${qtd_filme2s2[2] * 22.5:.2f}")
    print(f"- Meia: R${qtd_filme2s2[1] * 7.5:.2f}")



    print("\nMédia de avaliações:")
    if len(filme1_ava) != 0:
        mediaf1 = sum(filme1_ava) / len(filme1_ava)
        print(f"Filme 1: {mediaf1}")
    else:
        print("\nNão foram inseridos dados para o Filme 1\n")

    if len(filme2_ava) != 0:
        mediaf2 = sum(filme2_ava) / len(filme2_ava)
        print(f"Filme 2: {mediaf2}")
    else:
        print("\nNão foram inseridos dados para o Filme 2\n")

    if len(filme3_ava) != 0:
        mediaf3 = sum(filme3_ava) / len(filme3_ava)
        print(f"Filme 3: {mediaf3}")
    else:
        print("\nNão foram inseridos dados para o Filme 3\n")

    print(f"\nTotal de ingressos vendidos: {ing_p_tp.get('Total')}")

    medias = [mediaf1, mediaf2, mediaf3]
    return medias


def relatorio_final_txt(media_rf, ing_p_tp):
    with open("relatorio.txt", "w", encoding='utf-8') as arquivo:
        arquivo.write("*******  Relatório Final *******\n")
        arquivo.write("<<<<<< Filme 1 - Sessão 1: >>>>>>\n")
        arquivo.write("Quantidade de ingressos vendidos:")

        arquivo.write("\nMédia de avaliações:")
        if media_rf[0] != 0:
            arquivo.write(f"Filme 1: {media_rf[0]}")

        else:
            arquivo.write("\nNão foram inseridos dados para o Filme 1\n")

        if media_rf[1] != 0:
            arquivo.write(f"\nFilme 2: {media_rf[1]}")

        else:
            arquivo.write("\nNão foram inseridos dados para o Filme 2\n")

        if media_rf[2] != 0:
            arquivo.write(f"\nFilme 3: {media_rf[2]}")

        else:
            arquivo.write("\nNão foram inseridos dados para o Filme 3\n")

        arquivo.write(f"\nTotal de ingressos vendidos: {ing_p_tp.get('Total')}")


main()
