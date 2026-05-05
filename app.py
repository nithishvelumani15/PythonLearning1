import streamlit as st
import os
from dotenv import load_dotenv
from rag_chain import build_rag_chain

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="HR Assistant Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        justify-content: flex-end;
    }
    .assistant-message {
        background-color: #f5f5f5;
    }
    .message-content {
        max-width: 70%;
        word-wrap: break-word;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = build_rag_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "streamlit_session"

# Header
st.title("🤖 HR Assistant Chatbot")
st.markdown("---")
st.write("Welcome! Ask me anything about HR policies, benefits, and company information.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Session ID input
    st.session_state.session_id = st.text_input(
        "Session ID:",
        value=st.session_state.session_id,
        help="Enter a unique session ID to maintain conversation context"
    )
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.success("Chat history cleared!")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This HR Assistant uses:
    - **RAG (Retrieval-Augmented Generation)**
    - **Langchain** for LLM orchestration
    - **Google Gemini 2.5 Flash** as the LLM
    - **HuggingFace Embeddings** for document retrieval
    - **Chroma** as vector database
    """)

# Display chat history
st.markdown("### Conversation")
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-content">
                    <strong>You:</strong><br>{message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message assistant-message">
                <div class="message-content">
                    <strong>HR Assistant:</strong><br>{message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Input section
st.markdown("---")
col1, col2 = st.columns([0.85, 0.15])

with col1:
    user_input = st.text_input(
        "Your Question:",
        placeholder="Ask about HR policies, leave, benefits, etc...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", use_container_width=True, type="primary")

# Process user input
if send_button and user_input.strip():
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Show thinking indicator
    with st.spinner("HR Assistant is thinking..."):
        try:
            # Prepare input for RAG chain
            user_query_input = {"input": user_input}
            config = {"configurable": {"session_id": st.session_state.session_id}}
            
            # Get response from RAG chain
            response = st.session_state.rag_chain.invoke(
                user_query_input,
                config=config
            )
            
            # Add assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })
            
            # Rerun to display the new messages
            st.rerun()
            
        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")
            st.session_state.messages.pop()  # Remove the user message if there was an error

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8rem;'>
        <p>This chatbot is powered by RAG with Langchain | For HR Policy Inquiries Only</p>
    </div>
    """, unsafe_allow_html=True)
