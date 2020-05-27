from flask import Flask
from flask_restful import Resource, Api, reqparse

from algs import gcd

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('number')
parser.add_argument('a', type=int)
parser.add_argument('b', type=int)


class Methods(Resource):
    def get(self):
        return {'double': "2x2",
                "triple": "2x2x2",
                "gcd":"greatest common denominator between two ints"}


class double(Resource):
    def get(self):
        return 2 * 2

class triple(Resource):
    def get(self):
        return 2 * 2 * 2

class args_example(Resource):
    def get(self):
        return parser.parse_args()

class gcd_endpoint(Resource):
    def get(self, implementation: str) -> dict:
        args = parser.parse_args()
        a, b = args['a'], args['b']
        if (implementation == 'naive') and self.check_args(a,b):
            return {"method": "gcd",
                    "implementation": implementation, "result": gcd.gcd_naive(a, b),
                    "a": a,
                    "b": b}
        elif (implementation == 'clever') and self.check_args(a,b):
            return {"method": "gcd", "implementation": implementation, "result": gcd.gcd(a, b),
                    "a": a,
                    "b": b}
        else:
            return {"method": "gcd",
                    "implementation": implementation,
                    "result": "ERROR: must pass valid implementation (naive or clever) and valid a and b params, where a and b are integers 0 < a, b < 10 ** 7 ",
                    "a": a,
                    "b": b}

    def check_args(self, a: int, b: int) -> bool:
        if (a > 0) and (b > 0) and (a < 10**7) and (b< 10**7):
            return gcd.gcd(a, b)
        else:
            return f"acceptable values are any int greater than 1, you passed {a} and {b}"

api.add_resource(Methods, '/methods')
api.add_resource(double, '/double')
api.add_resource(triple, '/triple')
api.add_resource(args_example, '/args')
api.add_resource(gcd_endpoint, "/gcd/<string:implementation>")

if __name__ == '__main__':
    app.run("0.0.0.0", debug=False)
