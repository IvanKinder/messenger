import csv


def get_data():
    my_dict = {'Изготовитель системы': [], 'Название ОС': [], 'Код продукта': [], 'Тип системы': []}

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'r') as txt_file:
            for line in txt_file:
                for d in my_dict.keys():
                    if d in line:
                        my_dict[d].append(' '.join(line.split(':')[1].split()))
    return my_dict


file = 'csv_file.csv'


def write_to_csv(f):
    main_data = []
    with open(f, 'w') as csv_file:
        tmp_dict = get_data()
        num = len(tmp_dict.keys())
        main_data.append(list(tmp_dict.keys()))
        for i in range(num - 1):
            tmp_list = []
            for key in tmp_dict.keys():
                tmp_list.append(tmp_dict[key][i])
            main_data.append(tmp_list)
        f_n_writer = csv.writer(csv_file)
        for row in main_data:
            f_n_writer.writerow(row)


write_to_csv(file)
