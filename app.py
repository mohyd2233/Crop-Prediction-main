from flask import Flask, render_template, jsonify, request
import pickle as pkl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods = ['GET','POST'])
def prediction():
    if request.method=='POST':
        nitro = request.form.get('nitrogen')
        phos = request.form.get('phosphorus')
        pott = request.form.get('potassium')
        temp = request.form.get('temperature')
        hum = request.form.get('humidity')
        ph = request.form.get('ph')
        rf = request.form.get('rainfall')
        print(nitro,phos,pott,temp,hum,ph,rf)
        with open('model.pkl','rb') as model_file:
            mlmodel = pkl.load(model_file)
        res = mlmodel.predict([[float(nitro),float(phos),float(pott),float(temp),float(hum),float(ph),float(rf)]])
        return render_template("result.html",res=res)
    else:
        return render_template('/prediction.html')


'''@app.route('/showdata')
def showdata():
    return render_template('showdata.html')'''

if __name__ == '__main__':
    app.run()

