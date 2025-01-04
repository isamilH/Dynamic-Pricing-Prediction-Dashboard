

import streamlit as st
import pandas as pd
import joblib



# Load the trained model
model = joblib.load(r'D:\Users\tech\dynamic pricing\dynamic_pricing_model.pkl')

# App title
st.title("Dynamic Pricing Prediction Dashboard")

# Sidebar inputs
st.sidebar.header("Enter Ride Details:")
number_of_riders = st.sidebar.number_input("Number of Riders", min_value=1, value=50)
number_of_drivers = st.sidebar.number_input("Number of Drivers", min_value=1, value=25)
number_of_past_rides = st.sidebar.number_input("Number of Past Rides", min_value=0, value=10)
average_ratings = st.sidebar.slider("Average Ratings", min_value=1.0, max_value=5.0, value=4.5, step=0.1)
expected_ride_duration = st.sidebar.number_input("Expected Ride Duration (minutes)", min_value=1, value=60)
location_category = st.sidebar.selectbox("Location Category", ["Rural", "Suburban", "Urban"])
customer_loyalty_status = st.sidebar.selectbox("Customer Loyalty Status", ["Regular", "Silver"])
time_of_booking = st.sidebar.selectbox("Time of Booking", ["Morning", "Afternoon", "Evening", "Night"])
vehicle_type = st.sidebar.selectbox("Vehicle Type", ["Economy", "Premium"])

# Preprocess inputs
input_data = {
    "Number_of_Riders": number_of_riders,
    "Number_of_Drivers": number_of_drivers,
    "Number_of_Past_Rides": number_of_past_rides,
    "Average_Ratings": average_ratings,
    "Expected_Ride_Duration": expected_ride_duration,
    "Driver_to_Rider_Ratio": number_of_drivers / number_of_riders,
    "Cost_per_Minute": 0,  # Placeholder, calculated by model
    "Location_Category_Suburban": 1 if location_category == "Suburban" else 0,
    "Location_Category_Urban": 1 if location_category == "Urban" else 0,
    "Customer_Loyalty_Status_Regular": 1 if customer_loyalty_status == "Regular" else 0,
    "Customer_Loyalty_Status_Silver": 1 if customer_loyalty_status == "Silver" else 0,
    "Time_of_Booking_Evening": 1 if time_of_booking == "Evening" else 0,
    "Time_of_Booking_Morning": 1 if time_of_booking == "Morning" else 0,
    "Time_of_Booking_Night": 1 if time_of_booking == "Night" else 0,
    "Vehicle_Type_Premium": 1 if vehicle_type == "Premium" else 0,
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction
if st.sidebar.button("Predict Ride Cost"):
    prediction = model.predict(input_df)
    st.subheader("Predicted Ride Cost:")
    st.write(f"${prediction[0]:,.2f}")