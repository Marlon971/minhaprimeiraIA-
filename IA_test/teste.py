import os
import time
import glob
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# importações do google
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from google.api_core import exceptions






load_dotenv()

# n se esqueça de colocar sua key que vc pega no googleapi 
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERRO: Variável GOOGLE_API_KEY não encontrada no arquivo .env")
app = Flask(__name__)








#lembre-se de colocar gemini 2.5, outras versões estão atualizadas <-----------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.4  
)
print("Carregando modelo de embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")












textos_portfolio = [
    "O projeto Barbearia Chaves foi desenvolvido pelo Marlon utilizando Python e Flask. O sistema possui autenticação de usuários.",
    "O banco de dados utilizado no sistema foi MySQL. O sistema utiliza integração com SQLAlchemy.",
    "O front-end foi desenvolvido com HTML, CSS e JavaScript. O layout foi pensado para responsividade.",
    "O sistema utiliza Flask-Login para autenticação. As senhas são protegidas utilizando Werkzeug Security.",
    "Marlon possui conhecimentos em: Python, Flask, SQL, MySQL, HTML, CSS, JavaScript, Git e APIs REST."
]












pasta_documentos = os.path.join(os.path.dirname(__file__), 'documents')
arquivos_txt = glob.glob(os.path.join(pasta_documentos, "*.txt"))



if arquivos_txt:
    print(f"Encontrados {len(arquivos_txt)} arquivo(s) em /documents. Carregando dados...")
    for caminho_arquivo in arquivos_txt:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read().strip()
                if conteudo:
                    textos_portfolio.append(conteudo)
                    print(f"-> Arquivo carregado com sucesso: {os.path.basename(caminho_arquivo)}")
        except Exception as e:
            print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
else:
    print("Nenhum arquivo de texto extra encontrado na pasta /documents. Usando apenas dados padrão.")










print("Criando banco vetorial...")
vector_db = FAISS.from_texts(textos_portfolio, embeddings)
print("IA online com sucesso.")









def verificar_saudacao(mensagem):
    """
    Verifica se a mensagem do usuário é apenas um cumprimento simples.
    Retorna uma resposta amigável se for o caso, senão retorna None.
    """
    primeira_msg = mensagem.lower().strip().replace("?", "").replace("!", "")
    saudacoes = ["ola", "olá", "oi", "bom dia", "boa tarde", "boa noite", "eae", "opa", "tudo bem", "tudo bom", "baum?", "eae chef"]
    
    if primeira_msg in saudacoes:
        return (
            "Olá! Tudo ótimo por aqui, e com você?  "
            
            "tranquilo? oque você precisa?"
            
            "O que você gostaria de saber hoje?"
        )
    return None










@app.route('/')
def home():
    return render_template('index.html')











@app.route('/perguntar', methods=['POST'])
def perguntar():
    try:
        dados = request.get_json()
        pergunta_usuario = dados.get('pergunta', '')

        if not pergunta_usuario:
            return jsonify({'resposta': 'Diga algo!'}), 400

        
        busca = vector_db.similarity_search(pergunta_usuario, k=2)
        contexto = "\n".join([doc.page_content for doc in busca])

        
        prompt = f"""
        Você é uma inteligência artificial prestativa, informativa e amigável.
        
        INSTRUÇÕES:
        - Responda de forma direta e concisa (máximo 3 frases).
        - Use o CONTEXTO abaixo APENAS se ele for relevante para a pergunta.
        - Se a pergunta for sobre assuntos gerais, use seu próprio conhecimento.
        - Mantenha um tom de conversa normal e humano.

        CONTEXTO RELACIONADO:
        {contexto}

        PERGUNTA:
        {pergunta_usuario}
        """

        
        try:
            resposta = llm.invoke(prompt)
            return jsonify({'resposta': resposta.content})
        except exceptions.ResourceExhausted:
            return jsonify({'resposta': 'Cota esgotada. Tente em 1 minuto.'}), 429

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({'resposta': 'Erro interno.'}), 500
















if __name__ == '__main__':
    app.run(debug=True)