import csv

def ler_csv(caminho_arquivo):
    """Lê um arquivo CSV e retorna os dados como uma lista de dicionários."""
    dados = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

# Exemplo de uso
if __name__ == "__main__":
    caminho = 'caminho/para/seu/arquivo.csv'  # Substitua pelo caminho do seu arquivo CSV
    dados_lidos = ler_csv(caminho)
    print(dados_lidos)