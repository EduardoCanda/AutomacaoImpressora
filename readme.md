## Este projeto serve para mandar arquivos para a impressão automaticamente.

### Pacotes externos instalados:
    selenium==4.1.5
    PyAutoGUI==0.9.53
    webdriver_manager==3.7.0
    pyinstaller==5.1

### Para utilizar este programa, é necessário criar três pastas no C:\
    C:\Imprimir
    O programa vai ler os arquivos à serem imprimidos a partir desta pasta.
    
    C:\Impressos
    O programa utiliza essa pasta para mover os arquivos que já foram impressos pela sua impressora.

    C:\LogsImpressao
    Nesta pasta, o programa vai gerar um arquivo .txt com os logs de execução.

### OBS:
    Caso essas pastas não estejam criadas, o programa vai se encarregar de criar as mesmas. 
    Basta executar programa a primeira vez para criar as pastas. 
    Após as pastas estarem criadas, a execução do programa vai ocorrer como esperado. 
