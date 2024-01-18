import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from streamlit_drawable_canvas import st_canvas


def show():
    # Page title
    st.set_page_config(page_title="Cast Your Spell !", layout="centered")

    with st.container():
        st.title("Here you can cast your spell!")

    # Load the crystal ball image
    crystal_ball = Image.open("static/images/digit_ball.jpg").resize((1000, 1250))

    # Create a draw object
    draw = ImageDraw.Draw(crystal_ball)

    # Specify the font, size, and color
    font = ImageFont.truetype("arial", size=500)
    color = "rgb(0, 0, 0)"  #  color

    # Create columns for the canvas and the prediction zone
    col1, col2 = st.columns(2, gap="large")

    # In the first column, create the canvas
    with col1:
        st.title("Cast Your Spell")
        canvas = st_canvas()

    # Below the canvas, create the 'Predict' button
    if st.button("Predict"):
        # Get the image from the canvas
        image = canvas.image_data

        # Preprocess the image and make a prediction
        # For simplicity, let's say the predicted digit is 7
        digit = 1

        # Position where the digit will be drawn
        text = str(digit)
        width, height = crystal_ball.size
        _, _, textwidth, textheight = draw.textbbox((0, 0), text, font=font)
        position = ((width - textwidth) / 2, (height - textheight) / 2)
        st.write(position)
        # Draw the digit on the crystal ball image
        draw.text(position, text, fill=color, font=font)

    # In the second column, display the crystal ball image
    with col2:
        st.title("Crystal Ball")
        st.image(crystal_ball, use_column_width=True)


show()
