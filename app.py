from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("Titanic.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output==0:
        return render_template('Titanic.html',pred="OW!! Died")
    else:
        return render_template('Titanic.html',pred="Hurray!! Alive")


if __name__ == '__main__':
    app.run(debug=True)
