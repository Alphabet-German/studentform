import streamlit as st
from deta import Deta

deta = Deta(st.secrets['data_key'])
# deta = Deta(DETA_KEY)

db = deta.Base('userformdb')

def insertUser(name, addr, course):
    return db.put({'name': name, 'addr': addr, 'course': course})
