# Digit-Delineator

## Description

Digit Delineator is an application that predicts handwritten digits. It uses a model trained on the MNIST dataset with TensorFlow and Keras, and the user interface is built with Streamlit.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/achrafib1/Digit-Delineator.git
```

2. Navigate to the project directory:

```bash
cd Digit-Delineator
```

3. (Recommended) Create a virtual environment:
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment:

   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source env/bin/activate
     ```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:

```bash
streamlit run src\app.py
```

Then, open your web browser and go to `http://localhost:8501` to view the app.
