import streamlit as st
import pandas as pd
import re
from collections import Counter
from io import BytesIO

# Streamlit App
def main():
    st.title("Text File Word Count Analyzer")
    st.write(
        "This app allows you to upload a text file, "
        "counts the word frequencies, and provides an option to download the results."
    )
    
    # File uploader widget
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

    if uploaded_file is not None:
        # Read and display the content of the uploaded file
        content = uploaded_file.read().decode("utf-8")
        st.subheader("File Content Preview")
        st.text(content[:1000])  # Display a preview of the first 1000 characters

        # Process the text: remove punctuation and convert to lowercase
        processed_text = re.sub(r'[^\w\s]', '', content).lower()

        # Tokenize the text into words and count their frequency
        tokenized_words = processed_text.split()
        word_counts = Counter(tokenized_words)

        # Convert counts to a DataFrame
        speech_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count']).reset_index()
        speech_df.columns = ['Word', 'Count']
        speech_df = speech_df.sort_values(by='Count', ascending=False).reset_index(drop=True)

        # Display the DataFrame
        st.subheader("Word Count Results")
        st.dataframe(speech_df)

        # Provide an option to download the results as an Excel file
        if st.button("Download as Excel"):
            # Convert DataFrame to Excel
            towrite = BytesIO()
            with pd.ExcelWriter(towrite, engine='xlsxwriter') as writer:
                speech_df.to_excel(writer, index=False, sheet_name="Word Counts")
            towrite.seek(0)
            st.download_button(
                label="Download Excel file",
                data=towrite,
                file_name="speech_word_counts.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()
