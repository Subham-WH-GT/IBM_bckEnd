from Maths.mathpck import sum,subtraction,multiplication
from flask import Flask,jsonify,make_response,request,render_template 

app=Flask('Mathematics Problem Solver')
@app.route('/sum')
def sum_route():
    num1=float(request.args.get('num1'))
    num2=float(request.args.get('num2'))
    result=sum(num1,num2)
    return str(result)

@app.route('/mul')
def mul_route():
    num1=float(request.args.get('num1'))
    num2=float(request.args.get('num2'))
    result=multiplication(num1,num2)
    return str(result)