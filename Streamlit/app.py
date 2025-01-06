import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from PIL import Image
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="Streamlit Presentation",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page", 
    ["Home","Generalities About Web App Frameworks", "Setting Up and Using Streamlit", "Interactive Widgets", "Media Elements", "Data Exploration", "Data Visualization", "Deployment Guide", "Hosting Platforms", "Quiz"]
)

# Main content
if page == "Home":
    st.title("Welcome to Streamlit Presentation App")
    st.write("""
    This app demonstrates various Streamlit functionalities.
    Navigate through different pages using the sidebar.
    """)
    
    # Progress bar example
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    st.success("Loading complete!")
    
    # Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Presented By")
        st.write("**Hany El Atlassi**")
        st.write("**Bahiya Cheikh Mohamed Fadel**")
        st.write("**Adam BelBaraka**")
    with col2:
        st.header("Supervised By")
        st.write("**Mr. Azmi Mohammed**")
    with col3:
        st.header("Chapter Id")
        st.write("**Chapter 15**")

elif page == "Generalities About Web App Frameworks":
    
    # Generalities About Web App Frameworks section
    st.write("# Generalities About Web App Frameworks")

    st.write("## What Are Web App Frameworks?")
    st.write("""
    Web app frameworks are software libraries designed to simplify the development of web applications. 
    They provide tools, templates, and pre-built components that allow developers to focus on building functionality 
    rather than starting from scratch.
    """)
    st.image("Streamlit/images/Why-Should-You-Learn-Streamlit-in-2024.png")

    st.write("##  Popular Frameworks")
    st.write("""
    Some popular frameworks include:
    - **Flask**: A lightweight and flexible Python framework for building simple or complex applications.
    - **Django**: A high-level Python framework focused on rapid development and clean design.
    - **Streamlit**: A framework specifically designed for creating data-driven and interactive web apps with minimal effort.
    """)


    st.write("## Usages")
    st.write("""
    - **Building Web Applications**: From personal projects to enterprise-level solutions.
    - **Data Visualization and Analysis**: Displaying charts, graphs, and dashboards.
    - **APIs**: Hosting services that communicate between different applications.
    """)

    st.write("## Accessibility")
    st.write("""
    Web app frameworks often:
    - Have extensive documentation and active community support.
    - Simplify deployment to the web.
    - Require varying levels of coding expertise, with some (like Streamlit) being beginner-friendly.
    """)



