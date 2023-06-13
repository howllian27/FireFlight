from transformers import AutoTokenizer, AutoModel
import torch
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string
import nltk
import re
import os

# Set the NLTK data path relative to the current script location
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

# Check if NLTK data is already downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Load the BERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Global variables for BERT model and tokenizer
bert_tokenizer = None
bert_model = None

def load_bert_model():
    global bert_tokenizer, bert_model
    if bert_tokenizer is None or bert_model is None:
        # Load the BERT tokenizer and model
        bert_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        bert_model = AutoModel.from_pretrained('bert-base-uncased')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(token) for token in tokens]
    tokens = [lemmatizer.lemmatize(token, pos=wordnet.VERB) for token in tokens]
    text = ' '.join(tokens)
    return text

# bio_comparison.py functionalities converted into a class
class BioComparison:
    def __init__(self):
        load_bert_model()
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def get_bert_embeddings(self, sentence):
        inputs = bert_tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = bert_model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings

    def cosine_similarity(self, vec1, vec2):
        return torch.nn.functional.cosine_similarity(vec1, vec2).item()

    def compare_sentences(self, sentence1, sentence2):
        sentence1 = preprocess_text(sentence1)
        sentence2 = preprocess_text(sentence2)
        embeddings1 = self.get_bert_embeddings(sentence1)
        embeddings2 = self.get_bert_embeddings(sentence2)
        bert_similarity = self.cosine_similarity(embeddings1, embeddings2)
        return bert_similarity

# sentence1, sentence2 = "Soccer is my favourite sport", "I love soccer"
# bio_comparison = BioComparison()
# print(bio_comparison.compare_sentences(sentence1, sentence2))