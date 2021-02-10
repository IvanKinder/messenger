import json


def get_data_from_message(response: bytes):
    data_parse = json.loads(response)
    return data_parse


def send_message(data: dict):
    return json.dumps(data)


def get_settings():
    with open('common/conf.json') as conf_file:
        content = conf_file.read()
        conf_set = json.loads(content)
    return conf_set
