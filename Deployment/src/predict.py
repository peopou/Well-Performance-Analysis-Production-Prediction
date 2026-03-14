import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np
import joblib

load_f12 = joblib.load("D:\Hacktive8\milestone\p1-ftds033-hck-m2-peopou\Model\Modeling_F-12") 

def run():
    # Membuat form 
    with st.form('Data Ajuan'):
        BORE_WI_VOL = st.number_input('Jumlah injeksi air:', value=0)
        BORE_WAT_VOL = st.number_input('Jumlah air terproduksi', min_value=0, value=0)
        BORE_GAS_VOL = st.number_input("Jumlah Gas terproduksi", min_value=0, value=0)
        ON_STREAM_HRS = st.number_input('Waktu Oprasional Sumur:', min_value=0, max_value=24, value=24)
        AVG_DOWNHOLE_PRESSURE = st.number_input('BHP:', min_value=0, value=0)
        AVG_DOWNHOLE_TEMPERATURE = st.number_input('BHT', min_value=0, value=0)
        AVG_DP_TUBING = st.number_input('DP_Tubing', min_value=0, value=0)
        AVG_ANNULUS_PRESS = st.number_input('tekanan pada anulus', min_value=0, value=0)
        AVG_WHT_P = st.number_input('WHT_P', min_value=0, value=20)
        DP_CHOKE_SIZE = st.number_input('DP saat melewati Choke', min_value=0, value=0)
        AVG_CHOKE_SIZE = st.number_input('Bukaan Choke', min_value=0, value=0)
        AVG_WHP_P = st.number_input('WHP_P', min_value=0, value=0)
        predict = st.form_submit_button('Predict')

    # Only predict when the form is submitted
    if predict:
        # Create a DataFrame with the input data
        data_inf = pd.DataFrame({
            'BORE_WI_VOL': [BORE_WI_VOL],
            'BORE_WAT_VOL': [BORE_WAT_VOL],
            'BORE_GAS_VOL': [BORE_GAS_VOL],
            'ON_STREAM_HRS': [ON_STREAM_HRS], 
            'AVG_DOWNHOLE_PRESSURE': [AVG_DOWNHOLE_PRESSURE],
            'AVG_DOWNHOLE_TEMPERATURE': [AVG_DOWNHOLE_TEMPERATURE],
            'AVG_DP_TUBING': [AVG_DP_TUBING],
            'AVG_ANNULUS_PRESS': [AVG_ANNULUS_PRESS],
            'AVG_WHT_P': [AVG_WHT_P],
            'DP_CHOKE_SIZE': [DP_CHOKE_SIZE],
            'AVG_CHOKE_SIZE': [AVG_CHOKE_SIZE],
            'AVG_WHP_P': [AVG_WHP_P]
        })
        
        # Make prediction
        predictions = load_f12.predict(data_inf)
        
        # Display the prediction
        st.success(f"Oil Production Prediction: {predictions[0]:.2f} MSTB")

if __name__ == '__main__':
    run()