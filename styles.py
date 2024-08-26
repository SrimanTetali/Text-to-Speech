import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
            body {
                background-color: #121212; /* Dark background */
                color: #ffffff; /* White text */
            }

            h1 {
                color: #ffcc00; /* Bright color for title */
            }

            textarea {
                background-color: #1e1e1e; /* Darker text area */
                color: #ffffff; /* White text */
                border: 1px solid #ffcc00; /* Yellow border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px; /* Inner padding */
                width: 100%; /* Full width */
                resize: none; /* Disable resizing */
            }

            button {
                background-color: #ffcc00; /* Yellow button */
                color: #121212; /* Dark text on button */
                border: none; /* No border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px 20px; /* Padding */
                cursor: pointer; /* Pointer cursor */
                transition: background-color 0.3s; /* Smooth transition */
            }

            button:hover {
                background-color: #e6b800; /* Darker yellow on hover */
            }

            audio {
                margin-top: 20px; /* Margin for audio player */
            }
        </style>
    """, unsafe_allow_html=True)
