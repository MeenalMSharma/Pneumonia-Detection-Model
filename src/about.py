import streamlit as st

def main():
    st.markdown(
        '''
        <h2 style="text-align:center;">About Us</h2>
        <h3 style="text-align:center;">The Team</h3>
        ''', 
        unsafe_allow_html=True
    )  

if __name__ == "__main__":
    main()

# Define the columns only once
col1, mid, col2 = st.columns([20, 1, 9])

# Person 1: Anant Pratap Singh
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
    st.image("https://via.placeholder.com/260", width=260)  # Replace with a valid image URL

# Add spacing
st.write("---")

# Person 2: Meenal Sharma
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
    st.image("https://via.placeholder.com/260", width=260)  # Replace with a valid image URL


if __name__ == '__main__':
    main()
