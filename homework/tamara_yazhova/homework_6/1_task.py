text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = text.split()
fin_text = []

for word in words:
    if word[-1] in '.,':
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    fin_text.append(new_word)
print(' '.join(fin_text))
