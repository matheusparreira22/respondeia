# RespondeIA

Um sistema para responder comentários de clientes sobre produtos utilizando a API do Gemini.

## Descrição

Este projeto utiliza a API do Gemini para gerar respostas personalizadas e empáticas para comentários de clientes sobre produtos. O sistema é desenvolvido em Python e pode ser facilmente integrado a plataformas de e-commerce ou sistemas de atendimento ao cliente.

## Requisitos

- Python 3.8+
- Chave de API do Gemini

## Instalação

1. Clone o repositório:
```
git clone <url-do-repositório>
cd respondeia
```

2. Crie um ambiente virtual e ative-o:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Configure a chave de API:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave de API: `GEMINI_API_KEY=sua-chave-aqui`

## Uso

Para iniciar o aplicativo:

```
python app.py
```

Para testar a conexão com a API:

```
python test_connection.py
```

## Estrutura do Projeto

```
respondeia/
├── .env                  # Arquivo de variáveis de ambiente
├── .gitignore            # Arquivos a serem ignorados pelo git
├── README.md             # Documentação do projeto
├── app.py                # Aplicativo principal
├── requirements.txt      # Dependências do projeto
├── test_connection.py    # Script para testar a conexão com a API
└── src/                  # Código fonte
    ├── __init__.py       # Inicialização do pacote
    ├── gemini_client.py  # Cliente para a API do Gemini
    └── comment_processor.py  # Processador de comentários
```

## Licença

[MIT](LICENSE)
