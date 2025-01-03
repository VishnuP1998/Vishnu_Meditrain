import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# Load Lottie Animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Add custom CSS for styling
def add_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #f0f8ff;
        }
        .main {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4b0082;
            text-align: center;
            font-family: 'Arial', sans-serif;
            animation: fadeIn 2s ease-in-out;
        }
        .stButton > button {
            background-color: #4caf50;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)

# Main function to set up the app
def main():
    # Add custom CSS
    add_custom_css()
    
    # Display Lottie Animation
    st_lottie(
        load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json"),
        speed=1,
        reverse=False,
        loop=True,
        height=300
    )

    # Title with custom styling
    st.markdown("""
    <div style="background-color: #ff7f50; padding: 10px; border-radius: 10px;">
        <h1>MEDITRAIN PROJECT AI BOT</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("Any Queries, Sir?")

    # Initialize session state for storing conversation history
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Input text box for the user
    user_query = st.text_input("Your Query:", placeholder="Ask something...")

    # Submit button
    if st.button("Ask"):
        if user_query:
            # Simulate a loading spinner
            with st.spinner("Processing..."):
                time.sleep(1)  # Simulate processing time

            # Prepare the payload for the POST request
            payload = {"query": user_query}

            try:
                # Make the POST request to the API endpoint
                response = requests.post("https://vishnu-meditrain.onrender.com/response", json=payload)

                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()

                    # Extract and display the chatbot response
                    bot_response = data.get("response", "No response found.")

                    # Save the conversation to session state
                    st.session_state["conversation"].append(
                        {"user": user_query, "bot": bot_response}
                    )
                else:
                    st.error(
                        f"Error {response.status_code}: Unable to get a response from the API."
                    )
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query before sending.")

    # Display the conversation history
    st.write("### Conversation History")
    for chat in st.session_state["conversation"]:
        st.markdown(f"""
        <div style="background-color: #00008B;color: #ffffff; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
            <strong>You:</strong> {chat['user']}<br>
            <strong>DR AI:</strong> {chat['bot']}
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
