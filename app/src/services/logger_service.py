from datetime import datetime

PASTA_LOGS = r'C:\LogsImpressao'


class Logger:
    def __init__(self):
        self.__data_atual = datetime.now().strftime('%Y-%m-%d %H-%M')
        self.__arquivo = open(
            f'{PASTA_LOGS}/Logs - {self.__data_atual}.txt',
            "w+"
        )

    def gravar_log(self, mensagem):
        self.__arquivo.write(mensagem + '\n')

    def finalizar_log(self):
        self.gravar_log('Fim do programa.')
        self.__arquivo.close()
