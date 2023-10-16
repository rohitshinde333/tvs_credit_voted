from flask import Flask, request, jsonify
import pickle
from collections import Counter
import pandas as pd
app = Flask(__name__)
import statistics
with open('gbc_model.pkl', 'rb') as gbc_model_file:
    gbc_model = pickle.load(gbc_model_file)

with open('isolation_forest_model.pkl', 'rb') as iforest_model_file:
    iforest_model = pickle.load(iforest_model_file)

with open('knn_model.pkl', 'rb') as knn_model_file:
    knn_model = pickle.load(knn_model_file)

with open('logistic_regressoin_model.pkl', 'rb') as lr_model_file:
    lr_model = pickle.load(lr_model_file)

with open('one_class_svm_model.pkl', 'rb') as svm_model_file:
    svm_model = pickle.load(svm_model_file)

with open('rf_model.pkl', 'rb') as rf_model_file:
    rf_model = pickle.load(rf_model_file)

with open('XGBoost_classifier_model.pkl', 'rb') as XGB_model_file:
    XGB_model = pickle.load(XGB_model_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  
        data = pd.DataFrame(data, index=[0])
        gbc_prediction = gbc_model.predict(data)
        iforest_prediction = iforest_model.predict(data)
        knn_prediction = knn_model.predict(data)
        lr_prediction = lr_model.predict(data)
        svm_prediction = svm_model.predict(data)
        rf_prediction = rf_model.predict(data)
        XGB_prediction = XGB_model.predict(data)

        predictions = [gbc_prediction, iforest_prediction, knn_prediction, lr_prediction, svm_prediction, rf_prediction, XGB_prediction]
        voted_result = majority_vote(predictions)
        return jsonify({
            'voted_result': voted_result
        })

    except Exception as e:
        return jsonify({'error': str(e)})

def majority_vote(predictions):
    predictions = [int(pred[0]) for pred in predictions]
    predictions = [1 if pred == -1 else pred for pred in predictions]
    mode_prediction = statistics.mode(predictions)

    return [mode_prediction]

if __name__ == '__main__':
    app.run(debug=True)
