import pyautogui as pg
import time

from typing import List
from src.services.logger_service import Logger

pg.PAUSE = 2


def imprimir_arquivos(
        caminho_arquivos: List[str],
        webdriver,
        logger: Logger
):
    logger.gravar_log('Iniciando serviço de impressão...')

    contador = 0

    for caminho in caminho_arquivos:
        # Abrir arquivo no navegador
        webdriver.get(caminho)
        time.sleep(1)

        # Selecionar ícone da impressora
        pg.hotkey('ctrl', 'p')
        contador += 1

        # Aguardar arquivo carregar no navegador
        if contador == 1:
            logger.gravar_log('Adicionando primeiro arquivo da fila de impressão...')
            logger.gravar_log('Aguardando 30 segundos para o próximo arquivo a ser impresso...')
            time.sleep(30)
        else:
            time.sleep(2.5)

        # Apertar botão imprimir
        pg.press('enter')
        logger.gravar_log(f'Arquivo {caminho} adicionado na fila de impressão.')
