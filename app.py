import streamlit as st

pageTitle = 'Alphabet Admission Form'
pageIcon = ':monkey_face:'
layout = 'centered'


st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=layout)
st.title(pageTitle + ' ' + pageIcon)


# st.header('')

with st.form('entryForm', clear_on_submit=True):
    col0, col1 = st.columns(2)
    col0.text('Name')
    col1.text_input('', placeholder='Enter Name', label_visibility='collapsed')
    col0.text('Address')
    col1.text_input('', placeholder='Enter Address', label_visibility='collapsed')
    col0.text('Course')
    courses = ['8th', '9th', '10th', 'A1']
    col1.selectbox('', courses, label_visibility='collapsed')


    "---"

    submitted = st.form_submit_button('Save Form')

    if submitted:
        st.success('Data Saved')
