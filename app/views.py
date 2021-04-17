import csv

from django.shortcuts import render

from .find_class_and_data import find_class_and_data

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    header_table = []
    data_table = []
    with open("inflation_russia.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            row = row[0].split(";")
            if idx == 0:
                header_table = row
            else:
                data_table.append(list(map(lambda x: find_class_and_data(x), row)))
    context = {
                'header_table' : header_table,
                'data_table' : data_table
                }

    return render(request, template_name, context)


