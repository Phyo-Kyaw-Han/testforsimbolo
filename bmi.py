import streamlit as st

option = st.selectbox(
    "Unit",
    ("Metric Unit(Kg/M)", "Imperial Unit(lb/in)"))

weight =  st.number_input("Insert your weight",value=None, placeholder="Insert your weight...")
height =  st.number_input("Insert your height",value=None, placeholder="Insert your height...")

if st.button("Caculate",type="primary"):
    if option == "Metric Unit(Kg/M)":
        result = round(weight/pow(height,2),2)
        
    elif option == "Imperial Unit(lb/in)":
        result = round(weight/pow(height,2)*703,2)
    
    if result < 16:
        st.write(f"Your BMI is {result}.\n Your body weight is Severly Underweight")
        
    elif result > 16.1 and result <18.4:
        st.write(f"Your BMI is {result}.\n You body weight is Underweight")
        
    elif result > 18.5 and result <24.9:
        st.write(f"Your BMI is {result}.\n You body weight is Normal")
        
    elif result > 25.0 and result <29.9:
        st.write(f"Your BMI is {result}.\n You body weight is Overweight")
        
    elif result > 30.0 and result <34.9:
        st.write(f"Your BMI is {result}.\n You body weight is Moderately Overweight")
        
    elif result > 35.0 and result <39.9:
        st.write(f"Your BMI is {result}.\n You body weight is Severly Overweight")
        
    elif result > 40.0:
        st.write(f"Your BMI is {result}.\n You body weight is Morbidly Overweight")
        
    ##st.select_slider(
    ##"Range of Body Mass Index",
    ##options=["Severly Underweight", "Underweight", "Normal", "Overweight", "Moderately Obese", "Severly Obease", "Morbidly Obese"],
    ##value=(res))
    
st.button("Reset", type="primary")    
    
