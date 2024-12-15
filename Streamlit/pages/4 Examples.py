import streamlit as st
import pandas as pd
import altair as alt

# Examples of Applications section
st.write("# Examples of Applications")

st.write("## Application Ideas")

st.write("""
- **Interactive Dashboards**: Monitor real-time data with filters and charts that users can manipulate interactively.
- **Machine Learning Demos**: Allow users to upload files, tweak model parameters, and view predictions instantly.
- **Custom Reports**: Generate interactive reports that combine text, visuals, and user inputs for dynamic exploration of data.
- **Educational Tools**: Create tools for teaching concepts, such as physics simulations or data processing workflows.
- **Product Prototypes**: Rapidly build and test user-facing prototypes for feedback collection.
""")

st.write("## Code Example for a Dashboard")

st.code("""
import streamlit as st
import pandas as pd
import altair as alt

# Create data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Values': [23, 45, 56]
})

# Plot data
st.title("Dashboard Example")
st.bar_chart(data)
st.write("A simple bar chart to visualize data.")
""", language='python')
