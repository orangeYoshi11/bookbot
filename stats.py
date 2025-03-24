def get_word_count(text):
    count = len(str.split(text))
    return count

def get_character_count(text):
    d = {}
    text = text.lower()
    for char in text:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1
    return d

def sort_dict_count(collection):
    d = sorted(collection, key=lambda x: collection[x], reverse=True)
    return d