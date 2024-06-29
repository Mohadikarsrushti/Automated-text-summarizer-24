from transformers import T5Tokenizer, T5ForConditionalGeneration

def load_model():
    """
    Load the pre-trained T5 model and tokenizer.

    Returns:
    model: The T5 model.
    tokenizer: The T5 tokenizer.
    """
    # Load the pre-trained tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    return model, tokenizer

def summarize_text(model, tokenizer, text):
    """
    Generate a summary for the input text using the T5 model.

    Args:
    model: The T5 model.
    tokenizer: The T5 tokenizer.
    text (str): The input text to summarize.

    Returns:
    str: The generated summary.
    """
    # Tokenize the input text and prepare for the model
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    # Generate the summary
    summary_ids = model.generate(inputs, max_length=200, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    # Decode the summary
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Example usage
if _name_ == "_main_":
    model, tokenizer = load_model()
    sample_text = "Your long text document goes here. It can be a lengthy article, a research paper, or any other document that you need summarized."
    summary = summarize_text(model, tokenizer, sample_text)
    print("Summary:", summary)