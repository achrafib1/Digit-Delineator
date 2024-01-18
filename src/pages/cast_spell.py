import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from streamlit_drawable_canvas import st_canvas
import numpy as np
import time


def show():
    # Page title
    st.set_page_config(page_title="Cast Your Spell !", layout="centered")

    with st.container():
        st.title("Here you can cast your spell!")

    # Load the crystal ball image
    crystal_ball = Image.open("static/images/digit_ball.jpg").resize((1000, 1850))

    # Create a draw object
    draw = ImageDraw.Draw(crystal_ball)

    # Specify the font, size, and color
    font = ImageFont.truetype("arial", size=500)
    color = "rgb(0, 0, 0)"  #  color

    # Create columns for the canvas and the prediction zone
    col1, col2, col3 = st.columns(3, gap="large")

    # In the first column, create the canvas
    with col1:
        st.title("Cast Your Spell")
        canvas = st_canvas(height=350)
    with col3:
        st.title("Predicted Probabilities")
        progress_plot = st.empty()
        probabilities = [0 for _ in range(10)]
        progress_plot.bar_chart(probabilities, use_container_width=True, height=350)

    if st.button("Predict"):
        # Get the image from the canvas
        image = canvas.image_data

        # Preprocess the image and make a prediction
        digit = 1

        # Position where the digit will be drawn
        text = str(digit)
        width, height = crystal_ball.size
        _, _, textwidth, textheight = draw.textbbox((0, 0), text, font=font)
        position = ((width - textwidth) / 2, (height - textheight) / 2)
        st.write(position)

        # Draw the digit on the crystal ball image
        draw.text(position, text, fill=color, font=font)

        probabilities = np.random.rand(10)
        for i in range(9):  # 8 steps of 12.5% each
            progress_plot.bar_chart(
                [min((i) / 8, 1) * probabilities[j] for j in range(10)],
                use_container_width=True,
            )
        time.sleep(0.2)  #

    # In the second column, display the crystal ball image
    with col2:
        st.title("Crystal Ball")
        st.image(crystal_ball, use_column_width=True)


show()
