import numpy as np
import pandas as pd
import pickle
import json
import config

class Loan_Prediction():
    def __init__(self,Loan_ID, Married, Dependents, Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
     LoanAmount,Loan_Amount_Term,Credit_History,Property_Area) :
     self.Loan_ID = Loan_ID
     self.Married = Married
     self.Dependents = Dependents
     self.Education = Education
     self.Self_Employed = Self_Employed
     self.ApplicantIncome = ApplicantIncome
     self.CoapplicantIncome = CoapplicantIncome
     self.LoanAmount = LoanAmount
     self.Loan_Amount_Term = Loan_Amount_Term
     self.Credit_History = Credit_History
     self.Property_Area = Property_Area

    def Load_Model(self):
      with open (config.MODEL_PATH,'rb') as f:
          self.model = pickle.load(f)

      with open(config.JSON_PATH,'r') as f:
          self.json_data = json.load(f)
            
    def get_status(self):
      self.Load_Model()
      test_array = np.zeros(len([self.Loan_ID, self.Married, self.Dependents, self.Education, self.Self_Employed,
      self.ApplicantIncome, self.CoapplicantIncome, self.LoanAmount,
      self.Loan_Amount_Term, self.Credit_History, self.Property_Area]))    
      print(test_array)
      test_array[0] = self.Loan_ID
      test_array[1] = self.Married
      test_array[2] = self.Dependents
      test_array[3] = self.Education
      test_array[4] = self.Self_Employed
      test_array[5] = self.ApplicantIncome
      test_array[6] = self.CoapplicantIncome
      test_array[7] = self.LoanAmount
      test_array[8] = self.Loan_Amount_Term
      test_array[9] = self.Credit_History
      test_array[10] = self.Property_Area
      print(test_array)

      predict = self.model.predict([test_array])[0]
      
      return predict
