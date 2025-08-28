import csv
import os

def monta_description(row):
    # Monta o bloco HTML para o CDATA
    desc = f"<body><b>Veículo: </b>KEL3D30<br/>Sensores: <b>VPa</b> - Violação de Painel / <b>SPM</b> - Sensor Porta Motorista / <b>SPC</b> - Sensor Porta Carona / <b>Des</b> - Desengate / <b>SBT</b> - Sensor Bau Traseiro<br/>Atuadores: <b>Sir</b> - Sirene / <b>TBT</b> - Trava Bau Traseiro<br/>Acessórios: --<br/>Data Posição: {row['Data Posicão']}<br/>Data Chegada: {row['Data Chegada']}<br/>Velocidade: {row['Vel.']}<br/>Ignicao: {row['Ign']}<br/>Bateria: {row['Bat.']}<br/>Bloqueio: {row['Bloq']}<br/>Latitude: {row['Latitude']}<br/>Longitude: {row['Longitude']}<br/>UF: {row['UF']}<br/>Município: {row['Cidade']}<br/>Rua: {row['Rua']}<br/>Número: {row['N.']}<br/>GPS: {row['GPS']}<br/>Memória: {row['Mem']}<br/>Satélite: {row['Sat']}<br/>Sens. Atv.: {row['S. Ativados']}<br/>Atu. Atv.: {row['A. Ativados']}<br/>Pto. Embarcado: {row['Ponto de Ref. Embarcado']}<br/>Ponto Referência: {row['Ponto de Referência']}<br/>Rota: {row['Rota']}<br/>Em Operação: {row['Opera��o']}<br/>Panico: {row['P�nico']}<br/>Ancora: {row['�ncora']}<br/>" 
    return desc

def monta_name(row):
    # Extrai data/hora, velocidade, cidade/UF
    data = row['Data Posicão'].split(': ')[-1].split(' (')[0]
    data = ' '.join(data.split()[:2])
    vel = row['Vel.']
    cidade = row['Cidade']
    uf = row['UF']
    return f"{data} | Vel: {vel} | {cidade}/{uf}"

def decide_style(row):
    # Define o estilo do placemark, sendo vermelho para posições com violação de baú, painel ou desengate e azul para posições sem essas violações
    sens = row['S. Ativados']
    if any(x in sens for x in ['VPa', 'SBT', 'Des']):
        return '#estilo_2'
    return '#estilo_1'

