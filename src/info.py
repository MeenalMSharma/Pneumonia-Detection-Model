import streamlit as st

def main():
    st.markdown(
        '''
        <h1 style="text-align:center;">About the Dataset</h1>
        <h2>What is Pneumonia?</h2>
        <p>Pneumonia is a lung infection that causes inflammation and fluid or pus in the air sacs of the lungs. 
        It can be caused by bacteria, viruses, or fungi.</p>
        
        <h2>About Dataset</h2>
        <p>This dataset contains 7022 images of human lungs' X-ray.</p>
        ''',
        unsafe_allow_html=True,  # Required to render HTML properly
    ) 

if __name__ == '__main__':
    main()
