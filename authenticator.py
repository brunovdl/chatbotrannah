import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils import app as app_module

with open('utils/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credencials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()

authentication_status = st.session_state.get('authentication_status')

if authentication_status == True:
    authenticator.logout()
    app_module.main()
elif authentication_status == False:
    st.error('Usuário/Senha inválido')
elif authentication_status is None:
    st.warning('Por favor, utilizar seu usuário e senha!')