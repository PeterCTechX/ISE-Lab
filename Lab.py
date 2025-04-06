import streamlit as st
from google import genai
from google.genai.types import HttpOptions

# Set up Vertex AI Gemini API client

client = genai.Client(http_options=HttpOptions(api_version="v1"))

# Streamlit UI
st.title("Find Your Neighboring States")
users_state = st.text_input("Enter your U.S. state:")

# Section A: Vertex AI Gemini API call
def get_neighboring_states(state):
    prompt = f"What U.S. states border {state}? Just list the state names separated by commas."
    try:
        response = client.models.generate_content(
            model="gemini-2.0-pro",  # or "gemini-2.0-flash-001" for faster responses
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

neighboring_states = ""
if users_state:
    neighboring_states = get_neighboring_states(users_state)
# End of Section A

# Section B: Output to the user
st.write("The neighboring states are:")
if neighboring_states:
    st.success(neighboring_states)
# End of Section B
