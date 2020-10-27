import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb 
import pickle

# Load pickled XGBoost model
with open("../models/xgboost.pickle", "rb") as pfile:
    exec("xgboost = pickle.load(pfile)")
xg_clas = eval('xgboost')



alfreq = st.slider('% of Population Carrying Allele', float(0), float(2), 1.6) / 100
cadd = st.slider('CADD(RAW) Score', float(-6), float(45), float(2.74))
blosum = st.slider('BLOSUM62 Score', int(-4), int(11), int(0))
loftool = st.slider('LoFtool Score', float(0), float(1), float(0.34))
polyphen = st.selectbox('PolyPhen Category', ['Benign','Unknown','Possibly damaging','Probably damaging'])
sift = st.selectbox('SIFT Category', ['Tolerated','Likely Tolerated','Unknown','Likely Deleterious','Deleterious'])
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


pred_be = xg_clas.predict_proba(input_data)[0][0] * 100
pred_path = xg_clas.predict_proba(input_data)[0][2] * 100
pred_unc = xg_clas.predict_proba(input_data)[0][1] * 100

st.write(
f'Chance that the Variant is of Benign Consequence: {pred_be:.1f}%'
)
st.write(
f'Chance that the Variant is of Uncertain Consequence: {pred_unc:.1f}%'
)
st.write(
f'Chance that the Variant is of Pathogenic Consequence {pred_path:.2f}%'
)