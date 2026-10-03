# Design and Implementation of an AI-Based Text Summarisation System

## Project Description
The AI-Based Text Summarisation System is a web application developed using Python, Streamlit, and Natural Language Processing (NLP). The application automatically generates concise summaries from lengthy textual content using an extractive text summarization approach. Users can either enter text manually or upload a text (.txt) file, and the system identifies the most important sentences using word frequency analysis and sentence scoring techniques.

## Features
- Manual text input
- Upload text files (.txt)
- Automatic extractive text summarization
- Word frequency-based sentence scoring
- Original and summary word count
- Download generated summary
- Copy summary to clipboard
- Simple and user-friendly interface

## Technologies Used
- Python
- Streamlit
- NLTK (Natural Language Toolkit)
- Natural Language Processing (NLP)

## Project Structure
```
AI_Text_Summarization/
│
├── app.py
├── sample.txt
├── README.md
├── requirements.txt
```

## How to Run the Project

1. Install Python.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python -m streamlit run app.py
   ```

## Future Enhancements
- PDF document summarization
- DOCX document support
- Multi-language text summarization
- Abstractive summarization using transformer models
- User-selectable summary length
- Cloud deployment

## Applications
- Education
- Research
- Journalism
- Business reporting
- News summarization
- Content analysis

## Author
**Developed By:** Koppula Tejaswini
