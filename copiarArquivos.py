import os
import shutil

def mover_arquivos_para_qtd(diretorio_origem, diretorio_destino):
    # Verifica se o diretório de destino "QTD" existe, se não, cria um
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)
        print(diretorio_origem)

    # Percorre recursivamente todas as pastas e subpastas no diretório de origem
    for pasta_atual, _, arquivos in os.walk(diretorio_origem):
        # Para cada arquivo na pasta atual
        for arquivo in arquivos:
            # Verifica se o arquivo é uma música (você pode adicionar mais extensões de música, se necessário)
            if arquivo.endswith(('.mp3', '.wav', '.flac', '.aac')):
                # Constrói o caminho completo do arquivo de origem
                caminho_arquivo_origem = os.path.join(pasta_atual, arquivo)
                # Constrói o caminho completo do arquivo de destino na pasta "QTD"
                caminho_arquivo_destino = os.path.join(diretorio_destino, arquivo)
                # Move o arquivo para o diretório de destino
                shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
                print(f"Movido: {caminho_arquivo_origem} -> {caminho_arquivo_destino}")

# Diretório de origem que contém as músicas e subpastas
diretorio_origem = "C:\Users\brenn\Downloads\Musicas"
# Diretório de destino onde os arquivos serão movidos
diretorio_destino = "caminho/para/pasta/QTD"

# Chama a função para mover os arquivos
mover_arquivos_para_qtd(diretorio_origem, diretorio_destino)