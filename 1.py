words = ['разработка', 'сокет', 'декоратор']
words_utf_8 = ['\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
               '\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
               '\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

ex1 = []

for word in words:
    ex1.append(f'{word}: {type(word)}')

for word in words_utf_8:
    ex1.append(f'{word}: {type(word)}')

for word in ex1:
    print(word)

with open('1.txt', 'w', encoding='utf-8') as file_1:
    for word in ex1:
        if ex1.index(word) == 3:
            file_1.write('\n')
        file_1.writelines(word + '\n')
