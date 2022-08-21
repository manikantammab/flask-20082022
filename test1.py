from flask import Flask,request,jsonify

app=Flask(__name__)#Flask is class and app is object

@app.route('/abc',methods=['GET','POST'])#abc is root(path)
def test1():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify((str(result)))

@app.route('/abc1/sudh',methods=['GET','POST'])
def test2():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a*b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test3',methods=['GET','POST'])
def test3():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a**b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test4',methods=['GET','POST'])
def test4():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a-b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test5',methods=['GET','POST'])
def test5():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a/b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test6',methods=['GET','POST'])
def test6():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a/b
        return jsonify((str(result)))


if __name__=='__main__':#it try invoke the enter the python main
    app.run()



def test(a,b):
    return a+b

#1.write a program to insert a record in sql table via api database
#2.write a program to update a record via api
#3.write a program to delete a record via api
#4.write a program to fetch a record via api
#5. all the above questions you have to answer for mongo db as well.