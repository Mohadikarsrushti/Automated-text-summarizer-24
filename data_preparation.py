import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the input text by tokenizing, removing stopwords, and returning a cleaned string.

    Args:
    text (str): The input text to preprocess.

    Returns:
    str: The preprocessed text.
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [w for w in word_tokens if not w.lower() in stop_words]
    return ' '.join(filtered_text)

# Example usage
if _name_ == "_main_":
    sample_text = "This is a sample text for preprocessing. It will remove stopwords and tokenize the text."
    cleaned_text = preprocess_text(sample_text)
    print("Original Text:", sample_text)
    print("Cleaned Text:", cleaned_text)