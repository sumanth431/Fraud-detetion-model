import streamlit as st
import pandas as pd
import joblib
model= joblib.load('fraud_detection_pipeline.pkl')
st.title("Fraud Detection Model")
st.markdown("This app predicts whether a transaction is fraudulent or not.")
st.divider()

transaction_type=st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT","DEPOSIT"])
anount=st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg=st.number_input("Old Balance(sender)", min_value=0.0, value=5000.0)
newbalanceOrig=st.number_input("New Balance (sender)", min_value=0.0, value=9000.0)
oldbalanceDest=st.number_input("Old Balance (receiver)", min_value=0.0, value=2000.0)
newbalanceDest=st.number_input("New Balance (receiver)", min_value=0.0, value=3000.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': anount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    
    }])
    
    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction:'{int(prediction)}'")
    
    if prediction == 1:
        st.success("The transaction is fraudulent.")
    else:
        st.success("The transaction is not fraudulent.")