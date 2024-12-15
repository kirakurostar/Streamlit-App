import streamlit as st

# Deployment section
st.write("# Deployment")

st.write("## Streamlit Cloud")
st.write("""
Streamlit Cloud allows you to deploy your applications effortlessly.

**Steps to deploy:**
1. Push your code to a public GitHub repository.
2. Log in to Streamlit Cloud.
3. Connect your repository and select the main app file.
4. Your app will be live with a shareable link.
""")

st.write("## Other Hosting Options")
st.write("""
- **Heroku**: Use Heroku for more customizable deployment options.
- **Docker**: Package your app into a container for portability and scalability.
- **AWS/GCP/Azure**: Deploy your app for production-grade scalability.
""")

st.write("## Best Practices for Deployment")
st.write("""
- **Optimize Code**: Ensure efficient handling of large datasets or heavy computations.
- **Secure Sensitive Data**: Use environment variables to manage secrets like API keys.
- **Test Thoroughly**: Validate functionality on different devices and browsers.
""")
