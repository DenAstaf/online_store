import csv


def read_csv(type_catalog="all"):
    with open('data_base/data_base.csv', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        if type_catalog == "all":
            return [row for row in reader]  # Возвращает list, содержащий словари с данными о всех товарах
        else:
            return [row for row in reader if type_catalog == row['type_catalog']]  # Возвращает list, содержащий словари с данными о нужном виде товара
def write_csv(data):
    with open('data_base/data_base.csv', 'w', newline='', encoding='utf-8') as csv_file:
        column_name = ["id", "type_catalog", "name", "price"]
        writer = csv.DictWriter(csv_file, fieldnames=column_name)
        writer.writeheader()
        for elem in data:
            writer.writerow(elem)
