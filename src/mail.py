import streamlit as st
import smtplib
import time

def send_mail(sender: str, body: str, placeholder):
    if not sender or not body:
        placeholder.warning('Either sender or message is missing. Try again.')
        time.sleep(2)
        return

    # Ensure we are getting secrets properly
    try:
        email = st.secrets["email"]
        password = st.secrets["password"]
        target = st.secrets["target"]
    except KeyError:
        placeholder.error("Email credentials are missing! Set them in `.streamlit/secrets.toml`.")
        return

    # Check if placeholder is properly initialized
    if placeholder is None:
        st.error("Internal error: placeholder not initialized.")
        return

    try:
        with placeholder.container():  # Use a container to properly manage UI updates
            progress_bar = st.progress(0)
            time.sleep(1)
            conn = smtplib.SMTP('smtp.gmail.com', 587)
            progress_bar.progress(10)
            conn.ehlo()
            progress_bar.progress(30)
            conn.starttls()
            progress_bar.progress(50)
            conn.login(email, password)
            progress_bar.progress(70)
            conn.sendmail(email, target, f'Subject: From {sender}\n\n{body}')
            progress_bar.progress(90)
            conn.quit()
            progress_bar.progress(100)
            time.sleep(1)

        placeholder.success('Success! We will review your message, thanks!')
        time.sleep(3)
        placeholder.empty()  # Clear the placeholder after success

    except Exception as e:
        placeholder.error(f"Failed to send email: {e}")

def main():
    placeholder = st.empty()  # Properly define the placeholder

    placeholder.markdown(
        '''
        <h1 style="text-align:center;">Send Us a Message</h1>
        <hr>
        ''',
        unsafe_allow_html=True,
    )

    if 'message_count' not in st.session_state:
        st.session_state.message_count = 0

    sender = st.text_input('Sender', value='Anonymous')
    text = st.text_area('Message', key=f"message_{st.session_state.message_count}")

    if st.button('Send'):
        send_mail(sender, text, placeholder)  # Pass placeholder correctly
        st.session_state.message_count += 1  # Increment to refresh text input

if __name__ == '__main__':
    main()
