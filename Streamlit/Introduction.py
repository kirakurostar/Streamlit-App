#conda activate streamlitenv

#streamlit run app.py
import streamlit as st

# Title of the presentation with custom dark mode styling
st.markdown(
    """
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #11111;
            text-align: left;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title with a centered style
st.markdown('<p class="title">Web App Frameworks: An Introduction to Streamlit</p>', unsafe_allow_html=True)

# Introduction section
st.header("Introduction")
st.write(""" 
Welcome to this presentation on web app frameworks, with a special focus on Streamlit. 
By the end of this session, you will understand what web app frameworks are, their general uses and accessibility, 
and how to set up and use Streamlit to create interactive web applications.
""")
