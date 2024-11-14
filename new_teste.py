def main():
    main_menu = True

    filme1_ava = []
    filme2_ava = []
    filme3_ava = []

    mediaf1 = 0
    mediaf2 = 0
    mediaf3 = 0

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
            pass

        elif opcao_main == 2:
            pass

        elif opcao_main == 3:
            pass

        elif opcao_main == 4:
            pass

        elif opcao_main == 5:
            pass

        elif opcao_main == 6:
            pass

        elif opcao_main == 7:
            avaliar_filme(filme1_ava, filme2_ava, filme3_ava)

        elif opcao_main == 8:
            media_rf = relatorio_final(filme1_ava, mediaf1, filme2_ava, mediaf2, filme3_ava, mediaf3)
            relatorio_final_txt(media_rf)
            break

        else:
            print("\nDigite uma opção válida!(1 - 8)\n")


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


def relatorio_final(filme1_ava, mediaf1, filme2_ava, mediaf2, filme3_ava, mediaf3):

    print("\n*******  Relatório Final *******\n")

    print("<<<<<< Filme 1 - Sessão 1: >>>>>>\n")
    print("Quantidade de ingressos vendidos:")

    print("Receita por tipo (Filme 1 - Sessão 1):")


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

    medias = [mediaf1, mediaf2, mediaf3]
    return medias


def relatorio_final_txt(media_rf):
    with open("relatorio.txt", "w", encoding='utf-8') as arquivo:
        arquivo.write("*******  Relatório Final *******\n")
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


main()
