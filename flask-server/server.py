from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from joblib import load

app = Flask(__name__)
CORS(app)

model = load('knn_model.joblib')

scaler = load('scaler.joblib')

@app.route('/form', methods=['POST'])
def form_predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0])
    
    le = LabelEncoder()
    df["Gender"] = le.fit_transform(df["Gender"])
    df["Married"] = le.fit_transform(df["Married"])
    df["Education"] = le.fit_transform(df["Education"])
    df["Self_Employed"] = le.fit_transform(df["Self_Employed"])
    df["Property_Area"] = le.fit_transform(df["Property_Area"])
    df["Dependents"] = df["Dependents"].astype(float)
    
    df.drop(["loanID", "lastName", "firstName"], axis=1, inplace=True)

    df["ApplicantIncome"] = pd.to_numeric(df["ApplicantIncome"])
    df["CoapplicantIncome"] = pd.to_numeric(df["CoapplicantIncome"])
    df["LoanAmount"] = pd.to_numeric(df["LoanAmount"])
    df["Loan_Amount_Term"] = pd.to_numeric(df["Loan_Amount_Term"])
    df["Credit_History"] = pd.to_numeric(df["Credit_History"])

    df_scaled = df.copy()
    numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]
    df_scaled[numerical_columns] = scaler.transform(df[numerical_columns])

    predictions = model.predict(df_scaled)
    
    response = jsonify({"predictions": predictions.tolist()})
    
    return response

if __name__ == "__main__":
    app.run(port=8000, debug=True)
