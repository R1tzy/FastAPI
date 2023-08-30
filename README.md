# FastAPI Projects - Exemplos de Criação de APIs

Bem-vindo ao repositório "FastAPI Projects"! Aqui você encontrará exemplos práticos de criação de APIs utilizando o poderoso framework FastAPI. O FastAPI é uma ferramenta conhecida por sua alta performance e simplicidade no desenvolvimento de APIs web em Python.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python (versão X.X.X)
- pip (gerenciador de pacotes do Python)

## Instalação e Uso

1. **Clone este repositório:** Para começar, clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/seu-usuario/fastapi-api.git
   ```

2. **Navegue para o diretório do projeto:** Entre na pasta do projeto clonado:

   ```bash
   cd fastapi-api
   ```

3. **Crie e ative um ambiente virtual (opcional, mas recomendado):** É recomendado utilizar um ambiente virtual para isolar as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. **Instale as dependências:** Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação FastAPI:** Inicie o servidor de desenvolvimento:

   ```bash
   uvicorn main:app --reload
   ```

6. **Acesse a API:** No navegador, acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) ou utilize ferramentas como [Swagger UI](http://127.0.0.1:8000/docs) ou [ReDoc](http://127.0.0.1:8000/redoc) para visualizar e testar as rotas disponíveis.

## Estrutura do Projeto

- `main.py`: Arquivo principal contendo a configuração da aplicação FastAPI e as rotas da API.
- `requirements.txt`: Lista de dependências do projeto.

## Contribuição

Contribuições são bem-vindas! Se você tiver melhorias, correções de bugs ou novas funcionalidades para adicionar, abra um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE), permitindo que você use e modifique o projeto de acordo com suas necessidades.

---

Sinta-se à vontade para explorar, aprender e experimentar com esses exemplos de criação de APIs usando o FastAPI!