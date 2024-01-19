from pages import home
import streamlit as st

home.show()
st.markdown(
    """
    <style>
    a[href$="/"] {display: none;}

        a[href*="/home"]{
            display: none;
        }
        a[href*="/cast_spell"]{
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
