import shutil

from os import listdir
from os.path import isfile, join
from typing import List

from src.services.logger_service import Logger


class ArquivoService:
    def __init__(
            self,
            pasta_imprimir: str,
            pasta_impressos: str,
            logger: Logger
    ):
        self.arquivos = []
        self.arquivos_path = []
        self.pasta_imprimir = pasta_imprimir
        self.pasta_impressos = pasta_impressos
        self.logger = logger

    def carregar_caminho_arquivos(self) -> List[str]:
        self.arquivos = [
            f for f in listdir(self.pasta_imprimir) if isfile(
                join(self.pasta_imprimir, f)
            )
        ]

        self.arquivos_path = [
            f'{self.pasta_imprimir}/{arquivo}' for arquivo in self.arquivos
        ]

        self.logger.gravar_log(
            f'Caminho dos arquivos carregados: {self.arquivos_path}'
        )

        if not self.arquivos_path:
            self.logger.gravar_log('Não há arquivos para imprimir.')
            self.logger.gravar_log('Fim do programa.')

        return self.arquivos_path

    def mover_arquivos_para_pasta_impresso(self):
        for arquivo in self.arquivos:
            origem = f'{self.pasta_imprimir}/{arquivo}'
            destino = f'{self.pasta_impressos}/{arquivo}'
            shutil.move(origem, destino)

        self.logger.gravar_log(
            f'Arquivos {self.arquivos} movidos para a pasta {self.pasta_impressos}'
        )
