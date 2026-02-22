import pickle
from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)


model=pickle.load(open("models/house adaboost.pkl","rb"))
scaler=pickle.load(open("models/scaler.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictions",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="POST":
        age=float(request.form.get("age"))
        salary=float(request.form.get("estimated_salary"))
        new_scaled_data=scaler.transform([[age,salary]])
        result=model.predict(new_scaled_data)
        return render_template("home.html",results=result[0])
    
    else:
        return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)