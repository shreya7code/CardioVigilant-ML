Tech Stack Used:
1. Python and Data Science Libraries
2. HTML/CSS
3. Flask

By following these steps, you can run our heart disease prediction model locally and obtain predictions using the Flask API
Once you have done yoiur flask set up

1. Go to src folder > phase_3 folder

2.  Run the command python app.py to run the app.py file. Which will take you to our web page on your localhost.
      - The app.py code uses the pretrained model (model.pkl) that we have created in previous phase and run the model for our user. 
      - We have created the pickle file for our model in phase 2.

3. Input Data and Get Predictions
   - On the home page, you'll find input fields to enter information for heart disease prediction, such as age, cholesterol level, blood pressure, etc.
   - After entering the required information, submit the form.
   - The Flask API processes the input data using the trained machine learning model.
   - You will receive predictions regarding the likelihood of heart disease based on the input data