elif page == "Setting Up and Using Streamlit":
    
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
elif page == "Data Exploration":
    st.title("Data Exploration with Streamlit")
    
    st.markdown("""
    This section demonstrates how to load, explore, and visualize datasets using 
    Streamlit's features. We'll focus on analyzing log files and creating 
    interactive visualizations.
    """)
    
    # 1. File Upload Section
    st.header("1. Upload a Log File")
    st.markdown("""
    Upload your CSV file containing log data. The app will display a preview 
    and provide various analysis options.
    """)
    
    uploaded_file = st.file_uploader("Upload a log file (CSV format)", type="csv")
    
    if uploaded_file is not None:
        try:
            # Reading the log file
            df = pd.read_csv(uploaded_file)
            
            # Basic file information
            st.success("File successfully uploaded!")
            st.info(f"Number of records: {len(df)}")
            st.info(f"Number of columns: {len(df.columns)}")
            
            # Preview of the data
            st.subheader("Preview of the log data")
            st.dataframe(df.head())
            
            # 2. Log File Summary
            st.header("2. Log File Summary")
            
            # Numeric summary
            st.subheader("Numeric Data Summary")
            st.write(df.describe())
            
            # Column information
            st.subheader("Column Information")
            col_info = pd.DataFrame({
                'Data Type': df.dtypes,
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum(),
                'Unique Values': df.nunique()
            })
            st.dataframe(col_info)
            
            # 3. Data Visualization
            st.header("3. Data Visualization")
            
            # Select visualization type
            viz_type = st.selectbox(
                "Choose visualization type",
                ["Histogram", "Bar Chart", "Line Chart", "Box Plot"]
            )
            
            # Select column to visualize
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            categorical_columns = df.select_dtypes(include=['object']).columns
            
            if viz_type in ["Histogram", "Box Plot"]:
                selected_column = st.selectbox(
                    "Choose a numeric column to visualize",
                    numeric_columns
                )
            else:
                selected_column = st.selectbox(
                    "Choose a column to visualize",
                    df.columns
                )
            
            # Create visualization
            fig = plt.figure(figsize=(10, 6))
            
            if viz_type == "Histogram":
                plt.hist(df[selected_column].dropna(), bins=20, 
                        color='skyblue', edgecolor='black')
                plt.title(f"Histogram of {selected_column}")
                plt.xlabel(selected_column)
                plt.ylabel("Frequency")
                
            elif viz_type == "Bar Chart":
                value_counts = df[selected_column].value_counts()[:20]  # Top 20 values
                plt.bar(value_counts.index, value_counts.values, 
                       color='skyblue', edgecolor='black')
                plt.xticks(rotation=45)
                plt.title(f"Bar Chart of {selected_column}")
                plt.xlabel(selected_column)
                plt.ylabel("Count")
                
            elif viz_type == "Line Chart":
                if st.checkbox("Use date/time index"):
                    date_columns = df.select_dtypes(include=['datetime64']).columns
                    if len(date_columns) > 0:
                        date_column = st.selectbox("Select date column", date_columns)
                        df.set_index(date_column, inplace=True)
                plt.plot(df[selected_column], color='skyblue')
                plt.title(f"Line Chart of {selected_column}")
                plt.xticks(rotation=45)
                
            elif viz_type == "Box Plot":
                plt.boxplot(df[selected_column].dropna())
                plt.title(f"Box Plot of {selected_column}")
                plt.ylabel(selected_column)
            
            st.pyplot(fig)
            
            # 4. Data Filtering
            st.header("4. Data Filtering")
            
            # Column selection for filtering
            filter_column = st.selectbox(
                "Choose a column to filter",
                df.columns,
                key='filter_column'
            )
            
            # Value selection for filtering
            unique_values = df[filter_column].dropna().unique()
            selected_values = st.multiselect(
                "Select values to filter by",
                unique_values
            )
            
            if selected_values:
                filtered_df = df[df[filter_column].isin(selected_values)]
                st.write(f"Filtered data ({len(filtered_df)} records):")
                st.dataframe(filtered_df)
                
                # Export filtered data
                if st.button("Export Filtered Data"):
                    csv = filtered_df.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name="filtered_data.csv",
                        mime="text/csv"
                    )
            
            # 5. Advanced Analysis
            st.header("5. Advanced Analysis")
            
            # Correlation matrix for numeric columns
            if len(numeric_columns) > 1:
                st.subheader("Correlation Matrix")
                corr_matrix = df[numeric_columns].corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                plt.imshow(corr_matrix, cmap='coolwarm', aspect='auto')
                plt.colorbar()
                plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
                plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
                st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            
    else:
        st.info("Please upload a CSV file to begin analysis")
    
    # Additional information and tips
    st.sidebar.header("Tips")
    st.sidebar.markdown("""
    - Make sure your CSV file is properly formatted
    - Large files may take longer to process
    - Use the filtering options to focus on specific data
    - Export filtered data for further analysis
    """)

elif page == "Data Visualization":
    st.title("Data Visualization Examples")
    
    # Generate sample data
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # Different plot types
    st.subheader("Line Chart")
    st.line_chart(df)
    
    st.subheader("Area Chart")
    st.area_chart(df)
    
    st.subheader("Bar Chart")
    st.bar_chart(df)
    
    # Plotly chart
    st.subheader("Plotly Scatter Plot")
    fig = px.scatter(df, x='A', y='B', color='C')
    st.plotly_chart(fig)

