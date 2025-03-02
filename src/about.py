import streamlit as st

def main(): 
    st.markdown(
        '''
        <h2 align="center">
            About Us
        </h2>

        ## The Team
        ''', 
        unsafe_allow_html=True, 
    )  

    col1, mid, col2 = st.columns([20, 1, 9])

    with col1:
        st.markdown(
            '''
            ### Anant Pratap Singh
                
            -  I'm currently learning about **Machine Learning**
            ##### Reach me
    
            <h5 align="center">
                <strong><a href="https://github.com/Warlord-K">Github</a></strong> |
                <strong><a href="https://www.linkedin.com/in/yatharth-gupta-012177228/">LinkedIn</a></strong>
            </h5> 
            <br> 
            <br>
            ''', 
            unsafe_allow_html=True,
        )

    with col2:
        st.image("https://drive.google.com/uc?export=view&id=1wQ_OG-5wnpDtPx4p0WFUwtcggb330ijl", width=260)

    col1, mid, col2 = st.columns([20, 1, 9])

    with col1:
        st.markdown(
            '''
            ### Meenal Sharma
            
            -  I'm currently learning about **Machine Learning**
             ##### Reach me

            <h5 align="center">
                <strong><a href="https://github.com/surya1176">Github</a></strong> |
                <strong><a href="https://www.linkedin.com/in/surya-karthikeya-327255228">LinkedIn</a></strong>
            </h5>
            <br> 
            <br> 
            ''', 
            unsafe_allow_html=True,
        )

    with col2:
        st.image("https://drive.google.com/uc?export=view&id=1wadp8dr8U-6c2VBBqNO3elltyDH1kmvh", width=260)

if __name__ == '__main__':
    main()
