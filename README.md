# Streamlit Community Cloud URL Fetcher

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gh-to-st-url.streamlit.app/)

This repository contains a simple Streamlit app that takes the GitHub link to a `.py` Streamlit app and fetches its [Streamlit Community Cloud](https://streamlit.io/cloud) app URL if available. The app makes it easy for users to find and access Streamlit apps deployed on the Community Cloud.

## Features

- Accepts a GitHub URL for the main `.py` file of a Streamlit app
- Fetches the Community Cloud app URL if available
- Displays the Community Cloud app URL or an error message if the app does not exist

## Installation

To set up the app locally, follow these steps:

1. Clone the repository:

```sh
git clone https://github.com/snehankekre/github-to-app-url
```

2. Navigate to the cloned directory:

```sh
cd github-to-app-url
```

3. Install the dependencies:

```sh
pip install streamlit
```

4. Run the app:

```sh
streamlit run streamlit_app.py
```

## Usage

1. Open the app in your browser at `http://localhost:8501`
2. Enter the GitHub URL of the main `.py` module of your Streamlit app
3. Click the "Get URL" button or press `Enter`
4. The app will display the Community Cloud URL or an error message if the app does not exist