def main():
    # Processa todos os arquivos CSV na pasta
    csv_files = [f for f in os.listdir('.') if f.lower().endswith('.csv')]
    estilos = '''<Style id="estilo_1">\n <IconStyle>\n  <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>\n  </Icon>\n </IconStyle>\n</Style>\n<Style id="estilo_2">\n <IconStyle>\n  <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/red-blank.png</href>\n  </Icon>\n </IconStyle>\n</Style>'''
    chunk_size = 2000 # Limita a 2000 placemarks por arquivo KML
    for csv_path in csv_files:
        base_kml_path = os.path.splitext(csv_path)[0]
        with open(csv_path, encoding='iso-8859-1') as f:
            # Corrige a codificação do arquivo e caracteres corrompidos
            reader = csv.DictReader(f, delimiter=';')
            colunas = {col.lower().replace('ã', 'a').replace('�', 'a').replace('í', 'i').replace('ó', 'o').replace('ç', 'c').replace('é', 'e').replace('ê', 'e').replace('ô', 'o').replace('á', 'a').replace('ú', 'u').replace('â', 'a').replace(' ', '').replace('.', '').replace('�', ''): col for col in reader.fieldnames}
            def get(row, nome):
                nome = nome.lower().replace('ã', 'a').replace('�', 'a').replace('í', 'i').replace('ó', 'o').replace('ç', 'c').replace('é', 'e').replace('ê', 'e').replace('ô', 'o').replace('á', 'a').replace('ú', 'u').replace('â', 'a').replace(' ', '').replace('.', '').replace('�', '')
                return row.get(colunas.get(nome, nome), '')
            placemarks = []
            coords_list = []
            for row in reader:
                desc = f"<body><b>Veículo: </b>KEL3D30<br/>Sensores: <b>VPa</b> - Violação de Painel / <b>SPM</b> - Sensor Porta Motorista / <b>SPC</b> - Sensor Porta Carona / <b>Des</b> - Desengate / <b>SBT</b> - Sensor Bau Traseiro<br/>Atuadores: <b>Sir</b> - Sirene / <b>TBT</b> - Trava Bau Traseiro<br/>Acessórios: --<br/>Data Posição: {get(row, 'Data Posicao')}<br/>Data Chegada: {get(row, 'Data Chegada')}<br/>Velocidade: {get(row, 'Vel')}<br/>Ignicao: {get(row, 'Ign')}<br/>Bateria: {get(row, 'Bat')}<br/>Bloqueio: {get(row, 'Bloq')}<br/>Latitude: {get(row, 'Latitude')}<br/>Longitude: {get(row, 'Longitude')}<br/>UF: {get(row, 'UF')}<br/>Município: {get(row, 'Cidade')}<br/>Rua: {get(row, 'Rua')}<br/>Número: {get(row, 'N')}<br/>GPS: {get(row, 'GPS')}<br/>Memória: {get(row, 'Mem')}<br/>Satélite: {get(row, 'Sat')}<br/>Sens. Atv.: {get(row, 'S Ativados')}<br/>Atu. Atv.: {get(row, 'A Ativados')}<br/>Pto. Embarcado: {get(row, 'Ponto de Ref Embarcado')}<br/>Ponto Referência: {get(row, 'Ponto de Referencia')}<br/>Rota: {get(row, 'Rota')}<br/>Em Operação: {get(row, 'Operacao')}<br/>Panico: {get(row, 'Panico')}<br/>Ancora: {get(row, 'Ancora')}<br/>"
                data = get(row, 'Data Posicao').split(': ')[-1].split(' (')[0]
                data = ' '.join(data.split()[:2])
                vel = get(row, 'Vel')
                cidade = get(row, 'Cidade')
                uf = get(row, 'UF')
                name = f"{data} | Vel: {vel} | {cidade}/{uf}"
                sens = get(row, 'S Ativados')
                style = '#estilo_2' if any(x in sens for x in ['VPa', 'SBT', 'Des']) else '#estilo_1'
                lat = get(row, 'Latitude').replace(',', '.')
                lon = get(row, 'Longitude').replace(',', '.')
                placemark = f'''<Placemark>\n<description><![CDATA[{desc}]]></description>\n<name>{name}</name>\n<visibility>1</visibility>\n<Point>\n<coordinates> {lon},{lat}</coordinates></Point>\n<styleUrl>{style}</styleUrl></Placemark>'''
                placemarks.append(placemark)
                coords_list.append(f'{lon},{lat}')
        total = len(placemarks)
        num_files = (total + chunk_size - 1) // chunk_size
        for i in range(num_files):
            kml_path = f'{base_kml_path}_{i+1}.kml'
            chunk = placemarks[i*chunk_size:(i+1)*chunk_size]
            chunk_coords = coords_list[i*chunk_size:(i+1)*chunk_size]
            # Adiciona a linha conectando apenas os pontos do chunk
            linestring_placemark = ''
            if chunk_coords:
                linestring_placemark = f'''<Placemark>\n<name>Trajeto</name>\n<styleUrl>#estilo_linha</styleUrl>\n<LineString>\n<extrude>1</extrude>\n<tessellate>1</tessellate>\n<coordinates>\n{chr(10).join(chunk_coords)}\n</coordinates>\n</LineString>\n</Placemark>'''
            kml = f'''<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns="http://earth.google.com/kml/2.2">\n   <Document>\n{estilos}\n<LineStyle id="estilo_linha">\n     <color>ff0000</color>\n     <width>4</width>\n    </LineStyle>\n{linestring_placemark}\n{chr(10).join(chunk)}\n   </Document>\n </kml>'''
            with open(kml_path, 'w', encoding='utf-8') as f: # Codifica em UTF-8
                f.write(kml)

if __name__ == '__main__':
    main()
