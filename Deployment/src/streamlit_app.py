import streamlit as st
import eda, predict

with st.sidebar:
    st.title('Page Navigation')
    page = st.selectbox('Pilih Halaman',
                        ['eda', 'predict'])
    
if page == 'eda':
    eda.run()
else:
    predict.run()