

from datetime import datetime
import json
from locale import currency
import os
from pathlib import Path
import sys
import pandas as pd
from PIL import Image
import requests
import streamlit as st


from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from constants import Constants

import db_client as dbc




def payments():
    st.header('Account Tracking')
    with st.form("Check paid Invoices", clear_on_submit=True):
        st.selectbox("Select Account Number", Constants.ACCOUNT_NUMBER, key='accNumber') # noqa
        st.text_input("Cntract ID", key="contractNum")
        st.date_input("Payment Date", key='Date')
        submitted = st.form_submit_button("Check Payment")
        if submitted:
            accNumber = st.session_state['accNumber']
            contractId = st.session_state['contractNum']
            all_invoice = dbc.fetch_all_invoice(accNumber, contractId)
            paid_invoice = dbc.fetch_all_payments(accNumber, contractId)
            df = dbc.process_df(contractId, all_invoice, paid_invoice)
            st.dataframe(pd.DataFrame(df))


    st.write("---")
    st.write("##")
    st.subheader('Here to make your payments promptly')
    st.write("##")
    st.write("---")



    st.subheader('For Offical Use Only')
    with st.form("Invoice Records", clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        col1.selectbox("Select an Invoice to Pay", dbc.get_invoivces(), key='InvoiceId') # noqa
        col1.selectbox("Select Account Number", Constants.ACCOUNT_NUMBER, key='accountNumber') # noqa
        col2.selectbox("Select Constractor ID", Constants.CONTRACTORS_ID, key='contractId') # noqa
        col2.date_input("Payment Date", key='date')
        col1.number_input("Enter Invoice Amount", key='Amount')
        submitted = st.form_submit_button("Pay Invoice")
        if submitted:
            payment_date = str(st.session_state['date'])
            contractId = st.session_state['contractId']
            InvoiceId = st.session_state['InvoiceId']
            accountNumber = st.session_state['accountNumber']
            Amount = st.session_state['Amount']
            dbc.pay_milestone(InvoiceId, contractId, accountNumber, Amount, payment_date)
            st.write("Invoice Paid")
    st.write("---")