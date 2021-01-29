import subprocess

import chardet

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
subproc_ping = []

for arg in args:
    subproc_ping.append(subprocess.Popen(arg, stdout=subprocess.PIPE))

with open('5.txt', 'w') as file_5:
    for url in subproc_ping:
        for line in url.stdout:
            code_name = chardet.detect(line)
            line = line.decode(code_name['encoding']).encode('utf-8')
            file_5.writelines(f'{line.decode("utf-8")}\n')
