import json
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
import contract_milestones
import db_client as dbc
import payments


st.set_page_config(page_title= Constants.PAGE_TITLE, layout= "wide")


# -- INPUT and Save Form ------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.title(Constants.PAGE_TITLE + " "+ Constants.PAGE_ICON)
st.subheader("A risk free way of executing construction contracts")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load lottie construction file 

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---- Page Settings -----------


selected = option_menu(
    menu_title = None,
    options=['Contract Milestones', 'Transaction History'],
    icons=['pencil-fill', 'bar-chart-fill'],
    orientation='horizontal'
    )


def main():
    if selected == 'Contract Milestones': 
        contract_milestones.contract_milestones()
    else:
        payments.payments()


if __name__ == '__main__':
    main()
