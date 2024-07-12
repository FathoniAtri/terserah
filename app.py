import streamlit as st

st.title('KIMIA ORGANIK' )
st.subheader('', divider='rainbow')
st.write('helllooo :sunglasses:')
st.write('KIMOR COK :smile:')
st.write('f9:snake:')
import time
import numpy as np
import pandas as pd
import streamlit as st

_pencet = 'gapapa sih pencet aja, ga bakal kenapa napa'


def stream_data():
    for word in _pencet.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("Jangan dipencet"):
    st.write_stream(stream_data)

number = st.number_input("masukin bng")
kali = st.number_input("kali berapa bng?")
hasil_kali = number * kali
st.write(f"Hasil perkalian {number} dengan {kali} adalah: {hasil_kali}")
if hasil_kali % 2 == 0:
    st.write(f"{hasil_kali} bilangan genap itu cuy")
else:
    st.write(f"{hasil_kali} ganjit itu mah")