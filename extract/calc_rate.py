import csv

rate = {}

with open('./csv/all_review.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        rate.setdefault(row[0], {'total': 0, 'num': 0, 'avg': 0})

        rate[row[0]]['total'] += float(row[4])
        rate[row[0]]['num'] += 1

    for i in rate.values():
        i['avg'] = i['total'] / i['num']

with open('./csv/rate.csv', 'w') as f:
    writer = csv.writer(f)

    for k, i in rate.items():
        writer.writerow([k, i['num'], i['avg']])