elif page == "Interactive Widgets":
    st.title("Interactive Widgets")
    
    # Text input
    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")
    
    # Slider
    age = st.slider("Select your age", 0, 100, 25)
    st.write(f"Your age is {age}")
    
    # Checkbox
    if st.checkbox("Show/Hide"):
        st.write("You can see this text now!")
    
    # Select box
    option = st.selectbox(
        "Choose an option",
        ["Option 1", "Option 2", "Option 3"]
    )
    st.write(f"You selected: {option}")
    
    # Radio button
    genre = st.radio(
        "What's your favorite movie genre",
        ["Comedy", "Drama", "Documentary"]
    )
    st.write(f"You selected: {genre}")
    
    # Multi-select
    options = st.multiselect(
        "What are your favorite colors",
        ["Red", "Green", "Blue", "Yellow"],
        ["Blue"]
    )
    st.write(f"You selected: {options}")

elif page == "Media Elements":
    st.title("Media Elements")
    
    # Image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Video upload
    video_file = st.file_uploader("Choose a video...", type=["mp4", "mov"])
    if video_file is not None:
        st.video(video_file)
    
    # Audio upload
    audio_file = st.file_uploader("Choose an audio...", type=["mp3", "wav"])
    if audio_file is not None:
        st.audio(audio_file)
elif page == "Deployment Guide":
    st.title("Deployment Guide for Streamlit Apps")
    
    st.header("1. Streamlit Cloud Deployment")
    st.markdown("""
    ### Steps for Streamlit Cloud
    1. **Prepare Your Repository**
        - Push your code to GitHub
        - Ensure you have requirements.txt
        - Main app file (usually app.py)
        
    2. **Deploy on Streamlit Cloud**
        ```bash
        # Requirements.txt example
        streamlit==1.24.0
        pandas==1.5.3
        numpy==1.24.3
        plotly==5.15.0
        Pillow==9.5.0
        ```
        
    3. **Deployment Steps**
        - Visit [share.streamlit.io](https://share.streamlit.io)
        - Connect your GitHub account
        - Select your repository
        - Choose main file
        - Click Deploy
    """)
    
    st.header("2. Local Deployment")
    st.code("""
    # Run locally
    streamlit run app.py
    
    # Run on specific port
    streamlit run app.py --server.port 8501
    
    # Run with specific server address
    streamlit run app.py --server.address 0.0.0.0
    """)
    
    st.header("3. Docker Deployment")
    st.code("""
    # Dockerfile
    FROM python:3.9-slim
    
    WORKDIR /app
    
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    
    COPY . .
    
    EXPOSE 8501
    
    CMD ["streamlit", "run", "app.py"]
    """)
    
    st.markdown("""
    ### Docker Commands
    ```bash
    # Build image
    docker build -t streamlit-app .
    
    # Run container
    docker run -p 8501:8501 streamlit-app
    ```
    """)
    
    st.header("4. Production Considerations")
    st.markdown("""
    - Set up proper error handling
    - Implement caching for better performance
    - Use session state for user data
    - Configure authentication if needed
    - Set up monitoring and logging
    - Consider scaling options
    """)

