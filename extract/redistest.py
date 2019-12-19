import redis
import re
import csv

from itertools import islice

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_conn = redis.StrictRedis(connection_pool=redis_pool)


def cache():
    with open('./rawdata/warehouse_product.csv', 'r', errors='ignore') as f:
        csvdata = csv.reader(f)
        for n, line in enumerate(csvdata):
            if line[2]:
                actors = [i.strip() for i in line[2].split(',')]
                for i in actors:
                    redis_conn.sadd('actor', i)

            if line[3]:
                directors = [i.strip() for i in line[2].split(',')]
                for i in directors:
                    redis_conn.sadd('director', i)

            print('\r {}'.format(n), end='')


def save():
    with open('./csv/director.csv', 'w', newline='') as csvfile:
        cw = csv.writer(csvfile)

        director = redis_conn.smembers('director')
        for i, n in enumerate(director):
            aid = i + 1
            name = str(n, encoding='utf-8')
            cw.writerow([aid, name])
            print('\r {}'.format(i), end='')

    print('finished')

def load_id():
    ids = redis_conn.hkeys('user')
    for i in ids:
        redis_conn.sadd('user:id', i)



save()