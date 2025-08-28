# CSV to KML

Este projeto converte arquivos CSV de relatórios de posição detalhado da tecnologia Sascar contendo dados de rastreamento de veículos em arquivos KML compatíveis com Google My Maps.

## Funcionalidade
- Processa todos os arquivos `.csv` da pasta.
- Para cada CSV, gera arquivos KML com até 2000 pontos por arquivo.
- Cada ponto é representado por um pin com informações detalhadas.
- Os pontos de cada arquivo KML são conectados por uma linha (trajeto).

## Requisitos
- Python 3.x
- Nenhuma dependência externa além da biblioteca padrão.

## Como usar
1. Coloque seus arquivos CSV na mesma pasta do script `csv_to_kml.py`.
2. Execute o script:
   ```
   python csv_to_kml.py
   ```
3. Serão gerados arquivos KML para cada CSV encontrado.

## Observações
- Os arquivos KML podem ser importados diretamente no Google My Maps.
- Cada arquivo KML conecta apenas os pontos presentes nele.
- Este repositório inclui este script em um arquivo .exe. Ele funcionará de maneira independente da mesma forma que o script executado pelo terminal.

## Autor
- Lucas Rafael da Silva
