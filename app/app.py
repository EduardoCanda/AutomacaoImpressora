from src.services.logger_service import Logger
from src.services.arquivo_service import ArquivoService
from src.services import impressora_service

from src.utils.utils import criar_pastas_caso_nao_exista

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


def executar():
    criou = criar_pastas_caso_nao_exista()

    logger = Logger()
    logger.gravar_log('Iniciando execução...')

    logger.gravar_log('Verificando necessidade de criar as pastas...')
    if criou:
        logger.gravar_log('Este computador não tinha uma ou mais pastas criadas para utilizar este programa.')
        logger.gravar_log('O programa se encarregou de criar as pastas.')
        logger.gravar_log('De agora em diante, é só utilizar o programa normalmente, pois as pastas foram criadas.')
        logger.finalizar_log()
        return

    pasta_imprimir = r'C:\Imprimir'
    pasta_impressos = r'C:\Impressos'

    arquivo_service = ArquivoService(
        pasta_imprimir,
        pasta_impressos,
        logger
    )

    caminho_arquivos = arquivo_service.carregar_caminho_arquivos()

    if not caminho_arquivos:
        logger.finalizar_log()
        return

    logger.gravar_log('Conferindo webdriver...')
    service = Service(ChromeDriverManager(path=r'./chromedriver').install())
    # service = Service(r'./chromedriver.exe')

    impressora_service.imprimir_arquivos(
        caminho_arquivos,
        webdriver.Chrome(service=service),
        logger
    )

    arquivo_service.mover_arquivos_para_pasta_impresso()

    logger.finalizar_log()


if __name__ == '__main__':
    executar()
