from flask import Flask
from flask import Flask, render_template,request
import pickle
app=Flask(__name__)
import pymysql as pms
conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="adhula",
                   db="mydb")
cursor=conn.cursor()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
def getcredentials():
    username =[]
    pwd=[]
    cursor.execute("SELECT * FROM table1")
    result =cursor.fetchall()
    print(result)
    for i in result:
        username.append(i[0])
        pwd.append(i[1])

    return username,pwd
@app.route('/')
def main():
    return render_template('index.html')
print("app1")

@app.route("/auth",methods=["POST"])
def auth():
    user= request.form.get('uname')
    password= request.form.get('psw')
    user='adhula'
    password='adhula'
    print(user,password)
    #check if the username and password are valid
    usename, pswd = getcredentials()
    if user in usename:
      if password  in pswd:
         return render_template('success.html')
    else:
        # if the username and password are not valid, redirect back to the login page
        return render_template('index.html', error='Invalid username or password')


@app.route("/predict",methods=["POST"])
def predict():
    #a = request.form.get("flavour")
    #b = request.form.get('scoops')
    a=101
    b=2
    print(a,b)
    prediction = model.predict([[a,b]])
    if(prediction):
      return render_template("result.html",value = prediction[0])


if __name__ == '__main__':
    
    app.run(debug=True,host='localhost',port=5000)