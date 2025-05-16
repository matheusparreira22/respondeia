# RespondeIA 🚀

<div align="center">
  <img src="https://play-lh.googleusercontent.com/yDjaHCaOn_O89vnY7eOKH6ElEBtJrmN2CSI4yhiP1_GVC2zrxXWSFGxO0lt9-CU0mV4" alt="Alura Logo" width="150"/>
  <img src="https://logosmarcas.net/wp-content/uploads/2020/09/Google-Emblema.png" alt="Google Logo" width="200"/>
</div>

Um sistema revolucionário para responder comentários de clientes sobre produtos de materiais de construção utilizando a poderosa API do Gemini!

## 🌟 Descrição

Este projeto incrível utiliza a API do Gemini para gerar respostas personalizadas, empáticas e precisas para comentários de clientes sobre produtos de materiais de construção. O sistema é desenvolvido em Python e conta com uma interface web moderna e intuitiva que permite aos usuários:

- Navegar por um catálogo de produtos de materiais de construção
- Visualizar informações detalhadas sobre cada produto
- Fazer perguntas específicas sobre os produtos
- Receber respostas instantâneas geradas por IA

A magia acontece quando os clientes fazem perguntas! O sistema analisa inteligentemente o tipo de pergunta e:
- Para dúvidas sobre características, aplicações e uso dos produtos: gera respostas detalhadas e técnicas usando a API Gemini
- Para questões sobre estoque, prazos de entrega e logística: fornece respostas padronizadas informando que a equipe de vendas entrará em contato

## 🌐 Interface Web

Nossa nova interface web torna a experiência ainda mais incrível! Agora os usuários podem:

- Explorar produtos em uma interface visual atraente
- Clicar em produtos para ver detalhes completos
- Fazer perguntas diretamente na página do produto
- Ver as respostas aparecerem instantaneamente
- Acompanhar o histórico de perguntas e respostas

A interface é totalmente responsiva e oferece uma experiência de usuário excepcional em qualquer dispositivo!

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

## 🚀 Uso

### Interface de Linha de Comando

Para iniciar o aplicativo em modo console:

```
python app.py
```

Para testar a conexão com a API:

```
python test_connection.py
```

### 🌟 Interface Web

Para iniciar a incrível interface web:

```
python web_app.py
```

Depois, basta abrir seu navegador em `http://127.0.0.1:5000` e começar a explorar os produtos e fazer perguntas!

<div align="center">
  <img src="https://play-lh.googleusercontent.com/yDjaHCaOn_O89vnY7eOKH6ElEBtJrmN2CSI4yhiP1_GVC2zrxXWSFGxO0lt9-CU0mV4" alt="Alura Logo" width="80"/>
  <h3>Experimente agora e surpreenda-se com o poder da IA!</h3>
</div>

## 📁 Estrutura do Projeto

```
respondeia/
├── .env                  # Arquivo de variáveis de ambiente
├── .gitignore            # Arquivos a serem ignorados pelo git
├── README.md             # Documentação do projeto
├── app.py                # Aplicativo de linha de comando
├── web_app.py            # 🌟 Aplicativo web com Flask
├── requirements.txt      # Dependências do projeto
├── test_connection.py    # Script para testar a conexão com a API
├── templates/            # 🌟 Templates HTML para a interface web
│   ├── base.html         # Template base com layout comum
│   ├── index.html        # Página inicial com lista de produtos
│   └── product_detail.html # Página de detalhes do produto
├── static/               # 🌟 Arquivos estáticos para a interface web
│   ├── css/              # Estilos CSS
│   │   └── style.css     # Estilos principais
│   ├── js/               # Scripts JavaScript
│   │   └── script.js     # Funcionalidades interativas
│   └── img/              # Imagens
│       └── placeholder.svg # Imagem placeholder para produtos
└── src/                  # Código fonte principal
    ├── __init__.py       # Inicialização do pacote
    ├── gemini_client.py  # Cliente para a API do Gemini
    ├── message_handler.py # Processador de mensagens dos clientes
    └── db/               # Módulos de banco de dados
        ├── __init__.py   # Inicialização do pacote de banco de dados
        ├── product_db.py # Gerenciador do banco de dados de produtos
        └── products.json # Banco de dados de produtos em JSON
```

<div align="center">
  <img src="https://logosmarcas.net/wp-content/uploads/2020/09/Google-Emblema.png" alt="Google Logo" width="120"/>
  <h4>Potencializado pela API Gemini do Google</h4>
</div>

## 🛠️ Tecnologias Utilizadas

Este projeto combina tecnologias de ponta para oferecer uma experiência excepcional:

- **Python**: Linguagem base do projeto, escolhida por sua versatilidade e facilidade de uso
- **API Gemini**: Motor de IA avançado do Google para geração de respostas inteligentes
- **Flask**: Framework web leve e poderoso para a interface de usuário
- **HTML/CSS/JavaScript**: Para uma interface web moderna e responsiva
- **JSON**: Armazenamento de dados de produtos em formato leve e flexível

## 🚀 Próximos Passos

Estamos constantemente melhorando o RespondeIA! Alguns recursos planejados:

- Integração com bancos de dados reais
- Sistema de autenticação de usuários
- Painel administrativo para gerenciar produtos
- Análise de sentimento nos comentários dos clientes
- Suporte a múltiplos idiomas

## 📝 Licença

[MIT](LICENSE)

---

<div align="center">
  <p>Desenvolvido com ❤️ como parte dos projetos da Alura</p>
  <img src="https://play-lh.googleusercontent.com/yDjaHCaOn_O89vnY7eOKH6ElEBtJrmN2CSI4yhiP1_GVC2zrxXWSFGxO0lt9-CU0mV4" alt="Alura Logo" width="60"/>
</div>
