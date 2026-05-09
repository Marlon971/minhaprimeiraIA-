## Instalação e Execução

### Pré-requisitos
*   **Python 3.9+**
*   **Google Gemini API Key** (Obtida via [Google AI Studio](https://aistudio.google.com/api-keys))

### Passo a passo

1.  **Clone o repositório:**
   terminal:
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
   

2.  **Instale as dependências:**
    terminal:
    pip install Flask python-dotenv langchain langchain-google-genai langchain-community langchain-huggingface faiss-cpu sentence-transformers google-api-core
    

3.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto e insira sua chave:
       env:
    GOOGLE_API_KEY=sua_chave_aqui
   

4.  **Inicie o servidor:**
    terminal:
    python app.py
    




### O que mudou e por quê?
1.  **Termo "RAG":** É a palavra da moda no mundo de IA. Recrutadores buscam desenvolvedores que entendam esse fluxo (Documento -> Vector DB -> LLM).
2.  **Busca Semântica:** Mostra que você não está apenas fazendo um "chat", mas lidando com processamento de linguagem natural (NLP).
3.  **Hugging Face:** Citar o uso de embeddings locais demonstra conhecimento sobre como a IA processa informações antes de enviar para o Gemini.
4.  **Escalabilidade:** Essa palavra brilha nos olhos de quem contrata, pois mostra que você pensaUm bom README funciona como o "cartão de visitas" do seu código. Para atrair recrutadores, o foco deve sair apenas das "ferramentas" e focar nas **soluções** e nos **conceitos de engenharia** (como RAG e Busca Semântica).

Aqui está uma versão otimizada, utilizando termos técnicos de alta relevância no mercado atual:



#  Gemini RAG Explorer: Busca Semântica & IA Generativa

Este projeto implementa uma arquitetura de **RAG (Retrieval-Augmented Generation)** de ponta a ponta. A aplicação utiliza **IA Generativa** para responder perguntas baseadas em contextos extraídos de documentos locais, garantindo respostas precisas, atualizadas e com baixo índice de alucinação.

##  Tecnologias e Conceitos Aplicados

*   **LLM & IA:** Integração com o modelo **Google Gemini** via LangChain.
*   **Orquestração de Dados:** Uso de **LangChain** para criação de chains e gerenciamento de memória.
*   **Vector Database:** Implementação de busca vetorial de alta performance com **FAISS**.
*   **Embeddings:** Transformação de texto em vetores utilizando **Hugging Face Embeddings** (sentence-transformers).
*   **Back-end:** API robusta e leve desenvolvida em **Python** e **Flask**.
*   **Arquitetura de Dados:** Leitura automatizada e processamento de arquivos `.txt` para ingestão em base de dados vetorial.

##  Diferenciais do Projeto

*   **Busca Semântica:** Diferente de uma busca por palavras-chave comum, o sistema entende o **contexto** e a intenção por trás da pergunta do usuário.
*   **Privacidade e Segurança:** Implementação de variáveis de ambiente (`.env`) para proteção de credenciais sensíveis e chaves de API.
*   **Interface Amigável:** Front-end responsivo integrado para uma experiência de usuário (UX) fluida.
*   **Escalabilidade:** Estrutura modular preparada para a adição de novos conectores de dados ou modelos de linguagem.



##  Estrutura do Projeto

seu-projeto/
│
├── app.py                # Core da aplicação e rotas Flask
├── .env                  # Variáveis de ambiente (Chaves de API)
├── requirements.txt      # Gerenciamento de dependências
├── documents/            # Knowledge Base (Base de conhecimento local)
│   └── *.txt
├── templates/            # Interface Web (HTML/CSS)
    └── index.html