elif page == "Hosting Platforms":
    st.title("Web App Hosting Platforms Comparison")
    
    st.header("1. Streamlit Cloud")
    st.markdown("""
    - **Pros:**
        - Free tier available
        - Direct GitHub integration
        - Specifically designed for Streamlit
        - Easy deployment process
    - **Cons:**
        - Limited resources in free tier
        - Less flexibility compared to other platforms
    """)
    
    st.header("2. Heroku")
    st.markdown("""
    ### Deployment Steps
    1. Create Procfile:
    ```
    web: sh setup.sh && streamlit run app.py
    ```
    
    2. Create setup.sh:
    ```bash
    mkdir -p ~/.streamlit/
    echo "\
    [server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    \n\
    " > ~/.streamlit/config.toml
    ```
    
    3. Deploy using Heroku CLI:
    ```bash
    heroku create
    git push heroku main
    ```
    
    - **Pros:**
        - Well-established platform
        - Good documentation
        - Supports multiple languages
    - **Cons:**
        - No longer offers free tier
        - Can be expensive for larger apps
    """)
    
    st.header("3. AWS Elastic Beanstalk")
    st.markdown("""
    ### Deployment Steps
    1. Install EB CLI
    2. Initialize EB application:
    ```bash
    eb init -p python-3.9 streamlit-app
    eb create streamlit-env
    ```
    
    - **Pros:**
        - Highly scalable
        - Full AWS service integration
        - Professional-grade infrastructure
    - **Cons:**
        - More complex setup
        - Can be costly
        - Steeper learning curve
    """)
    
    st.header("4. Google Cloud Platform")
    st.markdown("""
    ### App Engine Deployment
    ```yaml
    # app.yaml
    runtime: python39
    entrypoint: streamlit run app.py --server.port $PORT
    
    instance_class: F1
    
    automatic_scaling:
      target_cpu_utilization: 0.65
      min_instances: 1
      max_instances: 10
    ```
    
    - **Pros:**
        - Good free tier
        - Excellent scaling capabilities
        - Strong security features
    - **Cons:**
        - Complex pricing structure
        - Configuration can be challenging
    """)
    
    st.header("5. DigitalOcean")
    st.markdown("""
    ### Deployment with Docker
    1. Create Droplet
    2. Install Docker
    3. Deploy container:
    ```bash
    docker-compose up -d
    ```
    
    - **Pros:**
        - Simple pricing
        - Good performance
        - Easy to use
    - **Cons:**
        - Manual setup required
        - Less managed services
    """)
    
    st.header("6. Railway.app")
    st.markdown("""
    - **Pros:**
        - Simple deployment
        - GitHub integration
        - Free tier available
        - Good for small projects
    - **Cons:**
        - Limited customization
        - Resource constraints
    """)
    
    st.header("Cost Comparison")
    
    cost_data = {
        'Platform': ['Streamlit Cloud', 'Heroku', 'AWS EB', 'GCP', 'DigitalOcean', 'Railway'],
        'Free Tier': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
        'Starting Price': ['$0', '$7/mo', '$0', '$0', '$5/mo', '$0'],
        'Enterprise Ready': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }
    
    df_cost = pd.DataFrame(cost_data)
    st.dataframe(df_cost)
    
    st.header("Choosing the Right Platform")
    st.markdown("""
    Consider these factors:
    1. **Budget**: What's your monthly hosting budget?
    2. **Scale**: Expected user base and traffic
    3. **Technical Expertise**: Your team's technical capabilities
    4. **Features Needed**: Authentication, databases, etc.
    5. **Geographic Requirements**: User location and latency
    6. **Maintenance**: Time available for maintenance
    7. **Support**: Need for professional support
    """)
    
    st.info("""
    💡 **Tip**: Start with Streamlit Cloud for simple apps and migrate to more robust 
    solutions as your needs grow.
    """)
