# alternative.py

text = input("Enter a string: ")

new_text = ""

for i in range(len(text)):
    if i % 2 == 0:
        new_text += text[i].upper()
    else:
        new_text += text[i].lower()

print(new_text)
words = text.split()

new_words = []

for i in range(len(words)):
    if i % 2 == 0:
        new_words.append(words[i].lower())
    else:
        new_words.append(words[i].upper())

result = " ".join(new_words)

print(result)