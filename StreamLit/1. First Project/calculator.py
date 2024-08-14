import streamlit  as st


# Styling

st.markdown(
    """
        <style>
            .answer{
                    background-color: #262730;
                    color: white;
                    font-size: x-large;
                    font-weight: 800;
                    border-radius: 10px;
                    padding: 10px;
            }
        </style>
    """,
    unsafe_allow_html=True
)



st.write("""
         # First Calculator
         """)

first_number = st.slider("Pick First number", 0, 100)


second_number = st.slider("Pick Second number", 0, 100)



option = st.selectbox(
    'Select Operation to be performed',
    ('Addition ', 'Subtraction', 'Multiplication' , 'Division'))




# Condition to display in button

if option == "Addition ":
    btnText = "Add"
elif option == "Subtraction":
    btnText = "Subtract"
elif option == "Multiplication":
    btnText = "Multiply"
else :
    btnText = "Divide"



# Button function to calculate 

def click_button():
    if option == "Addition ":
        st.markdown(f'<div class="answer">The result of {first_number} + {second_number} = {first_number + second_number}</div>',
        unsafe_allow_html=True)
    elif option == "Subtraction":
        st.markdown(
            f'<div class="answer">The result of {first_number} - {second_number} = {first_number - second_number}</div>',
            unsafe_allow_html=True
        )
    elif option == "Multiplication":
        st.markdown(
            f'<div class="answer">The result of {first_number} * {second_number} = {first_number * second_number}</div>',
            unsafe_allow_html=True
        )
    else :
        if second_number != 0:
            st.markdown(
                f'<div class="answer">The result of {first_number} / {second_number} = {first_number / second_number}</div>',
                unsafe_allow_html=True  
            )
        else :
            st.markdown(
            f'<div class="answer">Error :- Number cannot be divided by zero</div>',
            unsafe_allow_html=True
        )


st.button(btnText, on_click=click_button)