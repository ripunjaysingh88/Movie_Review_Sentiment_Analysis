from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
import inference

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods =['GET','POST'])
def index():
    if request.method=='POST':
            review = request.form['sentence'] 
            sentence = [review]
            predicted_result = inference.get_prediction(sentence)
            return render_template('show.html', result=predicted_result)
        
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))