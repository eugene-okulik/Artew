words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, count in words.items():
    new_words2 = ''.join(word for _ in range(count))
    print(new_words2)
