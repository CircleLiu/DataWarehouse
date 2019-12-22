from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/getproduct', methods=['POST'])
def getproduct():
    print(request.json)

    return jsonify({'status': 'OK'})

if __name__ == "__main__":
    app.run(debug=True)