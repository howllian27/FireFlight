from transformers import AutoTokenizer, AutoModel
import torch
from nltk import ngrams
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string
import nltk
import re

nltk.download('punkt')
nltk.download('wordnet')

# Load the BERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to preprocess the text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    tokens = word_tokenize(text)
    # Stem and lemmatize the tokens
    tokens = [stemmer.stem(token) for token in tokens]
    tokens = [lemmatizer.lemmatize(token, pos=wordnet.VERB) for token in tokens]
    # Join the tokens back into a single string
    text = ' '.join(tokens)
    return text

def jaccard_similarity(user1, user2, n=2):
    user1_ngrams = set(ngrams(re.findall(r'\b\w+\b', user1), n))
    user2_ngrams = set(ngrams(re.findall(r'\b\w+\b', user2), n))
    intersection = user1_ngrams.intersection(user2_ngrams)
    union = user1_ngrams.union(user2_ngrams)
    return len(intersection) / len(union)

def levenshtein_distance(user1, user2):
    if len(user1) < len(user2):
        return levenshtein_distance(user2, user1)
    if len(user2) == 0:
        return len(user1)
    previous_row = range(len(user2) + 1)
    for i, c1 in enumerate(user1):
        current_row = [i + 1]
        for j, c2 in enumerate(user2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def normalize_score(score, max_score):
    return score / max_score

# Function to compute the BERT embeddings for a sentence
def get_bert_embeddings(sentence):
    inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

# Function to compute the cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    return torch.nn.functional.cosine_similarity(vec1, vec2).item()

# Compute the BERT embeddings for two sentences
sentence1 = preprocess_text("I love to play football.")
sentence2 = preprocess_text("Soccer is my favorite sport.")
embeddings1 = get_bert_embeddings(sentence1)
embeddings2 = get_bert_embeddings(sentence2)

# Compute the cosine similarity between the two sets of embeddings
bert_similarity = cosine_similarity(embeddings1, embeddings2)

# Compute other similarity scores
jaccard_similarity = jaccard_similarity(sentence1, sentence2)
levenshtein_similarity = 1 - normalize_score(levenshtein_distance(sentence1, sentence2), max(len(sentence1), len(sentence2)))

# Define the weights for the different scores
# The weights are chosen based on the assumption that BERT similarity is the most important, followed by Jaccard similarity, and then Levenshtein similarity.
# BERT similarity is given the highest weight because it takes into account the semantic meaning of the words in the sentences.
# Jaccard similarity is given the second highest weight because it considers the overlap of words in the sentences.
# Levenshtein similarity is given the lowest weight because it is a simple measure of the difference between the two sentences, without considering the meaning of the words.
bert_weight = 0.7
jaccard_weight = 0.2
levenshtein_weight = 0.1

# Compute the weighted average of the scores
average_score = (bert_weight * bert_similarity + jaccard_weight * jaccard_similarity + levenshtein_weight * levenshtein_similarity)

print(f"The similarity between the two sentences is {average_score}.")
