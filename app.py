from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def login():
    pass


@app.route('/callback',methods=['GET','POST'])
def callback():
    pass


@app.route('/logout',methods=['GET','POST'])
def logout():
    pass


@app.route('/protected',methods=['GET','POST'])
def protected():
    pass




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=6968,debug=True)