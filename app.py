import streamlit as st

pageTitle = 'Alphabet German Academy Admission Form'
pageIcon = ':monkey_face:'
layout = 'centered'


st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=layout)
st.title(pageTitle + ' ' + pageIcon)


# st.header('')

with st.form('entryForm', clear_on_submit=True):
    # col0, col1 = st.columns(2)
    # col0.text('Name')
    st.text_input('Name', placeholder='Enter Name')
    # st.text('Address')
    st.text_input('Address', placeholder='Enter Address')
    # col0.text('Course')
    courses = ['8th', '9th', '10th', 'A1']
    st.selectbox('Course', courses)


    "---"

    submitted = st.form_submit_button('Save Form')

    if submitted:
        st.success('Data Saved')
