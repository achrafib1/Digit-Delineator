import streamlit as st
import time
from utils.images_helper import set_image_as_page_bg, Container_bg
from pathlib import Path
import os


def show():
    # Page title
    st.set_page_config(page_title="Digit Delineator!", layout="centered")

    # Hide the app page
    st.markdown(
        """
    <style>
    a[href$="/"] {display: none;}

    </style>
    """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.title("🎉 Welcome to Digit Delineator! 🎉")

    # Introduction
    with st.container():
        st.header("📚 Introduction", divider="orange")
        page_bg_img = "static/images/_65798238-9ae6-4612-b254-8712ed42d675.jpg"
        page_bg = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
        background-color: rgba(0,0,0,0);
        }}
        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
        </style>
        """

        st.markdown(page_bg, unsafe_allow_html=True)
        # set_image_as_page_bg(page_bg_img)
        st.markdown(
            """
            <p style='color: black;'>
            🧙‍♂️ Welcome, wizard! Ready to cast some number spells? 🪄 <br/><br/>
            This app uses the power of machine learning 🧠💡 to recognize the digit you draw.
            Think of it as casting a spell, and the app will predict the result of your spell. 🎯
            </p>
        
        """,
            unsafe_allow_html=True,
        )
        st.image(page_bg_img)

    # Navigation
    with st.container():
        st.header("🎩 Begin the Magic")
        if st.button("Start", use_container_width=True):
            st.markdown(
                f"""<style>
                            [data-testid="stAppViewContainer"] > .main {{
                            background-color: rgba(0,0,0,0.2);
                            }}
                    </style>
                            """,
                unsafe_allow_html=True,
            )
            with st.spinner("Let's start our magical journey!"):
                # Simulate a delay
                time.sleep(2)
            st.markdown(
                f"""<style>
                            [data-testid="stAppViewContainer"] > .main {{
                            background-color: rgba(0,0,0,0);
                            }}
                    </style>
                            """,
                unsafe_allow_html=True,
            )
            st.switch_page("pages/cast_spell.py")

    # Footer
    with st.container():
        st.subheader("", divider="orange")
        st.write(
            """
        Made with ❤️ by name
        """
        )


show()
