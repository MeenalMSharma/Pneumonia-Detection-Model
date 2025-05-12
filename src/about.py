import streamlit as st
from PIL import Image

def main():
    # Title and header
    st.markdown(
        '''
        <h2 style="text-align:center;">About Us</h2>
        <h3 style="text-align:center;">The Team</h3>
        ''', 
        unsafe_allow_html=True
    )  

    # --- Person 1: Anant Pratap Singh ---
    col1, mid, col2 = st.columns([20, 1, 9])

    with col1:
        st.markdown("### Anant Pratap Singh")
        st.markdown("- I'm currently learning about **Machine Learning**")
        st.markdown("##### Reach me")
        
        # HTML for links
        st.markdown(
            '''
            <div style="text-align:center;">
                <strong><a href="https://github.com/Warlord-K" target="_blank">Github</a></strong> |
                <strong><a href="https://www.linkedin.com/in/yatharth-gupta-012177228/" target="_blank">LinkedIn</a></strong>
            </div>
            ''', 
            unsafe_allow_html=True
        )

    with col2:
        img = Image.open("test_files/A.jpeg")
        st.image(img, width=260)

    # Add spacing
    st.write("---")

    # --- Person 2: Meenal Sharma ---
    col1, mid, col2 = st.columns([20, 1, 9])  # Define columns again

    with col1:
        st.markdown("### Meenal Sharma")
        st.markdown("- I'm currently learning about **Machine Learning**")
        st.markdown("##### Reach me")

        # HTML for links
        st.markdown(
            '''
            <div style="text-align:center;">
                <strong><a href="https://github.com/surya1176" target="_blank">Github</a></strong> |
                <strong><a href="https://www.linkedin.com/in/surya-karthikeya-327255228" target="_blank">LinkedIn</a></strong>
            </div>
            ''', 
            unsafe_allow_html=True
        )

    with col2:
        img2 = Image.open("test_files/M.jpeg")
        st.image(img2, width=260)


# Run the app
if __name__ == '__main__':
    main()
