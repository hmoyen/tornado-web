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

### Descrição
- O script abre o arquivo NetCDF e extrai metadados e variáveis como latitude, longitude, profundidade, tempo, u (velocidade zonal) e v (velocidade para meridional).
- Em seguida, converte as coordenadas de longitude para o formato desejado (graus a leste) e cria um objeto Basemap para visualização.
- O script gera um gráfico de vetores de corrente oceânica em um mapa, com preenchimento de costa e continente.
- Certifique-se de ajustar os parâmetros do Basemap, como limites de latitude e longitude, de acordo com a área geográfica dos seus dados.

### Notas
- Modifique os limites de longitude e latitude (`llcrnrlon`, `llcrnrlat`, `urcrnrlon`, `urcrnrlat`) no construtor do Basemap para se adequar à sua região geográfica de interesse.
- Descomente a linha `map.quiver()` para plotar vetores em um ponto específico no mapa. Ajuste os índices para plotar vetores em diferentes locais.

