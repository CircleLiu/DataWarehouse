import csv
from tqdm import tqdm

number_of_reviews = 7911684

with open('./rawdata/movies.txt', 'r', errors='ignore') as datafile:
    block = [''] * 9
    
    with open('./csv/all_review.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        for n in tqdm(range(number_of_reviews)):
            for i in range(9):
                block[i] = datafile.readline()
                while i == 3 and not block[3].startswith('review/helpfulness'):
                    block[3] = datafile.readline()
                while i == 8 and block[8] != '\n':
                    block[8] = datafile.readline()

            try:
                row = [j.split(':', 1)[1].strip() for j in block[:8]]
                writer.writerow(row)
            except:
                print(block)
                break
            
