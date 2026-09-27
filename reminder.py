import streamlit as st
import time
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pen Biting Reminder",
    page_icon="🖊️",
    layout="centered"
)

st.title("🖊️ Pen Biting Reminder")
st.write("A gentle audio reminder to keep your pen out of your mouth.")

# -----------------------------
# Settings
# -----------------------------
interval = st.number_input(
    "Reminder interval (seconds)",
    min_value=5,
    max_value=3600,
    value=30,
    step=5
)

message = st.text_input(
    "Reminder message",
    value="Please don't bite your pen."
)

# -----------------------------
# JavaScript audio reminder
# -----------------------------
def run_reminder(interval, message):

    # Browser Speech Synthesis
    html_code = f"""
    <script>
        let intervalSeconds = {interval};
        let message = {repr(message)};

        // Speak immediately
        function speakReminder() {{
            let speech = new SpeechSynthesisUtterance(message);
            speech.rate = 1.0;
            speech.pitch = 1.0;
            speech.volume = 1.0;

            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(speech);
        }}

        // Start timer
        speakReminder();

        setInterval(function() {{
            speakReminder();
        }}, intervalSeconds * 1000);
    </script>
    """

    components.html(html_code, height=50)


# -----------------------------
# Start / Stop buttons
# -----------------------------
if "running" not in st.session_state:
    st.session_state.running = False

col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start Reminder", use_container_width=True):
        st.session_state.running = True

with col2:
    if st.button("⏹️ Stop Reminder", use_container_width=True):
        st.session_state.running = False


# -----------------------------
# Run reminder
# -----------------------------
if st.session_state.running:

    st.success(f"🔔 Reminder is ON — every {interval} seconds")

    run_reminder(interval, message)

else:
    st.info("Reminder is OFF")

st.divider()

st.caption(
    "Keep this browser tab open while the reminder is running."
)