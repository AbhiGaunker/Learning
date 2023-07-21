from flask import Flask,request, render_template , jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods = ['POST'])
def math_operation1():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        if ops == 'add':
            ans = num1 + num2
            result = f"sum of    {num1} + {num2} is    {ans}" 
        elif ops =='subtract':
            ans = num1 - num2
            result = f"difference of {num1} - {num2} is {ans}"
        elif ops =='multiply':
            ans = num1 * num2
            result = f"product of {num1} * {num2} is {ans}"
        elif ops == 'divide':
            ans = num1 / num2 
            result = f"division of {num1} / {num2} is {ans}"
        
        return render_template('results.html',result = result)


@app.route('/info')
def info():
    return "this my information about application"

@app.route('/info/get')
def test():
    data = request.args.get('x')
    return "this is data input from my url {}".format(data)


@app.route('/postman_data',methods = ['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if ops == 'add':
            ans = num1 + num2
            result = f"sum of    {num1} + {num2} is    {ans}" 
        elif ops =='subtract':
            ans = num1 - num2
            result = f"difference of {num1} - {num2} is {ans}"

        elif ops =='multiply':
            ans = num1 * num2
            result = f"product of {num1} * {num2} is {ans}"

        elif ops == 'divide':
            ans = num1 / num2
            result = f"division of {num1} / {num2} is {ans}"
        
        return render_template('results.html',result = result)


if __name__ == '__main__':
    app.run(host= "0.0.0.0")