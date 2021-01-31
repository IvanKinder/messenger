try:
    words = [b'attribute', b'класс', b'функция', b'type']
    for word in words:
        print(word)
except SyntaxError as err:
    print(err)
