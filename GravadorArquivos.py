import os
import uuid
import requests


class GravadorArquivos:
    def __init__(self):
        self.caminho_responses = 'responses/'
        self.caminho_imagens = 'imagens/'

        self.criar_pasta(self.caminho_responses)
        self.criar_pasta(self.caminho_imagens)

    def criar_pasta(self, caminho):
        if not os.path.exists(caminho):
            os.makedirs(caminho)

    def gravar(self, response):
        id_aleatorio = uuid.uuid4()
        self.gravar_response(str(response), id_aleatorio)
        self.gravar_imagem(response.data[0].url, id_aleatorio)

    def gravar_response(self, data, id_aleatorio):
        nome_arquivo = f"{id_aleatorio}.txt"
        caminho_arquivo = os.path.join(self.caminho_responses, nome_arquivo)

        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(data)

    def gravar_imagem(self, url, id_aleatorio):
        nome_arquivo = f"{id_aleatorio}.png"
        caminho_arquivo = os.path.join(self.caminho_imagens, nome_arquivo)

        response = requests.get(url)
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(response.content)
