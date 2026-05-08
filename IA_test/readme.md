Este projeto é uma aplicação web desenvolvida com **Python**, **Flask** e **LangChain**, integrada com a API do **Google Gemini**.
Ela utiliza **FAISS** para busca vetorial e melhora as respostas com base em um contexto carregado de textos locais.




- Interface web com Flask
- Integração com o modelo Gemini
- Busca semântica com FAISS
- Leitura automática de arquivos `.txt` da pasta `documents`
- Uso de `.env` para proteger a chave da API
- Respostas amigáveis e contextuais



- Python
- Flask
- LangChain
- Gemini API
- FAISS
- Hugging Face Embeddings
- HTML, CSS e JavaScript



Antes de rodar o projeto, você precisa ter instalado:



- Python 3.9 ou superior
- pip
- Uma chave válida da API do Google Gemini

para começar, no terminal, coloque isso aqui ->
pip install Flask python-dotenv langchain langchain-google-genai langchain-community langchain-huggingface faiss-cpu sentence-transformers google-api-core


seu-projeto/
│
├── app.py
├── .env
├── requirements.txt
├── documents/
│   └── arquivos_txt.txt
├── templates/
    └── index.html



crie um arquivo ".env" e ensira sua chave do google que vc consegue
pelo https://aistudio.google.com/api-keys?project=gen-lang-client-0089037999
GOOGLE_API_KEY=sua_chave_aqui