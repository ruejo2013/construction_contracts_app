
import json
# from locale import currency
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


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load lottie construction file 

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def contract_milestones():
    lottie_png = load_lottieurl(Constants.LOTTIE_CONSTRUCTION)
    lottie_construction = load_lottiefile(Constants.LOTTIE_FILE)
        
    with st.container():
        st.write("---")
        st.header("Upload Your Invoice")
        st.subheader(f"Currency should be defined in {Constants.CURRENCY_}")
        col1, col2, right_column = st.columns([1,1,2])

        with st.form("entry_form", clear_on_submit=True):
            col1.selectbox("Select Constractor ID", Constants.CONTRACTORS_ID, key='contractId') # noqa
            col2.text_input("Invoice Number", key="InvoiceId")
            col2.number_input("Invoice Amount", key="Amount")
            col1.selectbox("Select Milestone:", Constants.MILESTONES, key="milestone") # noqa
            col1.date_input("Pick a date", key='date')
            uploaded_files = col2.file_uploader(
                'Upload Your invoice', key="invoice",
                accept_multiple_files=True
                )
            submitted = st.form_submit_button("Enter")
            if submitted:
                period_date = str(st.session_state['date'])
                contractId = st.session_state['contractId']
                InvoiceId = st.session_state['InvoiceId']
                Amount = st.session_state['Amount']
                milestone = st.session_state['milestone']
                # ------ Insert invoice details -------
                dbc.insert_milestone(contractId, InvoiceId, Amount, milestone, period_date)
                # -------- upload invoice ----------
                for uploaded_file in uploaded_files:
                    st.write("File Uploaded:", uploaded_file.name)
                    # dbc.upload_invoice(uploaded_file.name)
                st.write(f"Your invoice number {InvoiceId} has been recieved")
                st.success("Contract Updated")
                st.write("For quick payment")
                st.write("Please send a follow up Email below")
                

        with right_column:
            st.title("We make construction process painless")
            st_lottie(
                lottie_construction, speed=1.2,
                reverse=False, loop=True,height=640, 
                width=860, quality="high", key='New Construction'
                )

        "---"
        

    with st.container():
        st.write("---")
        # st.header("208 W 24th AVE Project, NEW YORK")
        # st.write("##")
        image_column, word_column, text_column = st.columns([1, 0.75, 1])
        with image_column:
            st.subheader("208 W 24th AVE Project, NEW YORK")
            st.image(Constants.IMG_CONSTRUCTION, caption='Ongoing Contruction Project in NYC', width=620)
        with word_column:
            st.markdown("---")
            st.markdown("##")
            # st.markdown(get_file_content_as_string("whatwedo.md"))
            st.markdown(
                Constants.WHO_WE_ARE, unsafe_allow_html=True
                )
            st.write("---")
        with text_column:
            st.subheader("The Abdulaha Shopping Complex, Doha")
            st.image(Constants.IMG_COMPLEX, caption='Delivery on Time', width=720)
            # , width=720

    with st.container():
        st.write("---")
        st.header("Upload project milestone Invoice")
        st.write("##")

        left_column, middle_column, right_column = st.columns([1,0.75, 1])
        with left_column:
            st.markdown(Constants.INVOICE_FORM, unsafe_allow_html=True)
                    
        with right_column:
            st_lottie(lottie_png, height=400,key='Under Construction')

