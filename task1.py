import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)[1:]  # список списков с параметрами: id, name, titleProject_id, class, score
    count_class = {}  # количество потерявших в классе
    sum_class = {}  # сумма всех оценок учеников класса
    for id, name, titleProject_id, level, score in answer:
        if "Хадаров Владимир" in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)

    # исправляем утеряные значения
    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open("sudent_new.csv", "w", encoding="utf8", newline='') as file:
    w = csv.writer(file)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])  # заголовок
    w.writerows(answer)
