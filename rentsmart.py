"""Orçamento de locação da R.M Imóveis. Execute: python rentsmart.py"""
import csv
from decimal import Decimal
from pathlib import Path


class Imovel:
    def __init__(self, categoria, quartos=1, vagas=0, sem_criancas=False):
        self.categoria = categoria
        self.quartos = quartos
        self.vagas = vagas
        self.sem_criancas = sem_criancas
        if categoria not in ('apartamento', 'casa', 'estudio'):
            raise ValueError('Categoria inválida.')
        if categoria == 'estudio':
            if quartos != 1 or vagas < 0 or sem_criancas:
                raise ValueError('Dados inválidos para estúdio.')
        elif quartos not in (1, 2) or vagas not in (0, 1):
            raise ValueError('Casa/apartamento: 1 ou 2 quartos e 0 ou 1 vaga.')
        if categoria == 'casa' and sem_criancas:
            raise ValueError('O desconto é exclusivo para apartamentos.')

    def aluguel_base(self):
        return {'apartamento': Decimal('700'), 'casa': Decimal('900'),
                'estudio': Decimal('1200')}[self.categoria]

    def adicional_quartos(self):
        if self.quartos == 2:
            return Decimal('200' if self.categoria == 'apartamento' else '250')
        return Decimal('0')

    def adicional_vagas(self):
        if self.categoria == 'estudio':
            # Uma vaga isolada não tem preço no enunciado: só há pacote de duas.
            return Decimal('250') + Decimal('60') * (self.vagas - 2) if self.vagas >= 2 else Decimal('0')
        return Decimal('300') * self.vagas

    def desconto(self):
        if self.categoria == 'apartamento' and self.sem_criancas:
            return (self.aluguel_base() + self.adicional_quartos() +
                    self.adicional_vagas()) * Decimal('0.05')
        return Decimal('0')

    def aluguel_mensal(self):
        return (self.aluguel_base() + self.adicional_quartos() +
                self.adicional_vagas() - self.desconto())


class Orcamento:
    TAXA_CONTRATUAL = Decimal('2000')

    def __init__(self, imovel, parcelas):
        if not 1 <= parcelas <= 5:
            raise ValueError('A taxa deve ser paga em 1 a 5 parcelas.')
        self.imovel = imovel
        self.parcelas = parcelas

    def parcela_taxa(self):
        return self.TAXA_CONTRATUAL / self.parcelas

    def valor_mes(self, mes):
        if not 1 <= mes <= 12:
            raise ValueError('Mês inválido.')
        taxa = self.parcela_taxa() if mes <= self.parcelas else Decimal('0')
        return self.imovel.aluguel_mensal(), taxa

    def gerar_csv(self, caminho):
        with open(caminho, 'w', newline='', encoding='utf-8-sig') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerow(['Mês', 'Aluguel mensal (R$)', 'Parcela da taxa (R$)', 'Total do mês (R$)'])
            for mes in range(1, 13):
                aluguel, taxa = self.valor_mes(mes)
                escritor.writerow([mes, csv_valor(aluguel), csv_valor(taxa),
                                   csv_valor(aluguel + taxa)])


def csv_valor(valor):
    return f'{valor:.2f}'.replace('.', ',')


def moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def escolher_opcao(pergunta, opcoes):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in opcoes:
            return resposta
        print('Opção inválida. Escolha:', ', '.join(opcoes))


def escolher_numero(pergunta, minimo, maximo=None):
    while True:
        texto = input(pergunta).strip()
        if texto.isdecimal():
            numero = int(texto)
            if numero >= minimo and (maximo is None or numero <= maximo):
                return numero
        limite = f' a {maximo}' if maximo is not None else ' ou mais'
        print(f'Digite um número inteiro de {minimo}{limite}.')


def main():
    print('=== RentSmart | R.M Imóveis ===')
    categoria = escolher_opcao('Imóvel (1 apartamento, 2 casa, 3 estúdio): ', ('1', '2', '3'))
    categoria = {'1': 'apartamento', '2': 'casa', '3': 'estudio'}[categoria]
    if categoria == 'estudio':
        quartos = 1
        print('Estúdio: 1 quarto. O estacionamento é vendido em pacote inicial de 2 vagas.')
        estacionamento = escolher_opcao('Deseja o pacote de estacionamento? (s/n): ', ('s', 'n'))
        vagas = 2 + escolher_numero('Quantas vagas adicionais? ', 0) if estacionamento == 's' else 0
        sem_criancas = False
    else:
        quartos = escolher_numero('Número de quartos (1 ou 2): ', 1, 2)
        vagas = 1 if escolher_opcao('Deseja uma vaga de garagem? (s/n): ', ('s', 'n')) == 's' else 0
        sem_criancas = (categoria == 'apartamento' and
                        escolher_opcao('Há crianças na locação? (s/n): ', ('s', 'n')) == 'n')
    parcelas = escolher_numero('Parcelas da taxa contratual (1 a 5): ', 1, 5)
    orcamento = Orcamento(Imovel(categoria, quartos, vagas, sem_criancas), parcelas)
    imovel = orcamento.imovel
    print('\n=== RESUMO DO ORÇAMENTO ===')
    print(f'Imóvel: {categoria} | Quartos: {quartos} | Vagas: {vagas}')
    print(f'Aluguel-base:           {moeda(imovel.aluguel_base())}')
    print(f'Adicional de quartos:   {moeda(imovel.adicional_quartos())}')
    print(f'Adicional de vagas:     {moeda(imovel.adicional_vagas())}')
    print(f'Desconto (5%):          -{moeda(imovel.desconto())}')
    print(f'ALUGUEL MENSAL:         {moeda(imovel.aluguel_mensal())}')
    print(f'Taxa contratual:        {moeda(orcamento.TAXA_CONTRATUAL)}')
    print(f'Pagamento da taxa:      {parcelas} x {moeda(orcamento.parcela_taxa())}')
    primeiro, taxa_primeiro = orcamento.valor_mes(1)
    print(f'Total no primeiro mês:  {moeda(primeiro + taxa_primeiro)}')
    caminho = Path(__file__).with_name('projecao_12_meses.csv')
    orcamento.gerar_csv(caminho)
    print(f'Projeção de 12 meses salva em: {caminho}')


if __name__ == '__main__':
    main()
