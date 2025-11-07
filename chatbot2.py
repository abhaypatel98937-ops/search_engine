from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate  # Changed from PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

# 1. Load Environment Variables
load_dotenv()

# 2. Set the Streamlit App Title
st.title("New AI Bot")

# 3. Define the Prompt and LLM Chain
prompt = ChatPromptTemplate.from_messages([  # Changed to ChatPromptTemplate
    ("system", "You are a helpful assistant that helps people find information."),
    ("user", "Question: {question}")
])

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()
chain = prompt | model | parser  # LCEL chain

# 4. Create the User Input Box with a key for better state management
input_text = st.text_input("Ask your question:", key="user_input")

# 5. Invoke the Chain and Display the Result
if input_text:
    with st.spinner('Thinking...'):
        try:
            response = chain.invoke({'question': input_text})
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Optional: Add a clear button
if st.button("Clear"):
    st.session_state.user_input = ""
    st.rerun()
