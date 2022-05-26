from src.services.logger_service import Logger
from src.services.arquivo_service import ArquivoService
from src.services import impressora_service

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PASTA_IMPRIMIR = r'C:\Imprimir'
PASTA_IMPRESSOS = r'C:\Impressos'


def executar():
    logger = Logger()

    arquivo_service = ArquivoService(
        PASTA_IMPRIMIR,
        PASTA_IMPRESSOS,
        logger
    )

    caminho_arquivos = arquivo_service.carregar_caminho_arquivos()

    if not caminho_arquivos:
        return

    service = Service(ChromeDriverManager().install())

    impressora_service.imprimir_arquivos(
        caminho_arquivos,
        webdriver.Chrome(service=service),
        logger
    )

    arquivo_service.mover_arquivos_para_pasta_impresso()

    logger.finalizar_log()


if __name__ == '__main__':
    executar()
