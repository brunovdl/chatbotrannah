import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()
from streamlit_chat import message 
from utils import chatbot, text

st.set_page_config(page_title='Rannah 2.0 Generative AI', page_icon=':speech_balloon:')

def main():
    st.header(f'Olá, *{st.session_state["name"]}*')
    user_question = st.text_input('Faça uma pergunta para mim!')

    if('conversation' not in st.session_state):
        st.session_state.conversation = None

    if(user_question):
        response = st.session_state.conversation(user_question)['chat_history']

        for i, response_text in enumerate(response):
            
            if(i % 2 == 0):
                message(response_text.content, is_user=True, key=str(i) + 'user')
            else:    
                message(response_text.content, is_user=False, key=str(i) + '_bot')
    
    with st.sidebar:
        
        st.title('Base de conhecimento')
        pdf_docs = st.file_uploader("Carregue seus arquivos", accept_multiple_files=True)

        if st.button('Processar'):
            all_files_text = text.process_files(pdf_docs)

            chunks = text.creat_text_chunks(all_files_text)

            vectorstore = chatbot.creat_vectorstore(chunks)

            st.session_state.conversation = chatbot.creat_conversation_chain(vectorstore)
        
        st.write('***')
        st.header('Como utilizar')
        st.text('''
. Clique no botão *Brownse File* e 
faça upload do seu arquivo.
(É permitido fazer upload de vários
arquivos.) obs: apenas .pdf
. Após os arquivos carregados clique 
em *Processar*, aguarde a conclusão
. Agora é só fazer perguntas para o
chat que ele irá te responder com 
base nos arquivos que você forneceu.
                ''')

if __name__=='__main__':
    
    main()