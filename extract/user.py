import redis
import re
import csv

from itertools import islice

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_conn = redis.StrictRedis(connection_pool=redis_pool)


def cache():
    total_lines = 7911684 * 9
    with open('./movies.txt', 'r', errors='ignore') as f:
        for n, line in enumerate(f):
            if line.startswith('review/userId:'):
                user_id = line.split(':')[1].strip()
            if line.startswith('review/profileName:'):
                user_name = line.split(':')[1].strip()

            if n % 9 == 8:
                redis_conn.hset('user', user_id, user_name)

            print('\r {}%'.format(100*n/total_lines), end='')


def save():
    with open('./csv/user.csv', 'w', newline='') as csvfile:
        cw = csv.writer(csvfile)
        cw.writerow(['userID', 'profileName'])

        for i in range(redis_conn.scard('user:id')):
            user_id = str(redis_conn.spop('user:id'), encoding='utf-8')
            name = str(redis_conn.hget('user', user_id), encoding='utf-8')
            cw.writerow([user_id, name])
            print('\r{}'.format(i))


def load_id():
    ids = redis_conn.hkeys('user')
    for i in ids:
        redis_conn.sadd('user:id', i)



save()