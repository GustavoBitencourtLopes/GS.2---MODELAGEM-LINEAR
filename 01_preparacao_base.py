# ============================================================
# GS 2026.2 - Modelagem Linear para Aprendizado de Máquina
# Gustavo Bitencourt (RM 568885) e Daniel Vieira (RM 573326)
# Item 01 - Preparação da base de dados
# Fonte: IPS Brasil 2026 (Índice de Progresso Social), 5.570 municípios
# ============================================================

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

# 1. Leitura da base original
dados_originais = pd.read_csv('dados/IPS_Brasil_2026_-_Tabela_de_Dados_Brasil.csv',
                              encoding='utf-8-sig')
print('Formato da base original:', dados_originais.shape)

# 2. Seleção das variáveis da análise, com nomes curtos
colunas = {
    'Município': 'municipio',
    'UF': 'uf',
    'Expectativa de Vida ': 'expectativa_vida',
    'Nota Mediana no Enem': 'nota_enem',
    'Densidade de Internet Banda Larga Fixa': 'internet_banda_larga',
    'Ideb Ensino Fundamental': 'ideb_fundamental',
    'Gravidez na Adolescência (<19)': 'gravidez_adolescencia',
    'Esgotamento Sanitário Adequado': 'esgoto_adequado',
    'Abastecimento de Água Via Rede de Distribuição': 'agua_rede',
    'Domicílios com Coleta de Resíduos Adequada': 'coleta_lixo',
}
dados = dados_originais[list(colunas.keys())].rename(columns=colunas)

# 3. Verificação de dados faltantes e de municípios duplicados
print('\nDados faltantes por coluna:')
print(dados.isna().sum())
print('\nMunicípios duplicados (mesmo nome e mesma UF):',
      dados.duplicated(subset=['municipio', 'uf']).sum())

# 4. Resumo estatístico das variáveis
print('\nResumo das variáveis:')
print(dados.describe().round(2))

# 5. Salvar a base que será usada nos próximos itens
dados.to_csv('dados/base_ips_2026.csv', index=False, encoding='utf-8-sig')
print('\nBase salva em dados/base_ips_2026.csv com',
      dados.shape[0], 'municípios e', dados.shape[1], 'colunas.')