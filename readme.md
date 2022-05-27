## Este projeto serve para mandar arquivos PDF para a impressão automaticamente.

### Pacotes externos instalados:
    selenium==4.1.5
    PyAutoGUI==0.9.53
    webdriver_manager==3.7.0
    pyinstaller==5.1

### Pré-requisitos para utilizar este software:

#### 1 - É necessário criar três pastas no C:\
    C:\Imprimir
    O software vai ler os arquivos à serem imprimidos a partir desta pasta.
    
    C:\Impressos
    O software utiliza essa pasta para mover os arquivos que já foram impressos pela sua impressora.

    C:\LogsImpressao
    Nesta pasta, o software vai gerar um arquivo .txt com os logs de execução.
    
    OBS:
    Caso essas pastas não estejam criadas, o software vai se encarregar de criar as mesmas. 
    Basta executar software a primeira vez para criar as pastas. 
    Após as pastas estarem criadas, a execução do software vai ocorrer como esperado. 

#### 2 - Utilizar o navegador Google Chrome:
    Este software utiliza o Chrome para ler os arquivos PDF e manda-los a impressora.
    Além disso, o software utiliza um driver nativo do Chrome para o navegador ser controlado auirátomaticamente.
    Não irá funcionar em outros navegadores.

#### 3 - Configuração da impressora:
    É importante que a impressora já esteja configurada para imprimir arquivos através Chrome.
    E que no momento de leitura do arquivo, a impressora esteja selecionada no "Destino".
    
    Exemplo abaixo:
![img.png](img.png)
