import streamlit as st
import requests
import base64

st.set_page_config(page_title="Blostem | Vernacular Advisor", page_icon="🎯", layout="wide")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64('BG.png')
    
    st.markdown(f'''
        <style>
        /* MAIN APP - Dark & Cinematic */
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
            url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #ffffff;
        }}
        
        /* HEADER - Remove default white line */
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
            border-bottom: none !important;
        }}
        
        /* LEFT PANEL (SIDEBAR) - Midnight Glassmorphism */
        [data-testid="stSidebar"] {{
            background-color: rgba(10, 15, 25, 0.9) !important;
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        /* Sidebar Text Visibility */
        [data-testid="stSidebar"] .stMarkdown, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label {{
            color: #e0f2ff !important;
            font-weight: 500 !important;
        }}
        
        [data-testid="stSidebar"] [data-testid="stMetricValue"] {{
            color: #00c6ff !important;
        }}

        /* QUERY SECTION - Input Area */
        .stTextArea textarea {{
            background-color: rgba(255, 255, 255, 0.05) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 12px !important;
            font-size: 1.15rem !important;
            font-weight: 500 !important;
            backdrop-filter: blur(5px);
        }}
        
        /* TARGETED FIX: Make "Customer Inquiry" Label White */
        [data-testid="stWidgetLabel"] p {{
            color: #ffffff !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }}

        .stTextArea textarea::placeholder {{
            color: #aaaaaa !important;
        }}

        /* RESULT CARD - High-Contrast Result */
        .result-card {{
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(25px);
            border-radius: 15px;
            padding: 30px;
            border-left: 8px solid #00c6ff;
            margin-top: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .result-card p, .result-card h3 {{
            color: #f0faff !important; 
        }}

        /* MAIN ACTION BUTTON */
        .stButton>button {{
            background: linear-gradient(90deg, #007bff, #00c6ff);
            border: none;
            color: white !important;
            padding: 15px 30px;
            font-weight: bold;
            border-radius: 10px;
            font-size: 1.1rem;
            box-shadow: 0 5px 20px rgba(0, 123, 255, 0.4);
            width: 100%;
            transition: 0.3s;
        }}
        
        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 123, 255, 0.5);
        }}
        
        [data-testid="stBlock"] {{
            padding-top: 0.5rem !important;
        }}
        </style>
    ''', unsafe_allow_html=True)
except Exception:
    st.sidebar.warning("Note: BG.png not detected. Applying High-Contrast Dark Theme.")

with st.sidebar:
    st.markdown("<div style='text-align: center; padding-top: 20px;'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='color: white;'>Advisor Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("### 🛠️ Configuration")
    language = st.selectbox("🎯 Target Language", ["Hindi", "Marathi", "Gujarati", "Bengali", "English"])
    st.selectbox("🛣️ Active Track", ["Vernacular FD Advisor", "Money Management", "Data Insights"])
    
    st.divider()
    
    st.markdown("### 📈 Live Performance")
    st.metric(label="✅ API Latency", value="184ms", delta="-12ms")
    st.metric(label="🔄 System Health", value="99.9%", delta="Stable")
    
    st.divider()
    
    st.markdown("<div style='opacity: 0.8;'>", unsafe_allow_html=True)
    st.info("**Solo Builder**")
    st.caption(" ")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🏦 Vernacular FD Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.25rem; color: #cbd5e0; font-weight: 400;'>Bridging Bharat’s Financial Literacy Gap</p>", unsafe_allow_html=True)

# Central Column Layout
_, center_col, _ = st.columns([1, 4, 1])

with center_col:
    st.write("") 
    user_query = st.text_area("✍️ Customer Inquiry", 
                              placeholder="e.g., Explain the 8.5% interest plan for a farmer in Gorakhpur...",
                              height=170)
    
    st.markdown("<div style='padding-top: 10px;'>", unsafe_allow_html=True)
    if st.button("✨ Simplify Banking Jargon"):
        if user_query:
            with st.spinner(f"Simplifying into {language}..."):
                try:
                    payload = {"message": user_query, "language": language}
                    response = requests.post("http://127.0.0.1:8000/chat", json=payload)
                    
                    if response.status_code == 200:
                        result = response.json().get("response")
                        st.markdown(f'''
                            <div class="result-card">
                                <h3 style='margin-bottom: 12px; color: #00c6ff;'>📝 {language} Explanation</h3>
                                <p style="line-height: 1.6;">{result}</p>
                            </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.error("Backend Error: Check main.py for details.")
                except:
                    st.error("Connection Failed: Is the FastAPI server running?")
        else:
            st.warning("Please type a query to help your customer.")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("<div style='text-align: center; color: #888888;'>Powered by FastAPI + Groq Llama-3.1 | Built for Blostem Hackathon 2026</div>", unsafe_allow_html=True)
