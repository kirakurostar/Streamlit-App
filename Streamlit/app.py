import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from PIL import Image

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
    ["Home","Generalities About Web App Frameworks", "Setting Up and Using Streamlit", "Data Visualization", "Interactive Widgets", "Media Elements", "Deployment Guide", "Hosting Platforms"]
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
    st.image("Streamlit\images\Why-Should-You-Learn-Streamlit-in-2024.png")

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

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Created with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
