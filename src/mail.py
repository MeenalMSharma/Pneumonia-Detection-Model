import streamlit as st
import smtplib
import time
import os


def send_mail(sender: str, body: str, placeholder):
    if not sender or not body:
        placeholder.warning('Either sender or message is missing. Try again.')
        time.sleep(2)
        return

    # Load credentials safely
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    target = os.getenv('TARGET')

    if not email or not password or not target:
        try:
            email = st.secrets["email"]
            password = st.secrets["password"]
            target = st.secrets["target"]
        except KeyError:
            placeholder.error("Email credentials are missing! Add them to `.streamlit/secrets.toml`.")
            return

    try:
        with placeholder.progress(0) as progress:
            time.sleep(1)
            conn = smtplib.SMTP('smtp.gmail.com', 587)
            progress.progress(10)
            conn.ehlo()
            progress.progress(20)
            conn.starttls()
            progress.progress(40)
            conn.login(email, password)
            progress.progress(60)
            conn.sendmail(email, target, f'Subject: From {sender}\n\n{body}')
            progress.progress(80)
            conn.quit()
            progress.progress(100)
            time.sleep(1)

        placeholder.success('Success! Your message has been sent.')
        time.sleep(3)
        placeholder.empty()

    except smtplib.SMTPAuthenticationError:
        placeholder.error("Failed to authenticate. Check your email and password.")
    except Exception as e:
        placeholder.error(f"Failed to send email: {e}")


def main():
    placeholder = st.empty()

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
        send_mail(sender, text, placeholder)
        st.session_state.message_count += 1  # Refresh text input after sending


if __name__ == '__main__':
    main()
