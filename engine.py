import spacy
import numpy as np
from operator import itemgetter

# Load the SpaCy model for English language
nlp = spacy.load('en_core_web_md')


# Step 1: Data Entry
def get_input_text():
    """
    Function prompts the user to enter text and returns it.
    """
    text = input("Enter your text:\n")
    return text


# Step 2: Load Standard Phrases
def load_standard_phrases(filepath):
    """
    Function loads standard phrases from a file and returns a list of phrases.
    :param filepath: Path to the file containing the standard phrases.
    :return: List of standard phrases.
    """
    with open(filepath, 'r') as txt_file:
        standard_phrases = [line.strip() for line in txt_file]
    return standard_phrases


# Step 3: Analyze Text
def analyze_text(input_text, standard_phrases):
    """
    Function analyzes the input text and compares it with each standard phrase.
    Returns a list of sentences with their corresponding standard phrases and similarity scores.
    :param input_text: The input text to analyze.
    :param standard_phrases: List of standard phrases.
    :return: List of sentences with their standard phrases and similarity scores.
    """
    doc = nlp(input_text)
    sentences = []

    for token in doc:
        if not token.is_stop and token.is_alpha:
            for standard_phrase in standard_phrases:
                standard_phrase_vector = nlp(standard_phrase).vector
                similarity = token.vector @ standard_phrase_vector / (
                        np.linalg.norm(token.vector) * np.linalg.norm(standard_phrase_vector))
                sentences.append((token.text, standard_phrase, similarity))

    return sentences


# Step 4: Suggestions
def get_suggestions(sentences, N):
    """
    Analyzes the input text and compares it with each standard phrase.
    Returns a list of sentences with their corresponding standard phrases and similarity scores.
    :param input_text (str): The input text to analyze.
    :param standard_phrases: List of standard phrases.
    :return: List of sentences with their standard phrases and similarity scores.
    """
    sorted_sentences = sorted(sentences, key=itemgetter(2), reverse=True)
    top_N_sentences = sorted_sentences[:N]

    for sentence in top_N_sentences:
        print(f'Source phrase: "{sentence[0]}"')
        print(f'Standard phrase: "{sentence[1]}"')
        print(f'Similarity score: {sentence[2]}')


# Example:
input_text = get_input_text()
standard_phrases = load_standard_phrases('standard_phrases.txt')
print(standard_phrases)
sentences = analyze_text(input_text, standard_phrases)
get_suggestions(sentences, 10)
