from flask import Flask, jsonify,request
from project_app.utils import Loan_Prediction
import config

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to Loan Prediction"

@app.route("/test")
def predict():
    Loan_ID = 1002.0
    Married = 0.0
    Dependents = 0.0
    Education  = 1.0
    Self_Employed = 0.0
    ApplicantIncome = 5849.0
    CoapplicantIncome = 0.0
    LoanAmount = 63.0
    Loan_Amount_Term = 229.0
    Credit_History = 1.0
    Property_Area = 1.0
    child = Loan_Prediction(Loan_ID,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    status = child.get_status()

    return jsonify({"return": f"Loan Status  : {status}"})


app.run()
    