from flask import Flask

app=Flask(__name__)

@app.route('/mani')
def welcome():
    return "this is your you tube channel"


if __name__=='__main__':
    app.run(debug=True)