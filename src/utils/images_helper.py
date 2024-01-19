import streamlit as st
import base64


def set_image_as_page_bg(main_bg):
    """
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    """
    # set bg name
    main_bg_ext = "jpg"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


def Container_bg(container_bg, container_id):
    container_bg_ext = "jpg"

    st.markdown(
        f"""
      <style>
      [data-testid={container_id}] > div:first-child {{
          background: url(data:image/{container_bg_ext};base64,{base64.b64encode(open(container_bg, "rb").read()).decode()});
          background-size: cover
      }}
      </style>
      """,
        unsafe_allow_html=True,
    )
