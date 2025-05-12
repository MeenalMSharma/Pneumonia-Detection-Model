import streamlit as st

def main():
    # Title with custom HTML styling
    st.markdown(
        '''
        <h1 style="text-align:center;">
            <b><u>PreCare Disease Detection Model</u></b>
        </h1>
        ''', 
        unsafe_allow_html=True
    )
    
    # Introduction section
    st.markdown(
        '''
        <h2><b>Introduction</b></h2>
        <p>PreCare is an advanced machine learning and deep learning-based solution designed to assist healthcare professionals in diagnosing critical diseases early through medical imaging. The system leverages cutting-edge technologies like Convolutional Neural Networks (CNN) to detect life-threatening conditions, helping to reduce diagnosis time and improve treatment outcomes. It provides accurate predictions and valuable insights for early intervention, ensuring patients receive timely care.</p>
        <br>
        ''', 
        unsafe_allow_html=True
    )

    # Diseases Targeted section
    st.markdown(
        '''
        <h2><b>Which Diseases are Targeted?</b></h2>
        <p>The PreCare Disease Detection Model focuses on two critical diseases that significantly impact public health:</p>
        <ul>
            <li><b>Pneumonia</b>: Pneumonia is a severe respiratory infection that causes inflammation of the air sacs in the lungs. Early detection is crucial for effective treatment. The PreCare model helps identify pneumonia from chest X-ray images, allowing for quicker and more accurate diagnosis. The system differentiates between normal and pneumonia-affected lungs, making it a valuable tool for healthcare professionals.</li>
            <li><b>Brain Tumor</b>: Brain tumors are abnormal growths in the brain that can have serious health consequences. Timely detection is critical to prevent further complications. PreCare uses deep learning models to analyze MRI scans of the brain, identifying tumors and their characteristics with high precision. This model assists radiologists in diagnosing brain tumors early, aiding in prompt medical intervention.</li>
        </ul>
        <br>
        ''',
        unsafe_allow_html=True
    )

    # Objectives section
    st.markdown(
        '''
        <h2><b>Objectives</b></h2>
        <p>The main objectives of the PreCare Disease Detection Model are:</p>
        <ul>
            <li><b>Early Detection</b>: To provide accurate and rapid diagnosis of pneumonia and brain tumors, facilitating timely medical intervention.</li>
            <li><b>Improved Accuracy</b>: Leverage advanced deep learning techniques to achieve high levels of diagnostic accuracy, reducing human error.</li>
            <li><b>Enhanced Accessibility</b>: Provide healthcare professionals with an easy-to-use tool for disease detection, making AI-powered diagnosis accessible in both urban and rural healthcare facilities.</li>
            <li><b>Supporting Radiologists</b>: Assist radiologists and clinicians by providing additional insights and improving decision-making processes.</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )

# Run the app
if __name__ == '__main__':
    main()
