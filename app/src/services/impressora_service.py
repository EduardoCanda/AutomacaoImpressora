import pyautogui as pg
import time

from typing import List

pg.PAUSE = 1


def imprimir_arquivos(caminho_arquivos: List[str], webdriver):
    for caminho in caminho_arquivos:
        webdriver.get(caminho)

        # Aguardar arquivo carregar no navegador
        time.sleep(3.5)

        # Selecionar ícone da impressora
        pg.hotkey('ctrl', 'p')
        time.sleep(1)

        # Apertar botão imprimir
        pg.press('enter')
        time.sleep(1)
