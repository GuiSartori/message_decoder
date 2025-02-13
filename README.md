# Message Decoder (Bot Games - Automation Anywhere)

Este projeto automatiza o processo de tradução de mensagens usando Selenium para interagir com o navegador e realizar traduções de texto.

## Descrição do Código

O script principal (`main.py`) faz o seguinte:
- Inicializa o Selenium WebDriver e abre a página do desafio.
- Realiza o login na comunidade Automation Anywhere utilizando credenciais armazenadas no arquivo `.env`.
- Captura o texto em búlgaro a ser traduzido.
- Abre uma nova aba com o tradutor de búlgaro para inglês.
- Insere o texto em búlgaro no campo de entrada do tradutor.
- Captura o texto traduzido para o inglês.
- Retorna à aba do Message Decoder e insere o texto traduzido no campo de entrada.
- Clica no botão de envio e captura os resultados da execução.

## Requisitos

- Python 3.x
- Selenium
- python-dotenv
- Pandas

## Estrutura do Projeto

```
OnlineGroceryOrderingAutomation/
├── logs/
├── src/
│   ├── utils/
│   │   ├── aa_login.py
│   │   ├── custom_log.py
│   │   └── msedgedriver.exe
│   └── main.py
├── .env
├── .gitignore
└── README.md
```
