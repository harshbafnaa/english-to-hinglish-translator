import streamlit as st
from translate import Translator
import json

# Load the translation dictionary from JSON file
with open("hinglish_to_english.json", "r", encoding="utf-8") as file:
    hinglish_to_english = json.load(file)

# Function to translate English text to Hindi
def translate_to_hindi(text):
    translator = Translator(to_lang="hi")
    translation = translator.translate(text)
    return translation

# Function to replace Hinglish words with English words
def replace_hinglish_with_english(text):
    words = text.split()
    for i in range(len(words)):
        if words[i] in hinglish_to_english:
            words[i] = hinglish_to_english[words[i]]
    return ' '.join(words)

# Streamlit app
st.title("English to Hinglish Translator")

# User input for multiple sentences
user_input = st.text_area("Enter multiple sentences in English (one per line):", "")

if user_input:
    # Split input into sentences
    sentences = user_input.split('\n')
    
    translated_sentences = []
    for sentence in sentences:
        # Translate to Hindi
        translated_text = translate_to_hindi(sentence)
        
        # Replace Hinglish words with English words
        final_output = replace_hinglish_with_english(translated_text)
        
        # Append the translated and replaced sentence to the list
        translated_sentences.append(final_output)
    
    # Display translated and replaced sentences
    st.subheader("Translated and Replaced Sentences in Hindi:")
    for i, sentence in enumerate(translated_sentences):
        st.write(f"{i + 1}. {sentence}")