import pandas as pd
from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
	req 				= request.get_json()
	input_data 			= req['data']
	input_data_df 		= pd.DataFrame.from_dict(input_data)

	feat_obj			= joblib.load('feats.pkl')
	scale_obj 			= joblib.load('scale.pkl')
	ohe_obj 			= joblib.load('ohe.pkl')
	model 				= joblib.load('model.pkl')

	input_data_scaled 	= pd.DataFrame(scale_obj.transform(input_data_df[feat_obj['num_cols']]), columns=feat_obj['num_cols'])
	input_data_ohe 		= pd.DataFrame(ohe_obj.transform(input_data_df[feat_obj['cat_cols']]).toarray(), columns=feat_obj['cat_ohe_cols'])
	input_data_bin 		= input_data_df[feat_obj['bin_cols']]
	input_data_df 		= pd.concat((input_data_bin,input_data_scaled,input_data_ohe), axis=1)

	prediction 			= model.predict(input_data_df)

	if prediction[0] == 1:
		result = 'Принято'
	else:
		result = 'Отказ'

	return jsonify({'output':{'result':result}})

@app.route('/')
def home():
	return 'Система прогнозирования'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='3000')