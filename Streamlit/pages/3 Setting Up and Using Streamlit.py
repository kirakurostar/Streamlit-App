
import streamlit as st

# Setting Up and Using Streamlit section
st.write("# Setting Up and Using Streamlit")

st.write("## Installation")
st.write("""
1. Install Python (if not already installed).
2. Install Streamlit using pip:`pip install streamlit`
""")

st.write("## Creating Your First App")
st.write("""
1. Open a new Python file (e.g., `app.py`).
2. Add the following code to display a title and some text:
```python
import streamlit as st
st.title("Hello, Streamlit!")
st.write("This is your first Streamlit app.")
```
3. Run the app using the command: `streamlit run app.py`
""")

st.write("## Adding Interactivity")
st.write("""
Use widgets like sliders and text inputs:
```python
name = st.text_input("What is your name?")
st.write(f"Hello, {name}!")

age = st.slider("How old are you?", 0, 100)
st.write(f"You are {age} years old.")
```
""")

st.write("## Exploring Streamlit Functions")
st.write("""
- `st.write()`: A versatile function for displaying text, data, or even Markdown content.
```python
st.write("Streamlit is amazing!", 42, [1, 2, 3])
st.write("Here's some **Markdown** text!")
```
- `st.sidebar`: Add a sidebar for extra functionality.
```python
option = st.sidebar.selectbox("Choose an option", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {option}")
```
- **Visualizations**: Create plots and charts effortlessly.
```python
import pandas as pd
import altair as alt

data = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
chart = alt.Chart(data).mark_line().encode(x='x', y='y')
st.altair_chart(chart, use_container_width=True)
```
""")