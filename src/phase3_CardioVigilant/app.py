#Importing relevant libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# set up flask configuration
app = Flask(__name__, static_url_path='/static', static_folder='static')

#load our model which we created using pickle 
model = pickle.load(open('model.pkl', 'rb'))

#rendering to our home page
@app.route('/')
def home():
    return render_template('index.html')

#Our prediction URL 
@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0],12)
    #when output = 1 User has heart disease else No
    if output==1:
        return render_template('index.html', prediction_text='We are sorry to inform that you may have Heart Disease! Please seek medical advise')
    else:
        return render_template('index.html', prediction_text='Congratulations! You dont have any Heart Disease! Stay Healthy')
        
    
#
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

#####auth:shreya
@app.route('/analytics')
def analytics():
    return render_template('analytics.html')



if __name__ == "__main__":
    app.run(debug=False)
