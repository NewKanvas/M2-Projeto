from time import sleep
import os
from questionario import *
from cores import *

# index.py e o arquivo principal que importada todos esses metodos e inicia cada um.
# Todas a funções são importadas e iniciadas para criar o candidato


# iniciar Classe
def iniciar():
    while True:
        respostas = {}  # Armazena as respostas

        # Inicia as perguntas
        idade(respostas)
        genero(respostas)
        estado(respostas)
        perguntas(respostas)
        # Criando Classe
        p = Candidato(
            respostas["Idade"],
            respostas["Genero"],
            respostas["Estado"],
            respostas["R1"],
            respostas["R2"],
            respostas["R3"],
            respostas["R4"],
        )
        # Depois ele e salvo com função da classe no arquivo csv
        p.salvar()


# Mensagem de Apresentação


def apresentacao():
    os.system("cls")

    print("**Pesquisa sobre Diversidade no Local de Trabalho**\n")
    sleep(3)
    os.system("cls")

    print("Bem-vindo à nossa pesquisa sobre diversidade no local de trabalho!\n")

    sleep(2)

    print(
        "Estamos empenhados em promover um ambiente de trabalho inclusivo e igualitário para todos os nossos colaboradores."
    )

    sleep(2)

    print(
        "Esta pesquisa tem como objetivo coletar opiniões e percepções sobre a diversidade e inclusão em nossa organização."
    )

    sleep(2)

    print(
        "Suas respostas são extremamente valiosas e nos ajudarão a tomar medidas para melhorar nossa cultura empresarial.\n"
    )
    input(f"{y}Pressione Enter para continuar...{rt}")


apresentacao()
iniciar()
