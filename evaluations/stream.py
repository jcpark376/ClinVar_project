'''
Code for Streamlit that allows users to alter the features.
Will output chance of DNA variation being benign vs pathogenic
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb 
import pickle

# Load pickled XGBoost model
with open("../models/xgboost.pickle", "rb") as pfile:
    exec("xgboost = pickle.load(pfile)")
xg_clas = eval('xgboost')

st.write('''
### DNA Variation Consequence Predictor
'''
)

# Sliders and drop-down menus
alfreq = st.slider('% of Population Carrying Allele', float(0), float(1), 0.5) / 100
cadd = st.slider('CADD(RAW) Score', float(-6), float(45), float(20))
blosum = st.slider('BLOSUM62 Score', int(-4), int(11), int(3))
loftool = st.slider('LoFtool Score', float(0), float(1), float(0.5))
polyphen = st.selectbox('PolyPhen Category', ['Benign','Unknown','Possibly damaging','Probably damaging'])
sift = st.selectbox('SIFT Category', ['Tolerated','Likely Tolerated','Unknown','Likely Deleterious','Deleterious'])
# Initilize the dictionary for the one-hot-encoded columns
poly_sift_dict = {
	'PolyPhen_benign': 0, 
	'PolyPhen_possibly_damaging': 0,
    'PolyPhen_probably_damaging': 0, 
	'PolyPhen_unknown': 0, 
	'SIFT_NaN': 0,
    'SIFT_deleterious': 0, 
	'SIFT_deleterious_low_confidence': 0, 
	'SIFT_tolerated': 0,
    'SIFT_tolerated_low_confidence': 0
}

# If user selects PolyPhen or SIFT values, update the dictionary
if polyphen == 'Benign':
	poly_sift_dict['PolyPhen_benign'] = 1
if polyphen == 'Unknown':
	poly_sift_dict['PolyPhen_unknown'] = 1
if polyphen == 'Possibly damaging':
	poly_sift_dict['Polyphen_possibly_damaging'] = 1
if polyphen == 'Probably damaging':
	poly_sift_dict['Polyphen_probably_damaging'] = 1


if sift == 'Tolerated':
	poly_sift_dict['SIFT_tolerated'] = 1
if sift == 'Likley Tolerated':
	poly_sift_dict['SIFT_tolerated_low_confidence'] = 1
if sift == 'Unknown':
	poly_sift_dict['SIFT_NaN'] = 1
if sift == 'Likley Deleterious':
	poly_sift_dict['SIFT_deleterious_low_confidence'] = 1
if sift == 'Deleterious':
	poly_sift_dict['SIFT_deleterious'] = 1

# Single-row dataframe representing user input of parameters
input_data = pd.DataFrame({
	'AF_ESP': [alfreq], 
	'AF_EXAC': [alfreq], 
	'AF_TGP': [alfreq], 
	'CADD_RAW': [cadd], 
	'BLOSUM62': [blosum], 
	'LoFtool': [loftool],
    'PolyPhen_benign': poly_sift_dict['PolyPhen_benign'], 
	'PolyPhen_possibly_damaging': poly_sift_dict['PolyPhen_possibly_damaging'],
    'PolyPhen_probably_damaging': poly_sift_dict['PolyPhen_probably_damaging'], 
	'PolyPhen_unknown': poly_sift_dict['PolyPhen_unknown'], 
	'SIFT_NaN': poly_sift_dict['SIFT_NaN'],
    'SIFT_deleterious': poly_sift_dict['SIFT_deleterious'], 
	'SIFT_deleterious_low_confidence': poly_sift_dict['SIFT_deleterious_low_confidence'], 
	'SIFT_tolerated': poly_sift_dict['SIFT_tolerated'],
    'SIFT_tolerated_low_confidence': poly_sift_dict['SIFT_tolerated_low_confidence']
	})


# Predict the probablities that DNA variant will be benign vs pathogenic. 
# Divide them by the sum
pred_be = xg_clas.predict_proba(input_data)[0][0] * 100
pred_path = xg_clas.predict_proba(input_data)[0][2] * 100

benign = pred_be / (pred_be + pred_path) * 100
patho = pred_path / (pred_be + pred_path) * 100

st.write(
f'Chance that the Variant is of Benign Consequence: {benign:.1f}%'
)

st.write(
f'Chance that the Variant is of Pathogenic Consequence {patho:.1f}%'
)
