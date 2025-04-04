def get_num_words(text):
    return len(text.split())

def map_characters_count(text):
    texts = text.lower()
    result_dict = {}
    for char in texts:
        if result_dict.get(char):
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    return result_dict

def sort_characters_count_dict(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
