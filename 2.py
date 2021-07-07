words = [b'class', b'function', b'method']


with open('2.txt', 'w') as file_2:
    for word in words:
        file_2.writelines(f'{word}: {type(word)}; len: {len(word)}\n')
