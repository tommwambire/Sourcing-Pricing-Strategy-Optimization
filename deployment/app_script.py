
import numpy as np
import pandas as pd
import streamlit as st 
from sklearn import preprocessing
import pickle

model = pickle.load(open('model_final', 'rb'))
#encoder_dict = pickle.load(open('encoder.pkl', 'rb')) 
cols=['Provinces', 'category', 'commodity', 'year', 'month']
wholesale_df = pd.read_csv('wholesale_df.csv')
wholesale_encoded = pd.read_csv('wholesale_encoded.csv')

  
def main():
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url("fruits_veg.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
    )


    st.title("Global Harvest Co")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Price Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    province_name = st.selectbox("Province", wholesale_df['Provinces'].unique())

    filtered_df = wholesale_df[wholesale_df['Provinces'] == province_name]

    food_categories = filtered_df['category'].unique()
    
    food_category = st.selectbox("Food Category", food_categories)

    filtered_df = filtered_df[filtered_df['category'] == food_category]

    food_commodity = st.selectbox("Food Commodity", filtered_df['commodity'].unique())
    year = st.number_input("Year", min_value=2015, max_value=2030, value=2024, step=1)
    month = st.number_input("Month", min_value=0, max_value=12, value=5, step=1)

    if st.button("Predict"):
        prediction_data_dict = {
                'Provinces' : province_name,
                'category' : food_category,
                'commodity' : food_commodity,
                'year' : year,
                'month' : month
            }
        
        commodities_info = {}
        keys_to_skip = ['year', 'month']

        feature_columns = list(wholesale_encoded.drop(['price/unit(KSH)'], axis=1).columns)

        for feature in feature_columns:
            commodities_info[feature] = 0

        for key, value in prediction_data_dict.items():
            if key not in keys_to_skip:
                element = key + "_" + value
                if element in feature_columns:
                    commodities_info[element] = 1 

        # Add 'year' and 'month' to the commodities_info dictionary
        commodities_info['year'] = prediction_data_dict.get('year', 0)
        commodities_info['month'] = prediction_data_dict.get('month', 0)

        # Convert commodities_info to a DataFrame
        commodities_data = pd.DataFrame.from_dict(commodities_info, orient='index').T

        # Predict using the model
        predicted = model.predict(commodities_data)

        st.success(f"{round(predicted[0], 2)} KSH")


    
if __name__=='__main__': 
    main()