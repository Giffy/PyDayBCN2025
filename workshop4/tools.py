"""Agent's tool library - can be extended at runtime!"""
from textblob import TextBlob
import textblob

def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

3

def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of a given text string using TextBlob library.

    Parameters:
    - text (str): The text to analyze for sentiment.

    Returns:
    - dict: A dictionary containing the polarity, subjectivity,
            and a label indicating if it's positive, negative or neutral.
    """

    # Use TextBlob to get the sentiment analysis
    blob = textblob.TextBlob(text)
    
    # Convert polarity from 0-1 to -1-1 for consistency in our function
    blob.polarity = -blob.sentiment.polarity

    # Return the result as a dictionary, where 'polarity', 'subjectivity', and 'label' are fields
    return {
        "polarity": blob.polarity,
        "subjectivity": blob.sentiment.subjectivity,
        "label": "positive" if blob.sentiment.polarity > 0 else ("negative" if blob.sentiment.polarity < 0 else "neutral")
    }

def count_words(text: str) -> dict:
    """
    Count words in a given text.
    
    Parameters:
    - text (str): The text string to analyze.
    
    Returns:
    - dict: A dictionary containing the following keys:
        total_words: Total number of unique words
        unique_words: Number of unique words
        char_count: Total characters excluding spaces
    """
    # Initialize a TextBlob object for the text
    blob = TextBlob(text)
    
    # Convert all words to lowercase and filter out punctuation
    word_counts = {word.lower(): count for word, count in blob.words}
    
    return {
        'total_words': len(word_counts),
        'unique_words': len(word_counts),
        'char_count': len(''.join(blob.words))
    }

# Function to check the correctness of the solution
def check_solution():
    sample_text = "The quick brown fox jumps over the lazy dog."
    result = count_words(sample_text)
    print(result)

if __name__ == "__main__":
    # Example usage: Check with a predefined text string
    check_solution()

# Registry of available tools
TOOLS = {
    "count_words": count_words,
    "analyze_sentiment": analyze_sentiment,
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
}
