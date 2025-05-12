import streamlit as st

def main():
    # Title with custom HTML styling
    st.markdown(
        '''
        <h1 style="text-align:center;">
            <b><u>Pneumonia Detection Model</u></b>
        </h1>
        ''', 
        unsafe_allow_html=True  # Required to render HTML properly
    )

# Run the app
if __name__ == '__main__':
    main()
