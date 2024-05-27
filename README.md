
# Mental Healthcare Chatbot

This project implements a mental health care chatbot using machine learning models. The chatbot is designed to provide users with information about mental health issues and support. It leverages multiple machine learning classifiers and is deployed using Streamlit for a user-friendly interface.

## Features

- Advanced text preprocessing including tokenization and lemmatization.
- SVM classifier for predicting user intents.
- Streamlit-based interactive chatbot interface.
- Model prediction with real-time chat experience.

## Requirements

- Python 3.x
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- spacy
- nltk
- streamlit
- joblib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SabjitSingh/Mental_HealthCare_Chatbot.git
    cd Mental_HealthCare_Chatbot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```


3. Download the SpaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Train the model and save it (if not already saved).

## Usage

### Running the Chatbot

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. The chatbot interface will open in your web browser. Enter your inputs and interact with the chatbot.

### Live Demo

You can access the live demo of the chatbot [here](https://mentalhealthcarechatbot.streamlit.app/).

## Training the Model

To train the model, follow the steps below. The training script preprocesses the text, trains the SVM model, and saves the trained model using `joblib`.

1. Load your dataset containing intents, tags, patterns, and responses into a pandas DataFrame.
2. Preprocess the text data using the `advanced_preprocess_text` function.
3. Train the SVM classifier and save the model.

## Streamlit App

The Streamlit app (`app.py`) provides an interactive UI for users to chat with the mental health care chatbot. The chatbot uses the pre-trained SVM model to predict responses based on user input.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features, bugs, or suggestions.

## License

This project is licensed under the MIT License.