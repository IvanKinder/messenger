import yaml

data = {
    '6\u019B': [6, 6, 5],
    '12\u019D': 5,
    '18\u519F': {
        '6\u019B': [6, 1],
        '12\u019D': 5
    }

}

print(data)

with open('yaml_file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)


with open('yaml_file.yaml', encoding='utf-8') as yaml_file:
    print(yaml_file.read())
