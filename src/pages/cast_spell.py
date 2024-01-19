import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps
from streamlit_drawable_canvas import st_canvas
import numpy as np
import time
import tensorflow as tf
from keras.models import load_model
import cv2


def load_digit_model():
    model = load_model("src/model/model.h5")
    return model


def show():
    # Page title
    st.set_page_config(page_title="Cast Your Spell !", layout="centered")

    # Hide the app page
    st.markdown(
        """
    <style>
    a[href$="/"] {display: none;}
    """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.title("📍 Here you can cast your spell! 🎩✨")

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
        canvas = st_canvas(width=225, height=350)
    with col3:
        st.title("📊Predicted Probabilities")
        progress_plot = st.empty()
        probabilities = [0 for _ in range(10)]
        progress_plot.bar_chart(probabilities, use_container_width=True, height=350)

    # Load the model
    model = load_digit_model()

    if st.button("Predict"):
        # Get the image from the canvas
        image = canvas.image_data
        # Convert the image from RGBA to grayscale using cv2
        image = 255 - image[:, :, 3]

        # Apply Gaussian blur
        image = cv2.GaussianBlur(image, (5, 5), 0)

        # Threshold the image to binary using Otsu's method
        _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the image
        contours, _ = cv2.findContours(
            image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # List to store all ROIs
        rois = []

        for contour in contours:
            [x, y, w, h] = cv2.boundingRect(contour)

            # Add padding around the bounding box coordinates
            padding = 29
            x = max(0, x - padding)
            y = max(0, y - padding)
            w = min(image.shape[1] - x, w + 2 * padding)
            h = min(image.shape[0] - y, h + 2 * padding)

            # Create rectangular region of interest with padding
            roi = image[y : y + h, x : x + w]

            roi = roi / 255.0
            # Resize ROI to 28x28
            roi = cv2.resize(roi, (28, 28))

            # Reshape the roi to the shape your model expects
            roi = np.reshape(roi, (1, 28, 28, 1))

            # Add the roi to the list
            rois.append(roi)

        # Make a prediction for each roi
        digit = 0
        digits_probs = []
        for roi in rois:
            st.image(roi)
            digits_probs = model.predict(roi)
            st.write(digits_probs)
            digit = np.argmax(digits_probs)

        # Position where the digit will be drawn
        text = str(digit)
        width, height = crystal_ball.size
        _, _, textwidth, textheight = draw.textbbox((0, 0), text, font=font)
        position = ((width - textwidth) / 2, (height - textheight) / 2)

        # Draw the digit on the crystal ball image
        draw.text(position, text, fill=color, font=font)

        for i in range(9):
            progress_plot.bar_chart(
                digits_probs[0],
                use_container_width=True,
            )
        time.sleep(0.2)  #

    # In the second column, display the crystal ball image
    with col2:
        st.title("Crystal Ball 🔮")
        st.image(crystal_ball, use_column_width=True)


show()
