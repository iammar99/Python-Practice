import streamlit as st

# Btn Functions

# Uppercase

def uppercase(str):
    return str.upper()

# Lowercase

def lowercase(str):
    return str.lower()

# Remove spaces

def remove_spaces(str):
    newText = ""
    for i in range(len(str)):
        if str[i] != " ":
            newText += str[i]
    return newText


# camelcase

def camelcase(str):
    newText = ""
    temp = ""
    for i in range(len(str)):
        if text[i] == " " and temp:
            newText += temp.capitalize() + " "
            temp = ""
        else:
            temp += text[i]
    newText += temp.capitalize()
    return newText


# Styling

st.markdown(
    """
<style>
.answer {
    font-size: 22px;
    font-weight: 600;
}
</style>
    """
,
unsafe_allow_html=True
)

st.write(
    """
    # TextUtiles
    ### You Can convert given string into lowercase or uppercase or remove blank spaces or count word and characters
    """
)

text = st.text_input("Try TextUtiles - Convert text to uppercase or lowercase.")
result = ""

col1, col2, col3, col4 = st.columns(4)


with col1:
                # Uppercase
    if st.button("Convert to Uppercase"):
        if text:  
            result = uppercase(text)  
        else:
            result = "Please enter some text."

with col2:

                # Lowercase
    if st.button("Convert to Lowercase"):
        if text: 
            result = lowercase(text) 
        else:
            result = "Please enter some text."

with col3:

                # Remove Spaces
    if st.button("Remove blank spaces"):
        if text: 
            result = remove_spaces(text) 
        else:
            result = "Please enter some text."
with col4:
    
                # Remove Spaces
    if st.button("Convert to camelcase"):
        if text: 
            result = camelcase(text) 
        else:
            result = "Please enter some text."


st.code(
    result
)



letter = len(text)
words = 0


#   For Counting Words

if text :
    words = 1
    for i in range(len(text) - 1):
        if text[i] == " " and text[i+1] != " " :
            words += 1


st.write(
    """
    ## Text Summary
    """
)

st.markdown(
    f'<div class="answer"> String contain {letter} letters and {words} Words </div>',
    unsafe_allow_html=True
)

