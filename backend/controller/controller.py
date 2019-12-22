from application import app
from flask import request

@app.route('/getproduct', methods=['POST'])
def getproduct():
    print(request.json)

    return 201