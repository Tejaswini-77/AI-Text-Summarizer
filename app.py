import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import streamlit.components.v1 as components
from collections import Counter

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

st.set_page_config(
    page_title="AI-Based Text Summarisation System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("AI Text Summarization")

st.sidebar.markdown("---")

st.sidebar.write("Technology Used")
st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• NLTK")
st.sidebar.write("• Natural Language Processing (NLP)")

st.sidebar.markdown("---")

st.sidebar.write("Project Developed By")
st.sidebar.write("Koppula Tejaswini")

st.title("Design and Implementation of an AI-Based Text Summarisation System")
st.markdown("""
### Project Description

This application uses **Artificial Intelligence (AI)** and **Natural Language Processing (NLP)** to generate concise summaries from lengthy text documents. Users can either type text manually or upload a text file. The system analyses the input and produces a meaningful summary, helping users save time and quickly understand important information.
""")
st.write("Generate concise summaries from lengthy documents using Natural Language Processing")

st.subheader("Enter Your Text")

text = st.text_area(
    "Type or paste your text here",
    height=350
)

uploaded_file = st.file_uploader(
    "Or Upload a Text File",
    type=["txt"]
)

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    if text.strip() == "":
        st.warning("Uploaded file is empty.")

if text == "":
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    st.subheader("Sample Text")

    st.write(text)


def summarize_text(text):
    sentences = sent_tokenize(text)
    if len(sentences) <= 2:
        return text
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))

    filtered_words = []

    for word in words:
        if word.isalnum() and word not in stop_words:
            filtered_words.append(word)

    word_frequency = Counter(filtered_words)

    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequency:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequency[word]

    summary_length = max(2, len(sentences)//3)

    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:summary_length]
    summary_sentences = sorted(
        summary_sentences,
        key=lambda sentence: sentences.index(sentence)
    )

    summary = " ".join(summary_sentences)
    return summary


if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please enter some text or upload a text file.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(text)

        st.subheader("📄 Generated Summary")

        st.text_area(
            "Generated Summary",
            value=summary,
            height=180
        )

        col1,col2 = st.columns(2)

        with col1:
            st.metric("Original Words",len(text.split()))

        with col2:
            st.metric("Summary Words",len(summary.split()))

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "⬇ Download Summary",
                summary,
                file_name="summary.txt",
                mime="text/plain",
                use_container_width=True
            )

        with col2:
            components.html(
                f"""
                <textarea id="summary" style="display:none;">{summary}</textarea>

                <button
                onclick="
                navigator.clipboard.writeText(document.getElementById('summary').value);
                document.getElementById('msg').innerHTML='✅ Copied!';
                "
                style="
                width:100%;
                background:#4CAF50;
                color:white;
                border:none;
                padding:10px;
                border-radius:8px;
                cursor:pointer;
                ">
                📋 Copy Summary
                </button>

                <div id="msg" style="color:green;font-size:14px;margin-top:5px;"></div>
                """,
                height=75,
            )

        st.markdown("---")
st.caption("© 2026 AI Text Summarization System | Developed using Python, Streamlit and NLTK")