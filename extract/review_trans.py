import csv
from tqdm import tqdm

number_of_reviews = 7911684

with open('./rawdata/movies.txt', 'r', errors='ignore') as datafile:
    block = [''] * 9
    
    with open('./csv/all_review.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for n in tqdm(range(number_of_reviews)):
            for i in range(9):
                block[i] = datafile.readline()

            row = [j.split(':', 1)[1].strip() if ':' in j else '' for j in block[:8]]
            writer.writerow(row)
