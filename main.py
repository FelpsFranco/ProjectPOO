from bola import Bola


def config_bola01(bola01):
    while True:
        bola01.mostra_cor()
        bola01.troca_cor()

        continuar_cor = input('\nContinuar? [S/N]')
        continuar_cor = continuar_cor[0].lower()
        if continuar_cor == 'n':
            break
    return bola01.cor


def config_bola02(bola02):
    while True:
        bola02.mostra_cor()
        bola02.troca_cor()

        continuar_cor = input('\nContinuar? [S/N]')
        continuar_cor = continuar_cor[0].lower()
        if continuar_cor == 'n':
            break
    return bola02.cor


def config_bola03(bola03):
    while True:
        bola03.mostra_cor()
        bola03.troca_cor()

        continuar_cor = input('\nContinuar? [S/N]')
        continuar_cor = continuar_cor[0].lower()
        if continuar_cor == 'n':
            break
    return bola03.cor

def config_bola04(bola04):
    bola04.nova_cor()
    bola04.novo_material()
    return bola04.cor, bola04.material


def op1(bola01):
    if bola01.estoque > 0:
        config_bola01(bola01)
        bola01.mostra_cor(), bola01.mostra_material(), bola01.mostra_circunferencia()
        compra = input('Deseja adquirir a bola? [S/N]')
        if compra == 'S' or 's':
            quantidade = int(input('Qual quantidade? '))
            bola01.estoque = bola01.estoque - quantidade
            if bola01.estoque > 0:
                print('Compra Realizada')
            else:
                print('Quantidade indisponível!')
    else:
        print('Produto Indísponivel.')


def op2(bola02):
    if bola02.estoque > 0:
        config_bola02(bola02)
        bola02.mostra_cor(), bola02.mostra_material(), bola02.mostra_circunferencia()
        compra = input('Deseja adquirir a bola? [S/N]')
        if compra == 'S' or 's':
            quantidade = int(input('Qual quantidade? '))
            bola02.estoque = bola02.estoque - quantidade
            if bola02.estoque > 0:
                print('Compra Realizada')
            else:
                print('Quantidade indisponível!')
    else:
        print('Produto Indísponivel.')


def op3(bola03):
    if bola03.estoque > 0:
        config_bola03(bola03)
        bola03.mostra_cor(), bola03.mostra_material(), bola03.mostra_circunferencia()
        compra = input('Deseja adquirir a bola? [S/N]')
        if compra == 'S' or 's':
            quantidade = int(input('Qual quantidade? '))
            bola03.estoque = bola03.estoque - quantidade
            if bola03.estoque > 0:
                print('Compra Realizada')
            else:
                print('Quantidade indisponível!')
    else:
        print('Produto Indísponivel.')

def op4(bola04):
    config_bola04(bola04)
    bola04.mostra_cor(), bola04.mostra_material(), bola04.mostra_circunferencia(), bola04.mostra_valor()

def compra(bola04):
    op4(bola04)
    print('Compra Realizada!\n')
    print('Configurações do produto:\n'
          'Cor -> {}\n'
          'Material -> {}'.format(bola04.cor, bola04.material))
    print('Valor a Pagar -> R${:.2f}'.format(bola04.valor))




def main():
    bola01 = Bola('Azul', 6, 'Pano', 15, 49.90)
    bola02 = Bola('Vermelha', 4, 'Plástico', 21, 39.90)
    bola03 = Bola('Branca', 10, 'Couro', 2, 69.90)
    bola04 = Bola('A ser Definido', 15, 'A ser Definido ', 1, 0.00)

    i = 'S'

    while i == 'S' or i == 's':
        if bola04.valor == 0:
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola01:')
            bola01.mostra_cor(), bola01.mostra_material(), bola01.mostra_circunferencia(), bola01.mostra_estoque(), bola01.mostra_valor(), bola01.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola02')
            bola02.mostra_cor(), bola02.mostra_material(), bola02.mostra_circunferencia(), bola02.mostra_estoque(), bola02.mostra_valor(), bola02.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola03')
            bola03.mostra_cor(), bola03.mostra_material(), bola03.mostra_circunferencia(), bola03.mostra_estoque(), bola03.mostra_valor(), bola03.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola04')
            bola04.mostra_cor(), bola04.mostra_material(), bola04.mostra_circunferencia(), bola04.mostra_estoque(), bola04.mostra_valor(), bola04.disponivel()

        else:
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola01:')
            bola01.mostra_cor(), bola01.mostra_material(), bola01.mostra_circunferencia(), bola01.mostra_estoque(), bola01.mostra_valor(), bola01.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola02')
            bola02.mostra_cor(), bola02.mostra_material(), bola02.mostra_circunferencia(), bola02.mostra_estoque(), bola02.mostra_valor(), bola02.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('INFORMAÇÕES Bola03')
            bola03.mostra_cor(), bola03.mostra_material(), bola03.mostra_circunferencia(), bola03.mostra_estoque(), bola03.mostra_valor(), bola03.disponivel()
            print('---------------------------------------------------------------------------------------------')
            print('PRODUTO EM CARRINHO')
            bola04.mostra_cor(), bola04.mostra_material(), bola04.mostra_circunferencia(), bola04.mostra_estoque(), bola04.mostra_valor()

        op = int(input('\nEscolha uma das bolas: '))

        if op == 1:
            op1(bola01)
            i = input('\nDeseja voltar as opções? [S/N]\n')

        if op == 2:
            op2(bola02)
            i = input('\nDeseja voltar as opções? [S/N]\n')

        if op == 3:
            op3(bola03)
            i = input('\nDeseja voltar as opções? [S/N]\n')

        if op == 4:
            if bola04.valor != 0:
                print('Produto já personalizado! Finalize a Venda')
                break
            else:
                compra(bola04)
                i = input('\nDeseja voltar as opções? [S/N]\n')


main()
print('Obrigado! Volte Sempre!')
