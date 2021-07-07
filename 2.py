import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {"orders": [{'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}]}
    with open('orders.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


write_order_to_json('apple', 12000, 200, 'John Dorian', '02.02.2022')
