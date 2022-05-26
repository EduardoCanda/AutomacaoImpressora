from src.service.arquivo_service import ArquivoService
from src.service import impressora_service
from selenium import webdriver


def executar():
    pasta_imprimir = r'C:\Imprimir'
    pasta_impressos = r'C:\Impressos'

    arquivo_service = ArquivoService(
        pasta_imprimir,
        pasta_impressos
    )

    caminho_arquivos = arquivo_service.carregar_caminho_arquivos()

    impressora_service.imprimir_arquivos(
        caminho_arquivos,
        webdriver.Chrome()
    )

    arquivo_service.mover_arquivos_para_pasta_impresso()


if __name__ == '__main__':
    executar()
