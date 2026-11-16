# AI Study & Work Assistant

Assistente conversacional construído com Python e Streamlit, com integração opcional a um modelo de linguagem via API.

## Funcionalidades

- Interface de chat.
- Histórico de mensagens durante a sessão.
- Instrução de sistema para respostas em português e foco em explicações claras.
- Configuração do modelo por variável de ambiente.
- Tratamento básico de erros.
- Modo de demonstração quando não há chave de API configurada.

## Tecnologias

- Python
- Streamlit
- OpenAI Python SDK
- python-dotenv

## Como executar localmente

1. Instale Python 3.10 ou superior.
2. Clone o repositório e entre na pasta do projeto.
3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Copie `.env.example` para `.env` e configure sua chave de API:

   ```env
   OPENAI_API_KEY=sua_chave
   OPENAI_MODEL=gpt-4o-mini
   ```

6. Inicie a aplicação:

   ```bash
   streamlit run app.py
   ```

Sem uma chave, a interface abre em modo de demonstração. Para respostas reais, é necessário ter acesso válido à API, configurar a chave e observar os custos do provedor.

## Segurança

- Nunca publique sua chave de API.
- O arquivo `.env` está listado no `.gitignore`.
- Não envie dados pessoais, confidenciais ou corporativos para serviços externos.

## Próximas melhorias

- Persistência de conversas em banco de dados.
- Autenticação de usuários.
- Testes automatizados.
- Exportação do histórico.
- Seleção de perfis de assistente.

## Sobre

Projeto de portfólio para demonstrar fundamentos de Python, integração com API, interface web, gerenciamento de estado e tratamento de erros.
