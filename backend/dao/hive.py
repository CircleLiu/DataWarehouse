from pyhive import hive

conn = hive.Connection(host='180.160.39.41', port=10000, username='root', database='movie')

def get_product_by_id(product_id):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where asin=\'{product_id}\'')
    result = cursor.fetchall()
    return result

def get_movie_by_date(start_date, end_date):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where release_date >= \'{start_date}\' and release_date <= \'{end_date}\'')
    result = cursor.fetchall()
    return result

def get_movie_by_name(name):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where name like \'{name}%\' ')
    result = cursor.fetchall()
    return result

def get_movie_by_actor(name):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where actor like \'%{name}%\' ')
    result = cursor.fetchall()
    return result

def get_movie_by_director(name):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where director like \'%{name}%\' ')
    result = cursor.fetchall()
    return result

def get_movie_by_genres(genres):
    cursor = conn.cursor()
    cursor.execute(f'select * from all_product where genres like \'%{genres}%\' ')
    result = cursor.fetchall()
    return result

def condition_search(conditions):
    sql = 'select asin, name, price, running_time, rank, publication_date, release_date from all_product '
    for i, condition in enumerate(conditions):
        if i == 0:
            sql += ' where {} {} \'{}\' '.format(condition['field'], condition['condition'], condition['value'])
        else:
            sql += ' {} {} {} \'{}\' '.format(condition['ao'], condition['field'], condition['condition'], condition['value'])
    print(sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return [{
        'asin': r[0],
        'name': r[1],
        'price': float(r[2]) if r[2] is not None else None,
        'running_time': r[3],
        'rank': r[4],
        'publication_date': r[5],
        'release_date': r[6]
    } for r in result]