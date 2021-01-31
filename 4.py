words = ['разработка', 'администрирование', 'protocol', 'standard']
words_bytes = []

with open('4.txt', 'w') as file_4:
    for word in words:
        words_bytes.append(word.encode('utf-8'))
    for word in words_bytes:
        file_4.writelines(f'{word}\n')
    file_4.write('\n')
    for word in words_bytes:
        file_4.writelines(f'{word.decode("utf-8")}\n')
