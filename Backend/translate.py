import speech_recognition as sr
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string
import threading
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Import required libraries
import speech_recognition as sr
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string
import threading
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Install required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the translator
translator = Translator()

# Define the language to translate to
dest_language = 'fr'  # Change this to your desired language code

# Define the sentiment analysis model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
model.eval()

# Define a function to preprocess text
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]

    # Stop word removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]

    # Removing special characters and punctuation
    filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

    return filtered_tokens

# Define a function to map sentiment scores to emotions
def map_sentiment_to_emotion(sentiment_score):
    # Define the threshold values for different emotions
    thresholds = {
        'sad': -0.8,
        'nervous': -0.6,
        'shy': -0.4,
        'happy': 0.4,
        'excited': 0.6,
        'neutral': 0.8,
        'desperate': -1.0,
        'crying': -0.2
    }

    # Map the sentiment score to an emotion based on the thresholds
    for emotion, threshold in thresholds.items():
        if sentiment_score <= threshold:
            return emotion

    return 'neutral'

# Define a function for real-time translation and sentiment analysis
def translate_and_analyze_audio():
    with sr.Microphone() as source:
        print("Press Enter to start recording...")
        input()
        print("Start recording...")

        audio = r.listen(source)

        print("Recording stopped.")
        print("Translating and analyzing...")

    try:
        # Use the Google Web Speech API for speech recognition
        text = r.recognize_google(audio)
        if text:
            print("Recognized Text:", text)

            # Translate the text
            translation = translator.translate(text, dest=dest_language)
            translated_text = translation.text
            print("Translated Text:", translated_text)

            # Preprocess the text for sentiment analysis
            preprocessed_text = preprocess_text(translated_text)
            preprocessed_text = ' '.join(preprocessed_text)

            # Perform sentiment analysis on text
            inputs = tokenizer.encode_plus(
                preprocessed_text,
                add_special_tokens=True,
                max_length=512,
                padding='max_length',
                return_tensors='pt'
            )
            input_ids = inputs['input_ids'].to(device)
            attention_mask = inputs['attention_mask'].to(device)

            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                predicted_class = torch.sigmoid(logits).squeeze().tolist()
                sentiment_text = predicted_class[0]
                emotion_text = map_sentiment_to_emotion(sentiment_text)
                print("Emotion (Text):", emotion_text)

            # Perform sentiment analysis on audio
            inputs = tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=512,
                padding='max_length',
                return_tensors='pt'
            )
            input_ids = inputs['input_ids'].to(device)
            attention_mask = inputs['attention_mask'].to(device)

            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                predicted_class = torch.sigmoid(logits).squeeze().tolist()
                sentiment_audio = predicted_class[0]
                emotion_audio = map_sentiment_to_emotion(sentiment_audio)
                print("Emotion (Audio):", emotion_audio)
        else:
            print("No speech detected.")

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service: {e}")

# Create and start a new thread for real-time translation and sentiment analysis
translation_analysis_thread = threading.Thread(target=translate_and_analyze_audio)
translation_analysis_thread.start()