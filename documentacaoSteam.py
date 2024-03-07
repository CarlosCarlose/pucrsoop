import csv
from collections import Counter, defaultdict

def ler_arquivo_csv(nome_arquivo):
    """
    Esta função lê um arquivo CSV e retorna três listas: uma com os anos de lançamento dos jogos,
    uma com os preços dos jogos e um dicionário com a soma das avaliações positivas para cada gênero
    em 2022.
    Nota: O exemplo acima é um teste doctest. 'steam_games.csv' de um arquivo pessoal. Caso reutileze a função, necessitara fazer 
    alterações na mesma.

    >>> anos, precos, generos_positivos = ler_arquivo_csv('steam_games.csv')
    >>> type(anos)
    <class 'list'>
    >>> type(precos)
    <class 'list'>
    >>> type(generos_positivos)
    <class 'collections.defaultdict'>
    """
    anos = []
    precos = []
    generos_positivos = defaultdict(int)
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                data_lancamento = linha['Release date']
                ano_lancamento = data_lancamento.split(',')[-1].strip()  # Extrai o ano
                preco = float(linha['Price'])
                generos = linha['Genres']
                positivo = int(linha['Positive'])
                anos.append(ano_lancamento)
                precos.append(preco)
                if ano_lancamento == '2022':
                    generos_positivos[generos] += positivo
            except ValueError as e:
                print(f"Erro ao processar a linha {linha}: {e}")
    return anos, precos, generos_positivos


class AnoMaisFrequente:
    """
    Esta classe recebe uma lista de anos e tem um método `ano_mais_frequente` que retorna o ano que mais aparece.

    >>> dados_ano = AnoMaisFrequente(['2022', '2021', '2022', '2023', '2022'])
    >>> dados_ano.ano_mais_frequente()
    '2022'
    """
    def __init__(self, anos):
        self.anos = anos

    def ano_mais_frequente(self):
        contador = Counter(self.anos)
        ano_mais_frequente = contador.most_common(1)[0][0]
        return ano_mais_frequente
    


class PorcentagemPreco:
    """
    Esta classe recebe uma lista de preços e tem um método `calcular_porcentagens` que retorna a porcentagem de jogos gratuitos e pagos.

    >>> dados_preco = PorcentagemPreco([0, 0, 10, 20, 0])
    >>> dados_preco.calcular_porcentagens()
    (60.0, 40.0)
    """
    def __init__(self, precos):
        self.precos = precos

    def calcular_porcentagens(self):
        gratuitos = self.precos.count(0)
        pagos = len(self.precos) - gratuitos
        porcentagem_gratuitos = (gratuitos / len(self.precos)) * 100
        porcentagem_pagos = (pagos / len(self.precos)) * 100
        return porcentagem_gratuitos, porcentagem_pagos

class GeneroMaisPositivo:
    """
    Esta classe recebe um dicionário onde as chaves são os gêneros e os valores são as somas das avaliações positivas para os jogos lançados em 2022.
    Tem um método `genero_mais_positivo` que retorna o gênero com a maior soma de avaliações positivas.

    >>> dados_genero = GeneroMaisPositivo({'Ação': 100, 'Aventura': 200, 'Action,RPG': 300})
    >>> dados_genero.genero_mais_positivo()
    'Action,RPG'
    """
    def __init__(self, generos_positivos):
        self.generos_positivos = generos_positivos

    def genero_mais_positivo(self):
        genero_mais_positivo = max(self.generos_positivos, key=self.generos_positivos.get)
        return genero_mais_positivo
    

#Estou usando o próximo comando pra execultar o teste doc automático

if __name__ == "__main__":
    import doctest
    doctest.testmod()
