import pyautogui as pg
import time

from typing import List
from src.services.logger_service import Logger

pg.PAUSE = 1


def imprimir_arquivos(
        caminho_arquivos: List[str],
        webdriver,
        logger: Logger
):
    logger.gravar_log('Iniciando serviço de impressão...')

    for caminho in caminho_arquivos:
        # Abrir arquivo no navegador
        webdriver.get(caminho)

        # Aguardar arquivo carregar no navegador
        time.sleep(3.5)

        # Selecionar ícone da impressora
        pg.hotkey('ctrl', 'p')
        time.sleep(1)

        # Apertar botão imprimir
        pg.press('enter')
        time.sleep(1)
        logger.gravar_log(f'Arquivo {caminho} adicionado na fila de impressão.')
