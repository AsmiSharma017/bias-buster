import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests
import random



# --- PAGE CONFIG ---

st.set_page_config(
    page_title="Bias Buster — AI Response Checker",
    layout="wide"
)
# --- PARTICLE BACKGROUND ---
st.markdown("""
<div id="tsparticles" style="position: fixed; width: 100%; height: 100%; z-index: -1;"></div>
<script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>
<script>
tsParticles.load("tsparticles", {
  background: {
    color: { value: "#000000" }
  },
  fpsLimit: 60,
  particles: {
    number: { value: 80, density: { enable: true, area: 800 } },
    color: { value: ["#ffffff", "#ff69b4"] },  // white + pink
    shape: { type: "star" },
    opacity: { value: 0.8 },
    size: { value: { min: 1, max: 3 } },
    move: { enable: true, speed: 1.2 }
  },
  interactivity: {
    events: { onHover: { enable: true, mode: "repulse" } },
    modes: { repulse: { distance: 100, duration: 0.4 } }
  },
  detectRetina: true
});
</script>
""", unsafe_allow_html=True)

# --- CUSTOM CSS FOR COLORFUL BACKGROUND & ANIMATION ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
        animation: gradientBG 10s ease infinite;
        min-height: 100vh;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .main {
        background: rgba(255,255,255,0.85);
        border-radius: 18px;
        padding: 2.5rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.25);
    }
    h1, h2, h3 {
        color: #ff5858 !important;
    }
    .stTextArea textarea {
        background: #fff7e6 !important;
        border-radius: 10px !important;
        font-size: 1.15em !important;
        color: #222 !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #36d1c4 0%, #5b86e5 100%);
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-size: 1.1em;
        box-shadow: 0 2px 8px rgba(91,134,229,0.18);
        transition: 0.2s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #5b86e5 0%, #36d1c4 100%);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- LOTTIE ANIMATION ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json")

# --- FUN FACTS ---
fun_facts = [
    "🤖 Did you know? The first chatbot, ELIZA, was created in the 1960s.",
    "🌍 AI bias can arise from the data it's trained on—always check your sources!",
    " The word 'algorithm' comes from a Persian mathematician, Al-Khwarizmi.",
    "⚖️ Bias detection is crucial for ethical AI development.",
    "💡 Even AI models can learn to be less biased with the right training!"
]

# --- LAYOUT ---
col1, col2 = st.columns([2, 3])
with col1:
    st_lottie(lottie_ai, speed=1, height=220, key="ai")
    st.markdown("### 💡 Fun Fact")
    st.info(random.choice(fun_facts))
    st.markdown("---")

with col2:
    st.title("Bias Buster — AI Response Checker")
    st.write("Paste any AI‑generated response; we detect bias and suggest neutral wording.")

    text = st.text_area("🤖 Paste the AI Response:", height=200, placeholder="Paste your AI-generated text here...")

    if st.button("Detect Bias"):
        if not text.strip():
            st.warning("Please paste some text to analyze.")
        else:
            with st.spinner("Analyzing with Gemini…"):
                prompt = f"""
You are an AI‑ethics expert. Analyse the text for bias or toxicity.
Return:
1. 'Biased' or 'Neutral'
2. Explanation of detected bias
3. A neutral rewrite

Text:
{text}
"""
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.success("✅ Analysis complete!")
                st.markdown("### 🏷️ **Bias Status:**")
                st.markdown(response.text)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(
    """
    <hr>
    <center>
    <small>
    Powered by Google Gemini | <a href="https://github.com/your-repo" target="_blank">GitHub</a>
    </small>
    </center>
    """, unsafe_allow_html=True
)
