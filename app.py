import streamlit as st
from recipe_query import FoodRecipeChat

st.title("ARIA: Assessing Risks of AI")

# Initialize the FoodRecipeChat instance
if "chat_instance" not in st.session_state:
    st.session_state.chat_instance = FoodRecipeChat()

# Display chat messages from FoodRecipeChat's history on app rerun
for message in st.session_state.chat_instance.messages:
    if message["role"] == "system":
        continue  # Skip system messages if you don't want to display them
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Use FoodRecipeChat to get the assistant's response
    assistant_response = st.session_state.chat_instance.food_recipe(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
