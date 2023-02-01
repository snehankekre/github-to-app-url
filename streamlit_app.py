import requests

import streamlit as st


def get_share_url(main_app_github):
    share_url = "https://share.streamlit.io/"
    main_app_github = (
        main_app_github.replace("https://github.com/", "")
        .replace("/blob", "")
        .rstrip("/")
    )
    username, repo, branch, main_module = main_app_github.split("/")
    return f"{share_url}{username}/{repo}/main/{main_module}"


def get_new_url(main_app_github):
    path = main_app_github.replace("https://github.com/", "").replace("/blob", "")
    r = requests.get(f"https://share.streamlit.io/api/v1/disambiguate?path={path}")
    return "https://" + r.json()["host"]


gh_app = st.text_input("Github URL to main module")

if gh_app:
    share_url = get_share_url(gh_app)
    st.write("Legacy URL:", share_url)
    st.write("New URL:", get_new_url(gh_app))
