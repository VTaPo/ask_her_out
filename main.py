import streamlit as st

def main():
    st.set_page_config(page_title="Special Invitation", layout="wide")

    # Custom CSS for pink background and cute font
    st.markdown(
        """
        <style>
        .stApp {
            background-color: pink;
        }
        .cute-font {
            font-family: 'Comic Sans MS', cursive;
            font-size: 24px;
            color: #FF69B4;
            text-align: center;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .cute-button {
            font-family: 'Comic Sans MS', cursive;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 15px;
            border: none;
            cursor: pointer;
            background-color: #90EE90;
            color: white;
        }
        .gif-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .gif-container img {
            max-width: 200px;
            height: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'page' not in st.session_state:
        st.session_state.page = 'invitation'

    if st.session_state.page == 'invitation':
        show_invitation_page()
    elif st.session_state.page == 'video':
        show_video_page()

def show_invitation_page():
    st.markdown('<p class="cute-font">đi chơi với mình ngày mai nhé, bạn cuti cuti</p>', unsafe_allow_html=True)
    
    # Display the cute gif
    st.image("https://res.cloudinary.com/vtphong/image/upload/v1728570706/ask%20her%20out/giphy_goout.gif", use_column_width=True)
    
    # Create button container
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    # Yes button
    if st.button("Yes", key="yes_button", help="Click to accept", use_container_width=False):
        st.session_state.page = 'video'
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_video_page():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col1:
        st.image("https://res.cloudinary.com/vtphong/image/upload/v1728570706/ask%20her%20out/giphy_heart.gif")
    
    with col2:
        st.image("https://res.cloudinary.com/vtphong/image/upload/v1728571415/ask%20her%20out/giphy_multi_heart.gif")
    
    with col3:
        st.image("https://res.cloudinary.com/vtphong/image/upload/v1728570705/ask%20her%20out/giphy_pink_heart.gif")

if __name__ == "__main__":
    main()
