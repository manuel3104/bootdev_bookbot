def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_words(text):
    """Zählt die Anzahl der Wörter in einem Text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Zählt die Häufigkeit jedes Zeichens im Text.
    Konvertiert alle Zeichen zu Kleinbuchstaben.
    Filtert nur Buchstaben (keine Leerzeichen/Satzzeichen).
    """
    char_count = {}
    
    for char in text:
        char_lower = char.lower()
        # Nur Buchstaben zählen (keine Leerzeichen, Satzzeichen, etc.)
        if char_lower.isalpha():
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
    
    return char_count

def sort_characters_by_count(char_dict):
    """
    Sortiert das Zeichen-Dictionary nach Häufigkeit (absteigend).
    Gibt eine Liste von Tupeln zurück: [(char, count), ...]
    """
    # Dictionary in Liste von Tupeln umwandeln und nach count sortieren
    char_list = list(char_dict.items())
    char_list.sort(key=lambda x: x[1], reverse=True)
    return char_list