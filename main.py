from stats import get_word_count
import stats
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

bookpath = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
content = get_book_text(bookpath)

num_words = get_word_count(content)
char_count = stats.get_character_count(content)

#Book Title
print(f"{"="*10} BOOKBOT {"="*10}\nAnalyzing book found at {bookpath}..." )

#Word Count
print(f"{"-"*13} Word Count {"-"*12}\nFound {num_words} total words")

#Character Breakout
results = stats.sort_dict_count(char_count)
print(f"{"-"*10} Character Count {"-"*10}")

for k in results:
    if k.isalpha():
        print(f"{k}: {char_count[k]}")

