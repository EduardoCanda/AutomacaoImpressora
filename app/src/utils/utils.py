import os

PASTAS = [
    r'C:\Imprimir',
    r'C:\Impressos',
    r'C:\LogsImpressao'
]


def criar_pastas_caso_nao_exista():
    criou_pastas = False

    for pasta in PASTAS:
        if not os.path.isdir(pasta):
            os.mkdir(pasta)
            criou_pastas = True

    return criou_pastas
