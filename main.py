import sys
from stats import get_book_text, count_words, count_characters, sort_characters_by_count

def main():
    # Command Line Arguments prüfen
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Dateipfad aus Command Line Argument holen
    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    try:
        # Buch-Inhalt laden
        book_content = get_book_text(filepath)
        
        # Wörter zählen
        print("----------- Word Count ----------")
        num_words = count_words(book_content)
        print(f"Found {num_words} total words")
        
        # Zeichen zählen und sortieren
        print("--------- Character Count -------")
        char_counts = count_characters(book_content)
        sorted_chars = sort_characters_by_count(char_counts)
        
        # Sortierte Zeichen ausgeben
        for char, count in sorted_chars:
            print(f"{char}: {count}")
        
        print("============= END ===============")
        
    except FileNotFoundError:
        print(f"Error: Could not find file at {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Main-Funktion aufrufen
if __name__ == "__main__":
    main()