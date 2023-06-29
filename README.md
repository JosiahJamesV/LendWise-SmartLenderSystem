Lendwise - Smart Lender System

Team Members:
Saumya Goel 
Aryan Gudetti 
Karthik G
Josiah James 


VIDEO DEMO LINK:
https://drive.google.com/file/d/1E6hkmzHHDyKEzS6qokDRj6I_fWg_QfB7/view?usp=sharing


Welcome to Lendwise, a Smart Lender System built with the power of machine learning! This project aims to predict loan eligibility based on various factors using different classification models. The frontend of the application is developed using React and leverages frameworks like Formik and Yup for form handling. On the backend, we have a Flask server that interacts with a Python model, which performs data processing, scaling, and training using classification techniques such as KNN, Random Forest, Naive Bayes, XG Boost, Logistic Regression, and Decision Tree.

Features
Predicts loan eligibility based on user inputs using advanced machine learning models.
User-friendly frontend built with React, providing a seamless and intuitive interface.
Form handling and validation made easy with the use of Formik and Yup frameworks.
Flask server acts as a bridge between the frontend and the Python model, facilitating data processing and fetching predictions.
Different classification models utilized for accurate loan eligibility predictions.
Installation
To run the Lendwise Smart Lender System on your local machine, follow these steps:

Clone the repository:
git clone https://github.com/your-username/lendwise.git

Navigate to the Flask server directory:
cd lendwise/flask-server

Install the required Python dependencies:
pip install -r requirements.txt

Start the Flask server:
python3 server.py

Open a new terminal window and navigate to the React client directory:
cd lendwise/client

Install the required Node.js dependencies:
npm install
Start the React development server:
npm start

Open your web browser and access the application at http://localhost:3000.


Usage
- Fill in the loan application form with the necessary details.
- Click on the "Check Eligibility" button to submit the form.
- The system will utilize the machine learning models to predict your loan eligibility.
- The result will be displayed on the screen, indicating whether you are eligible for the loan or not.

Enjoy using Lendwise - the Smart Lender System!
