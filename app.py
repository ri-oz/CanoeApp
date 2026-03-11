import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Canoe Trip RSVP", page_icon="🛶", layout="centered")

# --- CUSTOM CSS FOR RETRO VIBE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    html, body, [class*='css'] {
        font-family: 'Press Start 2P', cursive;
    }
    
    /* Make headers pop with arcade colors */
    h1, h2, h3 {
        color: #e94560 !important;
        text-shadow: 2px 2px 0px #000000;
    }
    
    /* Style the main background */
    .stApp {
        background-color: #1a1a2e;
        color: #ffffff;
    }
    
    /* Style the success text */
    .st-emotion-cache-10trblm {
        color: #4ecca3;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
# This allows the app to "remember" button clicks
if 'boat' not in st.session_state:
    st.session_state.boat = None
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = None

# --- HEADER ---
st.title("🛶 PLAYER SELECT")
st.write("Welcome to the official Canoe Trip Lobby. Please configure your loadout below.")

# --- STEP 1: PLAYER NAME ---
st.header("1. ENTER PLAYER NAME")
player_name = st.text_input("Gamer Tag / Real Name", placeholder="e.g. River King")

# --- STEP 2: VESSEL SELECTION ---
st.header("2. CHOOSE YOUR VESSEL")
col1, col2 = st.columns(2)

with col1:
    # Make sure "kanoe-roto-viking (1).jpg" is in the same folder as this Python script
    st.image("kanoe-roto-viking (1).jpg", use_container_width=True)
    st.subheader("Crimson Cruiser")
    st.write("**Class:** Heavy Canoe")
    st.write("**Capacity:** 3 Players")
    st.write("**Stat:** High Cargo, Low Speed")
    if st.button("SELECT CRIMSON"):
        st.session_state.boat = "Crimson Cruiser"

with col2:
    # Make sure "kajak-vista.jpg" is in the same folder
    st.image("kajak-vista.jpg", use_container_width=True)
    st.subheader("Orange Outlaw")
    st.write("**Class:** Rapid Kayak")
    st.write("**Capacity:** 2 Players")
    st.write("**Stat:** High Speed, Low Cargo")
    if st.button("SELECT ORANGE"):
        st.session_state.boat = "Orange Outlaw"

# Show currently selected boat
st.info(f"**Current Vessel:** {st.session_state.boat if st.session_state.boat else 'None Selected'}")

# --- STEP 3: DIFFICULTY SELECTION ---
st.header("3. SELECT DIFFICULTY")
d_col1, d_col2, d_col3 = st.columns(3)

with d_col1:
    if st.button("EASY"):
        st.session_state.difficulty = "Easy"
    st.caption("Lazy River Float. Snacks included.")

with d_col2:
    if st.button("NORMAL"):
        st.session_state.difficulty = "Normal"
    st.caption("Steady Paddling. A light workout.")

with d_col3:
    if st.button("HARDCORE"):
        st.session_state.difficulty = "Hardcore"
    st.caption("White Water Rush. Prepare to get wet.")

# Show currently selected difficulty
st.info(f"**Current Difficulty:** {st.session_state.difficulty if st.session_state.difficulty else 'None Selected'}")

# --- SUBMIT SECTION ---
st.markdown("---")
if st.button("JOIN LOBBY", type="primary", use_container_width=True):
    # Form Validation
    if not player_name:
        st.error("❌ ERROR: Player Name required!")
    elif not st.session_state.boat:
        st.error("❌ ERROR: Please select a vessel!")
    elif not st.session_state.difficulty:
        st.error("❌ ERROR: Please select a difficulty!")
    else:
        # Success Action
        st.success(f"🎉 SUCCESS! **{player_name}** has joined the lobby with the **{st.session_state.boat}** on **{st.session_state.difficulty}** mode!")
        st.balloons()