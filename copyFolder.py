import os
import shutil
from tqdm import tqdm

def copy_folders(source_dir, dest_dir):
    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Lista todas as pastas no diretório de origem
    folders = os.listdir(source_dir)
    
    # Loop sobre todas as pastas e copia cada uma
    for folder in tqdm(folders, desc="Copying", bar_format="{l_bar}{bar:50}{r_bar}", ncols=100, colour='green'):
        # Constrói o caminho completo para a pasta de origem e destino
        source_folder_path = os.path.join(source_dir, folder)
        dest_folder_path = os.path.join(dest_dir, folder)
        
        # Copia a pasta
        shutil.copytree(source_folder_path, dest_folder_path)

# Diretórios de origem e destino
source_directory = "C:\Users\brenn\Downloads\Musicas"
destination_directory = '/caminho/para/diretorio_de_destino'

# Chama a função para copiar as pastas
copy_folders(source_directory, destination_directory)
