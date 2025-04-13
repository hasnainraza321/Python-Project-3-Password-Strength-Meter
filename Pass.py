import streamlit as st 
import re

# Set page title and icon
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

# App title
st.title("🔏 Password Strength Checker")

# Welcome message
st.markdown("""
## Welcome to Password Strength Checker! ✊  
Use this simple tool to check the strength of your password.
""")

# Corrected text_input (type=...)
password = st.text_input("Enter your password:", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else: 
        feedback.append("❌ Password should have at least one uppercase and one lowercase letter.")
    
    if re.search(r'\d', password):  # Corrected \d for digit
        score += 1
    else:
        feedback.append("❌ Password should have at least one digit.")

    if re.search(r'[!@#$*]', password):  # Corrected regex and quote placement
        score += 1
    else:
        feedback.append("❌ Password should have at least one special character (!@#$*).")

    # Score-based messages
    if score == 4:
        st.success("💹 Your password is strong!")

    elif score == 3:
        feedback.append("😒 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")

    # Display suggestions
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter a password to check its strength.")
