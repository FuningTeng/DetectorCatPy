from logic import *
from utils import expr_handle_infix_ops, count, Symbol
from flask.ext.cors import CORS, cross_origin
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
    
@app.route('/api/dpllsatisfiable', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def dpllsatisfiable():
    if not request.json or not 'knowledgebase' in request.json:
        abort(400)
    
    knowledgebase = request.json['knowledgebase']    
    result = str(dpll_satisfiable(expr(knowledgebase)))
    return jsonify({'result':result}), 201

if __name__ == '__main__':
    app.run()

