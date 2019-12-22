from flask import Flask
from flask import request, jsonify
import dao.neo as neo

app = Flask(__name__)

@app.route('/getproduct', methods=['POST'])
def getproduct():
    print(request.json)

    return jsonify({'status': 'OK'})


@app.route('/actor_with_actor', methods=['POST'])
def cactor_with_actor():
    name = request.json['name']
    res = neo.actor_with_actor(name)
    res = [{'name': v['d2.actor_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/actor_with_director', methods=['POST'])
def actor_with_director():
    name = request.json['name']
    res = neo.actor_with_director(name)
    res = [{'name': v['d2.director_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/director_with_actor', methods=['POST'])
def director_with_actor():
    name = request.json['name']
    res = neo.director_with_actor(name)
    res = [{'name': v['d2.actor_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/director_with_director', methods=['POST'])
def director_with_director():
    name = request.json['name']
    res = neo.director_with_director(name)
    res = [{'name': v['d2.director_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/collaboration_of_actor', methods=['POST'])
def collaboration_of_actor():
    n = request.json['name']
    res = neo.collaboration_of_actor(n)
    res = [{'name1': v['d1.actor_name'], 'name2': v['d2.actor_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/collaboration_of_director', methods=['POST'])
def collaboration_of_director():
    n = request.json['name']
    res = neo.collaboration_of_director(n)
    res = [{'name1': v['d1.director_name'], 'name2': v['d2.director_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

@app.route('/collaboration_of_director_and_actor', methods=['POST'])
def collaboration_of_director_and_actor():
    n = request.json['name']
    res = neo.collaboration_of_director_and_actor(n)
    res = [{'actor': v['d1.actor_name'], 'director': v['d2.director_name'], 'count': v['count(p)']} for v in res]
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)