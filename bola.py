class Bola:
    def __init__(self, cor='unknown', circunferencia=0, material='unknown', estoque=0, valor=0):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.estoque = estoque
        self.valor = valor

    def mostra_estoque(self):
        return print('Estoque atual: {}'.format(self.estoque))

    def mostra_valor(self):
        return print('O valor da bola é: R${:.2f}'.format(self.valor))

    def disponivel(self):
        if self.estoque > 0:
            return print('Está a Venda!')
        else:
            return print('Produto Indisponível para Personalização!')

    def mostra_circunferencia(self):
        return print('A circunferência é: {}'.format(self.circunferencia))


    def nova_cor(self):
        cores = input('Qual a cor desejada? ')
        self.cor = cores

    def troca_cor(self):
        troca = input('Deseja mudar a cor atual {}? [S/N]'.format(self.cor))

        troca = troca[0].lower()

        if troca == 's':
            nova_cor = input('\n Nova cor: ')
            self.cor = nova_cor
        else:
            print('Ok a cor continua {}'.format(self.cor))

    def mostra_cor(self):
        print('A cor atual é: {}'.format(self.cor))

    def novo_material(self):
        materiais = input('Qual Material deseja utilizar?\n'
                         'Couro\n'
                         'Plástico\n'
                         'Bola de Leite\n')
        if materiais == 'Couro':
            self.material = materiais
            self.valor = self.valor + 109.00
        if materiais == 'Plástico' or materiais == 'Plastico':
            self.material = materiais
            self.valor = self.valor + 89.90
        if materiais == 'Bola de Leite':
            self.material = materiais
            self.valor = self.valor + 29.90



    def troca_material(self):
        troca_m = input('Deseja mudar o material atual {}? [S/N]'.format(self.material))
        troca_m = troca_m[0].lower()

        if troca_m == 's':
            novo_material = input('\n Novo material: ')
            self.material = novo_material
        else:
            print('A cor {} não foi alterada.'.format(self.material))

    def mostra_material(self):
        print('O Material atual é: {}'.format(self.material))