import streamlit as st
import pandas as pd
import re
from collections import Counter

# Streamlit app
st.title("Speech Word Counter")

# User input text box
user_input = st.text_area("Paste your text here")

# Add a submit button
if st.button("Submit for processing"):
    if user_input:
        # Preprocess the input text (remove punctuation, numbers, convert to lowercase)
        processed_text = re.sub(r'[^\w\s]|[\d]', '', user_input).lower()

        # Tokenize the input text into words
        tokenized_words = processed_text.split()

        # Count the frequency of words in the input text
        word_counts = Counter(tokenized_words)

        # Convert counts to a DataFrame
        speech_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count']).reset_index()
        speech_df.columns = ['Word', 'Count']

        # Display the DataFrame
        st.write(speech_df)

        # Convert DataFrame to CSV
        csv = speech_df.to_csv(index=False).encode('utf-8')

        # Provide a download button for the CSV file
        st.download_button(
            label="Download excel file",
            data=csv,
            file_name="speech_word_counts.csv",
            mime="text/csv"
        )
    else:
        st.warning("Please paste some text to process.")
