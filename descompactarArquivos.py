import os
import zipfile
import sys
import asyncio
from tqdm import tqdm

async def extrair_arquivos_zip(pasta_origem, pasta_destino):
    # Verifica se o diretório de destino existe, se não, cria um
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Conta o total de arquivos a serem extraídos
    total_arquivos = sum(1 for arquivo in os.listdir(pasta_origem) if arquivo.endswith('.zip'))
    arquivos_extraidos = 0

    # Lista de tarefas assíncronas
    tasks = []

    # Percorre todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        # Verifica se o arquivo é um arquivo zip
        if arquivo.endswith('.zip'):
            # Constrói o caminho completo do arquivo zip de origem
            caminho_arquivo_zip = os.path.join(pasta_origem, arquivo)
            # Adiciona a tarefa assíncrona à lista de tarefas
            tasks.append(extrair_arquivo_zip_async(caminho_arquivo_zip, pasta_destino))
            arquivos_extraidos += 1

    # Executa todas as tarefas assíncronas
    await asyncio.gather(*tasks)

async def extrair_arquivo_zip_async(caminho_arquivo_zip, pasta_destino):
    # Extrai os arquivos do zip para a pasta de destino
    with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
        for item in tqdm(zip_ref.namelist(), desc="Extraindo arquivos", unit="arquivo", bar_format="{l_bar}{bar}{r_bar}", colour='green'):
            zip_ref.extract(item, pasta_destino)

if __name__ == "__main__":
    # Verifica se os argumentos foram passados corretamente
    if len(sys.argv) != 3:
        faltando = ""
        if len(sys.argv) < 2:
            faltando = "diretório de origem"
        elif len(sys.argv) < 3:
            faltando = "diretório de destino"
        print(f"Os argumentos {faltando} são necessários.")
        sys.exit(1)

    # Obtém os diretórios de origem e destino dos argumentos
    diretorio_origem = sys.argv[1]
    diretorio_destino = sys.argv[2]

    # Inicia o loop de evento assíncrono
    asyncio.run(extrair_arquivos_zip(diretorio_origem, diretorio_destino))