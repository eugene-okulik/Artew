# Дано
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

# Разбивка на слова
words = text.split()
print(words)

# Новый список для хранения новых слов
new_words = []

for word in words:
    if word[-1] in '.,':
        new_word = word[:-1] + 'ing' # Удаляем знак(.,) и добавляем окончание к слову
        new_word = new_word + word[-1] # Добавляем обратно знак 
    else:
        new_word = word + 'ing'
    new_words.append(new_word)

new_words = ' '.join(new_words)

print(new_words)
