from collections import defaultdict


def get_num_words(text):
    return len(text.split())


def get_num_characters(text):
    results = defaultdict(int)

    for char in text:
        results[char.lower()] += 1

    return dict(results)


def get_sorted_characters(characters):
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)