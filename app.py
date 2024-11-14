from collections import Counter
import streamlit as st
import pandas as pd
import re

# Streamlit app
st.title("Speech (Text) Word Counter")

st.write("A text processing tool to help with Take-Home Assignment 3 for statistics.")

# User input text box
user_input = st.text_area("Paste your text here")

# Add a submit button
if st.button("Submit for processing"):
    
    # st.divider()

    if user_input:
        # Preprocess the input text (remove punctuation, and numbers, convert to lowercase)
        processed_text = re.sub(r'[^\w\s]|[\d]', '', user_input).title()

        # Tokenize the input text into words
        tokenized_words = processed_text.split()

        # Count the frequency of words in the input text
        word_counts = Counter(tokenized_words)

        # Convert counts to a DataFrame
        speech_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Occurence']).reset_index()
        speech_df.columns = ['Word', 'Occurrence']

        # Display the DataFrame

        st.success("Your excel file is ready! 🎉, Scroll down to download the file")

        
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

# st.info('For support regarding the tool, contact https://wa.me/qr/VBL77I3GHYG6K1', icon="ℹ️")

# st.divider()

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f1f1f1;
        padding: 10px 10px;
        text-align: center;
        font-size: 12px;
    }
    </style>
    <div class="footer">
         <h6>
         For support regarding the tool, contact <a href="https://wa.me/qr/VBL77I3GHYG6K1" target="_blank">here</a>.
        </h6>
        Made with ❤️ by your M1 course representatives.<br>
    </div>
    """,
    unsafe_allow_html=True
)


