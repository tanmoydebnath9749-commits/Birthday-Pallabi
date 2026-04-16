import streamlit as st
from streamlit_confetti import confetti
import streamlit_lottie as st_lottie
import requests
import os
import base64
import time

# পেজ সেটিংস
st.set_page_config(page_title="Grand Surprise for Pallavi", page_icon="❤️", layout="centered")

# ১. মিউজিক ফাংশন (শুরু থেকে মেমোরি পর্যন্ত চলবে)
def get_audio_html(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            return f"""
                <audio autoplay loop id="bg-music">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
    return ""

# ২. কিউট অ্যানিমেশন লোড
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

panda_hi = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tiviy88S.json")
panda_dance = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_0mS9ID.json")
cute_cat = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tr1p44db.json")

# ৩. থিয়েটার পর্দা এবং জাদুকরী সিএসএস
st.markdown("""
    <style>
    .stApp { background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a1c4fd, #fbc2eb); background-size: 400% 400%; animation: gradient 15s ease infinite; }
    @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    
    /* থিয়েটার পর্দার অরিজিনাল অ্যানিমেশন */
    .curtain-container {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 9999; display: flex; overflow: hidden; pointer-events: none;
    }
    .curtain-left, .curtain-right {
        width: 50%; height: 100%;
        background: radial-gradient(circle, #b00 0%, #600 100%);
        box-shadow: inset 0 0 100px #000;
        transition: transform 3s cubic-bezier(0.7, 0, 0.3, 1);
        border: 2px solid #400;
    }
    .open-left { transform: translateX(-100%); }
    .open-right { transform: translateX(100%); }

    .happy-title { font-family: 'Dancing Script', cursive; color: white; font-size: 70px; text-align: center; text-shadow: 0 0 20px #ff1493; font-weight: bold; }
    .glass-box { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(15px); padding: 40px; border-radius: 30px; text-align: center; color: white; }
    </style>
    """, unsafe_allow_html=True)

# সেশন স্টেট (ধাপ নিয়ন্ত্রণ)
if 'step' not in st.session_state:
    st.session_state.step = 1

# মিউজিক কন্ট্রোল (প্রথম বাটন টিপলেই শুরু হবে)
if st.session_state.step > 1:
    st.markdown(get_audio_html("music.mp3"), unsafe_allow_html=True)

# --- ধাপ ১: শুরু (এখান থেকেই গান চালু হবে) ---
if st.session_state.step == 1:
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    if panda_hi: st_lottie.st_lottie(panda_hi, height=200)
    st.markdown("<h2>Hey Pallavi... ❤️</h2>", unsafe_allow_html=True)
    if st.button("Start the Surprise! ✨"):
        st.session_state.step = 2
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- ধাপ ২: থিয়েটার পর্দা খোলার বাটন ---
elif st.session_state.step == 2:
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    if cute_cat: st_lottie.st_lottie(cute_cat, height=200)
    st.markdown("<h2>Ready for the Grand Show? 🎭</h2>", unsafe_allow_html=True)
    if st.button("🎭 Open the Theatre Curtain"):
        st.session_state.step = 3
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- ধাপ ৩: মেইন সারপ্রাইজ (পর্দা সরা এবং সেলিব্রেশন) ---
elif st.session_state.step == 3:
    # এখানে পর্দা সরার অ্যানিমেশন রিয়েল-টাইমে দেখাবে
    st.markdown("""
        <div class="curtain-container">
            <div class="curtain-left open-left"></div>
            <div class="curtain-right open-right"></div>
        </div>
    """, unsafe_allow_html=True)
    
    # এরর ফ্রি কনফেটি এবং প্রচুর বেলুন
    confetti(emojis=['🎈', '💖', '🐼', '🎂', '✨'])
    st.balloons()
    
    st.markdown('<p class="happy-title">Happy Birthday, Pallavi! 🎂</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("pallavi.jpeg"):
            st.image("pallavi.jpeg", use_container_width=True)
        if panda_dance: st_lottie.st_lottie(panda_dance, height=250)

    st.markdown("<div class='glass-box'><h3>Happy Birthday dear..many many happy returns of the day...💗!❤️sobsomoy eivabei hasi khusi thak...💞ajker dinta enjoy kor....💖" "</h3></div>", unsafe_allow_html=True)
    
    st.write("#")
    if st.button("See Your Memories 📸"):
        st.session_state.step = 4
        st.rerun()

# --- ধাপ ৪: মেমোরিস (গান চলতেই থাকবে) ---
elif st.session_state.step == 4:
    st.markdown("<h2 style='text-align:center; color:white;'>📸 Our Sweet Memories</h2>", unsafe_allow_html=True)
    photos = ["pallavi2.jpeg", "pallavi3.jpeg", "pallavi4.jpeg", "pallavi5.jpeg"] 
    cols = st.columns(2)
    for idx, photo in enumerate(photos):
        if os.path.exists(photo):
            with cols[idx % 2]:
                st.image(photo, use_container_width=True, caption=f"Special Moment {idx+1}")
    
    if st.button("Back to Show ⬅️"):
        st.session_state.step = 3
        st.rerun()