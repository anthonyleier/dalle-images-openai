import sys
from GeradorImagens import GeradorImagens
from GravadorArquivos import GravadorArquivos


def main():
    argumentos = sys.argv[1:]
    prompt = ' '.join(argumentos)

    gerador_imagens = GeradorImagens()
    gravador_arquivos = GravadorArquivos()

    response = gerador_imagens.gerar(prompt)
    gravador_arquivos.gravar(response)


if __name__ == "__main__":
    main()
