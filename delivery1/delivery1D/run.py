import requests
from typing import List, Tuple

def get_wikipedia_content(title: str) -> str:
    """
    Retrieves the content of a Wikipedia article based on the provided title.

    Args:
        title: The title of the Wikipedia article.

    Returns:
        The content of the Wikipedia article as a string.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={title}&explaintext=1"
    response = requests.get(url)
    data = response.json()
    page_id = list(data["query"]["pages"].keys())[0]
    content = data["query"]["pages"][page_id]["extract"]
    return content

def get_all_words(text: str) -> List[str]:
    """
    Retrieves all words from a given text, using a generator function

    Args:
        text: The text to search words from.

    Returns:
        A list of filtered words.
    """
    words = text.split()
    for word in words:
        if word.endswith("-"):
            yield from get_all_words(word.rstrip("-"))
        else:
            yield word

def count_words_with_more_than_4_chars(content: str) -> int:
    """
    Counts the number of words in the content with more than 4 characters.

    Args:
        content: The content to analyze.

    Returns:
        The count of words with more than 4 characters.
    """
    words = (word for word in get_all_words(content) if len(word) > 4)
    count = sum(1 for _ in words)
    return count

def get_top_5_most_common_words(content: str) -> List[Tuple[str, int]]:
    """
    Retrieves the 5 most common words in the content with more than 4 characters.

    Args:
        content: The content to analyze.

    Returns:
        A list of tuples containing the most common words and their frequencies.
    """
    words = (word for word in get_all_words(content) if len(word) > 4)
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_words

# Título del artículo de Wikipedia. TODO Cambiarlo o parametrizarlo
article_title = "Madrid"

# Obtener el contenido del artículo
article_content = get_wikipedia_content(article_title)

# Obtener la cantidad de palabras con más de 4 caracteres
word_count = count_words_with_more_than_4_chars(article_content)

# Obtener las 5 palabras más repetidas
top_words = get_top_5_most_common_words(article_content)

# Imprimir los resultados
print("Number of words with more than 4 characters:", word_count)
print("Top 5 most common words:")
for word, frequency in top_words:
    print(word, "-", frequency)
