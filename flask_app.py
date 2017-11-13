from logic import *
from utils import expr_handle_infix_ops, count, Symbol

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/dpllsatisfiable', methods=['POST'])
def dpllsatisfiable():
    if not request.json or not 'knowledgebase' in request.json:
        abort(400)
    knowledgebase = request.json['knowledgebase']    
    result = str(dpll_satisfiable(expr(knowledgebase)))
    return jsonify({'result':result}), 201

if __name__ == '__main__':
    app.run(debug=True)

print(dpll_satisfiable(expr('A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) & (B | ~C | D) & (A | ~E | F) & (~A | E | D)')))
