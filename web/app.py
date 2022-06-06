from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)

api=Api(app)

def checkposted(posted, function):
    if(function == "add" or function == "subtract" or function == "multiply"):
        if "x" not in posted or "y" not in posted:
            return 301
        else:
            return 200
    else:
        if "x" not in posted or "y" not in posted:
            return 301
        elif(int(posted["y"]) == 0):
            return 302
        else:
            return 200

class Adicao(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "add")
        if(status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        sum = x+y
        ret = {
            'Message': sum,
            'Status code': 200
        }
        return jsonify(ret)

class Subtracao(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "subtract")
        if(status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        diff = x-y
        ret = {
            'Message': diff,
            'Status code': 200
        }
        return jsonify(ret)
class Multiplicacao(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "multiply")
        if (status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        prod = x * y
        ret = {
            'Message': prod,
            'Status code': 200
        }
        return jsonify(ret)
class Divisao(Resource):
    def post(self):
        posted = request.get_json()
        status = checkposted(posted, "divide")
        if (status != 200):
            retJ = {
                "Message": "An error happened",
                "Status code": status
            }
            return jsonify(retJ)
        x = posted["x"]
        y = posted["y"]
        x = int(x)
        y = int(y)
        quo = x*1.0/ y
        ret = {
            'Message': quo,
            'Status code': 200
        }
        return jsonify(ret)

api.add_resource(Adicao, "/Adicao")
api.add_resource(Subtracao,"/Subtracao")
api.add_resource(Multiplicacao,"/Multiplicacao")
api.add_resource(Divisao,"/Divisao")
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)