elif page == "Quiz":
    st.title("🧠 Test Your Knowledge: Streamlit Quiz")

    # Introduction
    st.write("""
    This quiz will test your understanding of Streamlit concepts, syntax, and best practices.  
    Answer the questions below and see how well you've mastered the material!
    """)

    # Question 1
    st.subheader("1. What is Streamlit primarily used for?")
    q1 = st.radio(
        "Select the correct answer:",
        ["Choose an option", 
        "Building mobile applications", 
        "Creating data-driven and interactive web apps", 
        "Developing backend APIs", 
        "Game development"]
    )
    if q1 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q1 == "Creating data-driven and interactive web apps":
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect. Streamlit is used for building data-driven and interactive web apps.")

    # Question 2
    st.subheader("2. Which function is used to display a dataframe in Streamlit?")
    q2 = st.radio(
        "Choose the correct function:",
        ["Choose an option", "st.write()", "st.dataframe()", "st.table()", "st.display()"]
    )
    if q2 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q2 == "st.dataframe()":
        st.success("✅ Correct! st.dataframe() is designed specifically for displaying dataframes.")
    else:
        st.error("❌ Incorrect. The correct answer is st.dataframe().")

    # Question 3
    st.subheader("3. Which Streamlit widget allows users to select numeric values?")
    q3 = st.selectbox(
        "Pick the correct widget:",
        ["Choose an option", "st.radio()", "st.slider()", "st.checkbox()", "st.text_input()"]
    )
    if q3 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q3 == "st.slider()":
        st.success("✅ Correct! st.slider() lets users select numeric or date ranges.")
    else:
        st.error("❌ Incorrect. The correct answer is st.slider().")

    # Question 4
    st.subheader("4. What are the benefits of using Streamlit?")
    q4 = st.multiselect(
        "Select all that apply:",
        [
            "Simple and quick to set up",
            "Requires extensive front-end coding",
            "Interactive widgets with minimal effort",
            "Data visualization made easy",
            "Compatible only with JavaScript"
        ]
    )
    if not q4:
        st.warning("⚠ Please select at least one answer.")
    elif set(q4) == {"Simple and quick to set up", "Interactive widgets with minimal effort", "Data visualization made easy"}:
        st.success("✅ Correct! Streamlit is simple, interactive, and great for data visualization.")
    else:
        st.error("❌ Incorrect. The correct answers are: Simple and quick to set up, Interactive widgets with minimal effort, and Data visualization made easy.")

    # Question 5
    st.subheader("5. Which function is used to add a text box for user input?")
    q5 = st.radio(
        "Choose the correct function:",
        ["Choose an option", "st.button()", "st.text_input()", "st.radio()", "st.write()"]
    )
    if q5 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q5 == "st.text_input()":
        st.success("✅ Correct! st.text_input() is used to add a text box for user input.")
    else:
        st.error("❌ Incorrect. The correct answer is st.text_input().")

    # Question 6
    st.subheader("6. True or False: Streamlit apps require extensive knowledge of HTML, CSS, and JavaScript.")
    q6 = st.radio(
        "Select your answer:",
        ["Choose an option", "True", "False"]
    )
    if q6 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q6 == "False":
        st.success("✅ Correct! Streamlit simplifies web app development without needing front-end expertise.")
    else:
        st.error("❌ Incorrect. The correct answer is False.")

    # Question 7
    st.subheader("7. What does st.markdown() do?")
    q7 = st.radio(
        "Select the best answer:",
        ["Choose an option", 
        "Runs a Python script", 
        "Displays formatted text using Markdown", 
        "Adds a button to the app", 
        "Creates a sidebar"]
    )
    if q7 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q7 == "Displays formatted text using Markdown":
        st.success("✅ Correct! st.markdown() is used to display Markdown-formatted text.")
    else:
        st.error("❌ Incorrect. The correct answer is: Displays formatted text using Markdown.")

    # Question 8
    st.subheader("8. Which file format is required to run a Streamlit app?")
    q8 = st.radio(
        "Choose the correct answer:",
        ["Choose an option", "HTML", "Python (.py)", "JavaScript (.js)", "JSON"]
    )
    if q8 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q8 == "Python (.py)":
        st.success("✅ Correct! Streamlit apps are written in Python and use .py files.")
    else:
        st.error("❌ Incorrect. The correct answer is Python (.py).")

    # Question 9
    st.subheader("9. Which function is used to create a sidebar in Streamlit?")
    q9 = st.radio(
        "Select the correct function:",
        ["Choose an option", "st.write()", "st.sidebar()", "st.text_input()", "st.plot()"]
    )
    if q9 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q9 == "st.sidebar()":
        st.success("✅ Correct! st.sidebar() is used to create a sidebar.")
    else:
        st.error("❌ Incorrect. The correct answer is st.sidebar().")

    # Question 10
    st.subheader("10. Which function is used to display a large title in Streamlit?")
    q10 = st.radio(
        "Select the correct function:",
        ["Choose an option", "st.write()", "st.header()", "st.title()"]
    )
    if q10 == "Choose an option":
        st.warning("⚠ Please choose an answer.")
    elif q10 == "st.title()":
        st.success("✅ Correct! st.title() is used for large titles.")
    else:
        st.error("❌ Incorrect. Try again!")

    # Final Score
    st.success("🎉 Quiz Complete! How did you do? If you’d like to improve, revisit the topics and try again.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Created with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)