# Copiador de Arquivos

Este é um script Python simples para copiar arquivos de um diretório para outro, adicionando um prefixo numérico aos nomes dos arquivos.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca `tqdm` instalada. Caso não tenha instalado, você pode instalar via pip:

```
pip install tqdm
```

## Como Usar

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/copiar-arquivos.git
```
2. Navegue até o diretório do script:
```
cd copiar-arquivos
```
3. Execute o script `copiar_arquivos.py`, especificando o diretório de origem e o diretório de destino:
```
python copiar_arquivos.py /caminho/para/diretorio/de/origem /caminho/para/diretorio/de/destino
```
Substitua `/caminho/para/diretorio/de/origem` pelo caminho do diretório de origem e `/caminho/para/diretorio/de/destino` pelo caminho do diretório de destino.

4. O script copiará os arquivos do diretório de origem para o diretório de destino, adicionando um prefixo numérico aos nomes dos arquivos.

## Observações

- A barra de progresso será exibida durante o processo de cópia dos arquivos.

