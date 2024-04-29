import os
import shutil
import sys
from tqdm import tqdm

def copiar_arquivos_para_qtd(diretorio_origem, diretorio_destino):
    
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    arquivos_a_copiar = []
    for pasta_atual, _, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            if arquivo.endswith(('.mp3', '.wav', '.flac', '.aac')):
                arquivos_a_copiar.append(os.path.join(pasta_atual, arquivo))

    arquivos_a_copiar.sort()

    total_arquivos = len(arquivos_a_copiar)

    
    barra_progresso = tqdm(total=total_arquivos, desc="Copiando arquivos", unit="arquivo", bar_format="{l_bar}{bar}{r_bar}", colour='green')

    
    for i, caminho_arquivo_origem in enumerate(arquivos_a_copiar):
        
        nome_arquivo = os.path.basename(caminho_arquivo_origem)
        
        novo_nome = f"{i:03d} - {nome_arquivo.split('-', 1)[-1]}"
        
        caminho_arquivo_destino = os.path.join(diretorio_destino, novo_nome)
        
        shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)

        barra_progresso.update(1)

    barra_progresso.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        faltando = ""
        if len(sys.argv) < 2:
            faltando = "diretório de origem"
        elif len(sys.argv) < 3:
            faltando = "diretório de destino"
        print(f"Os argumentos {faltando} são necessários.")
        sys.exit(1)

    diretorio_origem = sys.argv[1]
    diretorio_destino = sys.argv[2]

    copiar_arquivos_para_qtd(diretorio_origem, diretorio_destino)
