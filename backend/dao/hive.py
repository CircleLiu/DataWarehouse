from pyhive import hive

conn = hive.Connection(host='192.168.50.235', port=10000, username='root', database='movie')

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

get_movie_by_name('Titanic')