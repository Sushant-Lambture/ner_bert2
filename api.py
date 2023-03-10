from flask import Flask,request,jsonify
from flask_cors import CORS
# from markupsafe import escape
# from itsdangerous import json
from bert import Ner

app = Flask(__name__)
CORS(app)

model = Ner("/home/sushant/env/ner_bert2/bert-base-cased/out_base")

@app.route("/predict",methods=['POST'])
def predict():
    text = request.json["text"]
    try:
        out = model.predict(text)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run('0.0.0.0',port=8000)