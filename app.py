from flask import Flask
from flask import Flask, render_template,request
import pickle
app=Flask(__name__)
print("app=flask()")
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
    print("in get credentials")
    username =[]
    pwd=[]
    cursor.execute("SELECT * FROM table1")
    result =cursor.fetchall()
    print(result)
    for i in result:
        username.append(i[0])
        pwd.append(i[1])

    return username,pwd
@app.route("/")
def main():
    print("app1")
    return render_template('index.html')

@app.route("/auth",methods=["POST"])
def auth():
    print("app2")
    user= request.form.get('uname')
    password= request.form.get('psw')
    user='lol'
    password='lol'
    print(user,password)
    #check if the username and password are valid
    usename,pswd = getcredentials()
    if user in usename:
      if password  in pswd:
         return render_template('success.html')
    else:
        # if the username and password are not valid, redirect back to the login page
        return render_template('index.html', error='Invalid username or password')


@app.route("/predict",methods=["POST"])
def predict():
    print("app3")
    #flavour= request.form.get("flavour")
    #scoops= request.form.get("scoops")
    flavour=101
    scoops=2
    print(flavour,scoops)
    prediction = model.predict([[flavour,scoops]])
    if(prediction):
      return render_template("result.html",value = prediction[0])


if __name__ == '__main__':
    print("main")
    app.run(host='localhost',port=5000)
