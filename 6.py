import chardet


code_name = set()
lines = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as test_file:
    for line in lines:
        test_file.writelines(f'{line}\n')

with open('test_file.txt', 'br') as test_file:
    for line in test_file:
        code_name.add(chardet.detect(line)['encoding'])

with open('6.txt', 'w') as file_6:
    file_6.write(str(code_name) + '\n')

    with open('test_file.txt', 'r') as test_file:
        for line in test_file:
            line = line.encode('utf-8')
            file_6.writelines(line.decode('utf-8') + '\n')
