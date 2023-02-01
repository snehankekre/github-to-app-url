import requests

import streamlit as st


def get_new_url(main_app_github):
    path = main_app_github.replace("https://github.com/", "").replace("/blob", "")
    r = requests.get(f"https://share.streamlit.io/api/v1/disambiguate?path={path}")
    try:
        return "https://" + r.json()["host"]
    except:
        return "Error: " + r.text


gh_app = st.text_input("Github URL of main module")

if gh_app:
    st.write("New URL:", get_new_url(gh_app))
