import streamlit as st
from UI_settings import page_config

page_config() # Avoid malfunctions by set page configurations after you import streamlit

def function_1():
    st.write("This is a template")

if __name__ == "__main__":
    function_1()