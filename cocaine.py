import streamlit as st
import pandas as pd

# create a function to preprocess the user input
def preprocess_input(input_df):
    # Preprocess the input data as needed
    # Perform any necessary transformations or computations
    # Return the processed input data

    # Perform one-hot encoding on the 'Gender' variable
    gender_mapping = {
        'Female': [1, 0],
        'Male': [0, 1]
    }
    input_df['Gender_Female'], input_df['Gender_Male'] = zip(*input_df['Gender'].map(gender_mapping))
    input_df.drop('Gender', axis=1, inplace=True)
    
    # Additional preprocessing steps...
    
    # Return the processed input data
    return input_df

def predict_cocaine_user(input_data):
    # Perform the prediction based on the input data
    # Implement your prediction logic here
    # Return the prediction result

    # Example: Predict based on age, gender, and substance usage
    age = input_data['Age']
    gender_female = input_data['Gender_Female']
    gender_male = input_data['Gender_Male']
    amphet = input_data['Amphet']
    amyl = input_data['Amyl']
    benzos = input_data['Benzos']
    cannabis = input_data['Cannabis']
    coke = input_data['Coke']

    if age < 30 and gender_male == 1 and amphet > 0 and amyl > 0:
        return "This person is likely a cocaine user"
    elif age >= 30 and gender_male == 1 and benzos > 0 and cannabis > 0 and coke > 0:
        return "This person is likely a cocaine user"
    elif age >= 30 and gender_female == 0 and benzos > 0 and cannabis > 0:
        return "This person is likely a cocaine user"
    else:
        return "This person is not likely a cocaine user"


# define the input form
def input_form():
    age = st.slider('Age', 16, 75, 25)
    gender = st.radio('Gender', ['Female', 'Male'])
    amphet = st.selectbox('Amphet', [0, 1, 2, 3, 4, 5, 6])
    amyl = st.selectbox('Amyl', [0, 1, 2, 3, 4, 5, 6])
    benzos = st.selectbox('Benzos', [0, 1, 2, 3, 4, 5, 6])
    cannabis = st.selectbox('Cannabis', [0, 1, 2, 3, 4, 5, 6])
    coke = st.selectbox('Coke', [0, 1, 2, 3, 4, 5, 6])
    
    # create a dictionary of the input data
    input_data = {'Age': age,
                  'Gender': gender,
                  'Amphet': amphet,
                  'Amyl': amyl,
                  'Benzos': benzos,
                  'Cannabis': cannabis,
                  'Coke': coke}
    
    # convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])
    
    return input_df

# create the Streamlit app
def main():
    st.title('Cocaine User Prediction')

    # get the user input
    input_df = input_form()

    # preprocess the input
    input_df_processed = preprocess_input(input_df)

    # convert DataFrame to dictionary
    input_data = input_df_processed.to_dict(orient='records')[0]

    # make the prediction
    prediction = predict_cocaine_user(input_data)

    # display the prediction
    st.write(prediction)


if __name__ == '__main__':
    main()
