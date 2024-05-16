# Tornado Demo

Este é um simples exemplo de aplicativo web usando o framework Tornado em Python.

## Cloning this Repository

To clone this repository, and all of its submodules, use the following command:
```
git clone --recursive git@github.com:hmoyen/tornado-web.git
```

# Working with Submodules

Submodules are, simply put, repositories within repositories. In order to work with them, say, to commit, push, pull, etc. you can't just commit to the sky_ws repository, as all the changes you've made to the submodules won't be commited - instead, you have to either commit each submodule individually, or use the following command to do all the submodules at once.

```
git submodule foreach <your-desired-git-command>
```

then, do the same command to the sky_ws repository, as you would've normally.


## If you cloned this repository without the recursive flag

Just run the following commands to initialize the submodules

```
git submodule update --init --recursive
```


## Requisitos

Certifique-se de ter Python instalado em seu sistema. Este projeto foi desenvolvido e testado com Python 3.

Você pode instalar as dependências executando o seguinte comando:

```
pip install -r requirements.txt
```

## Executando o servidor

Para iniciar o servidor, execute o seguinte comando:

```
python webserver.py
```

Isso iniciará o servidor na porta 9090 por padrão. Você pode acessar o aplicativo em seu navegador visitando `http://localhost:9090`.

## Estrutura do projeto

- `webserver.py`: Este é o arquivo principal que contém a lógica do servidor web.
- `static/`: Este diretório contém os arquivos estáticos do aplicativo, como HTML, CSS e JavaScript.
- `web.py` e `view.py`: primeiros tutoriais seguidos

## Current-maps

### Arquivos:

1. **read.py:** Este script é responsável por ler o arquivo `.p3d` e gerar arquivos de velocidades e posições do campo vetorial das correntes. Ele extrai os dados do arquivo `.p3d` e cria arquivos de texto contendo as informações necessárias para plotar o campo vetorial.

2. **test_proj.py:** Este script utiliza os arquivos de velocidades e posições gerados pelo `read.py` para plotar o campo vetorial das correntes em um mapa. Ele utiliza a biblioteca `Basemap` do `matplotlib` para criar um mapa e `quiver` para representar as setas do campo vetorial.

### Instruções de Uso:

1. **read.py:**
   - Certifique-se de ter o arquivo `.p3d` no mesmo diretório que o script `read.py`.
   - Execute o script `read.py`. Ele irá ler o arquivo `.p3d` e gerar os arquivos de velocidades (`extracted_velx.txt` e `extracted_vely.txt`) e posições (`x_values.txt` e `y_values.txt`) do campo vetorial das correntes.

2. **test_proj.py:**
   - Certifique-se de ter os arquivos de velocidades (`extracted_velx.txt` e `extracted_vely.txt`) e posições (`x_values.txt` e `y_values.txt`) gerados pelo `read.py`, bem como o arquivo `test_proj.py`, no mesmo diretório.
   - Execute o script `test_proj.py`. Ele irá ler os arquivos de velocidades e posições, plotar o campo vetorial das correntes em um mapa e exibir o mapa resultante.


