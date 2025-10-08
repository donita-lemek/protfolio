import streamlit as st
from PIL import Image

# --- CONFIGURATION ---
PAGE_TITLE = "Donita Lemek | Data Scientist & Developer"
PAGE_ICON = "🌟"
NAME = "DONITA LEMEK"
DESCRIPTION = "Aspiring Data Scientist and Full-Stack Developer with a foundation in Data Analytics, MERN Stack, and Web Technologies. Interested in learning and exploring AI concepts."
EMAIL = "donitalemek@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/donita-lemek",
    "GitHub": "https://github.com/yourusername",
    "Portfolio (WIP)": "#", 
}
RESUME_FILE = "Resume .pdf" 

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered", initial_sidebar_state="collapsed") # Centered layout is better for small, elegant apps

# --- CUSTOM STYLING OVERHAUL ---
def local_css():
    """Injects custom CSS for a cute, elegant, and highly visible aesthetic."""
    ACCENT_COLOR = "#3498db"  # Soft Blue/Teal for primary emphasis
    TEXT_COLOR = "#2c3e50"    # Dark navy for high contrast
    BG_COLOR = "#ecf0f1"      # Very light gray/off-white background
    CARD_BG = "#ffffff"       # Pure white for content cards
    
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        /* General App Theme */
        html, body, [class*="stApp"] {{
            font-family: 'Poppins', sans-serif;
            background-color: {BG_COLOR}; 
            color: {TEXT_COLOR};
        }}
        
        /* Main Title Styling */
        h1 {{
            color: {TEXT_COLOR};
            font-weight: 700;
            font-size: 3em; /* Larger main title */
            margin-bottom: 0.1em;
        }}
        
        /* Section Header Styling */
        h2 {{
            color: {ACCENT_COLOR};
            font-weight: 700;
            font-size: 1.8em;
            border-bottom: 2px solid {ACCENT_COLOR};
            padding-bottom: 5px;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        
        /* Sub-Header Styling (Experience/Project Titles) */
        h3 {{
            color: {TEXT_COLOR};
            font-weight: 600;
            font-size: 1.25em;
            margin-bottom: 0.1em !important;
        }}
        
        /* Content Card Styling (for Projects/Experience) */
        .stExpander, .st-emotion-cache-1r6i0x {{
            background-color: {CARD_BG};
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
            border-left: 5px solid {ACCENT_COLOR}; /* Feature stripe */
        }}
        
        /* Caption/Date Styling */
        .stCaption {{
            color: #7f8c8d; /* Gray for dates/location */
            font-style: italic;
            margin-top: -5px;
            display: block;
        }}

        /* Footer Styling */
        .footer {{
            text-align: center; 
            font-size: small; 
            color: #7f8c8d; 
            padding-top: 20px;
            margin-top: 30px;
        }}
        
        /* Button Styling */
        .stDownloadButton > button {{
            background-color: {ACCENT_COLOR};
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }}
        .stDownloadButton > button:hover {{
            background-color: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}

        /* Hide the default Streamlit menu/footer/header */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)
    
# --- HEADER SECTION ---
def render_header():
    """Renders the main header, contact info, and summary."""
    st.title(NAME)
    st.markdown(f"**{DESCRIPTION}**")
    
    st.markdown(f"**📧 Email:** {EMAIL} | **📞 Phone:** +91 9400790480 | **📍 Location:** Wayanad, Kerala, India")

    # Social Media Links
    social_links = " | ".join([f"[{key}]({value})" for key, value in SOCIAL_MEDIA.items()])
    st.markdown(f"**🌐 Links:** {social_links}")
    
    st.markdown("---")

# --- EXPERIENCE SECTION ---
def render_experience():
    """Renders Professional Experience details."""
    st.header("💼 Professional Experience")

    # --- ProductByDesign ---
    st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
    st.subheader("Associate Data Scientist (Remote Internship) @ ProductByDesign")
    st.caption("Melbourne, Australia | August 2025 - Present")
    st.markdown("""
    - Built a **predictive dashboard** in SAP Analytics Cloud using time series forecasting.
    - Modeled and wrangled data for analysis; applied **Smart Predict** to forecast trends.
    - Visualized insights with interactive charts and KPIs to support business decisions.
    """)
    st.markdown('</div>', unsafe_allow_html=True) # End custom card

    # --- Kalkitech Ltd ---
    st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
    st.subheader("Software Development Engineer Intern (Hybrid Internship) @ Kalkitech Ltd")
    st.caption("Kochi, Kerala | December 2023 - August 2025")
    st.markdown("""
    - Developed a C-based **simulation tool** to improve substation safety protocols, reducing incidents through better risk management.
    - Built a **React UI** for enhanced accessibility and used data visualization for testing and performance validation.
    - Working on ML based projects to simulate phasor signals.
    """)
    st.markdown('</div>', unsafe_allow_html=True) # End custom card

    # --- AtithiGo ---
    st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
    st.subheader("Frontend Developer (Remote Internship) @ AtithiGo")
    st.caption("Kochi, Kerala | December 2024 - March 2025")
    st.markdown("""
    - Collaborated with a team of three developers to design and build the complete **front-end** for the AtithiGo hotel booking website.
    - Utilized modern front-end technologies to ensure a responsive and user-friendly design.
    - Focused on enhancing UI/UX for seamless navigation and booking experience.
    """)
    st.markdown('</div>', unsafe_allow_html=True) # End custom card
    
    st.markdown("---")

# --- PROJECTS SECTION ---
def render_projects():
    """Renders key projects using expandable sections for a clean look."""
    st.header("💡 Key Projects & Achievements")

    PROJECTS = [
        {
            "title": "Pill Management System (Pill Tracker)",
            "tech": "MERN Stack, MongoDB, Scanning Technology (e.g., OpenCV/QR Code)",
            "desc": "Developed a full-stack MERN application for tracking medication inventory. Features included **scanning pills** (via QR or image processing) to instantly record critical details like **expiry date**, dosage, usage instructions, and stock levels in a MongoDB backend. Designed for robust data management and user safety."
        },
        {
            "title": "Gold Price Prediction",
            "tech": "Python, XGBoost, Web Scraping, ETL",
            "desc": "Developed a gold price prediction pipeline using XGBoost, performing web scraping, exploratory data analysis (EDA), and ETL on historical and market datasets to maximize prediction accuracy."
        },
        {
            "title": "TRACER (Logistics Tracking System)",
            "tech": "GPS, Sensor Data, Predictive Modelling, Sentiment Analysis",
            "desc": "Created a logistics tracking system using GPS and sensor data to monitor containers in international waters. Improved supply chain efficiency with real-time tracking and optimized routing. Built a dashboard with **sentiment analysis** for port risk assessment."
        },
        {
            "title": "Church Management System",
            "tech": "Full-Stack: React, Flask, MongoDB",
            "desc": "Developed a full-stack web app to manage church records digitally (members, sacraments, families, events). Implemented secure login, dynamic forms, search, and reporting features."
        },
    ]

    for project in PROJECTS:
        # The styling for st.expander is customized via CSS for rounded corners and shadow
        with st.expander(f"**{project['title']}** - *{project['tech']}*"):
            st.markdown(project['desc'])
            
    st.markdown("---")

# --- SKILLS SECTION ---
def render_skills():
    """Renders technical skills categorized."""
    st.header("🛠️ Skills & Technologies")
    
    # Using 3 columns for density and readability
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        st.markdown("Python, R, C, C++, Java, Javascript, HTML, CSS, SQL")
        
    with col2:
        st.subheader("Data Science / ML")
        st.markdown("Scikit-learn, NumPy, Pandas, Matplotlib, Machine Learning, Statistical Modelling")

    with col3:
        st.subheader("Tools / Frameworks")
        st.markdown("Tableau, React, Flask, MongoDB, Express, Node.js, Hadoop, SAP Analytics Cloud")

    st.markdown("---")

# --- EDUCATION & LEADERSHIP SECTION ---
def render_education_leadership():
    """Renders education and leadership experience side-by-side."""
    st.header("📚 Education & Leadership")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Education")
        st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
        st.markdown("**BTech Computer Science & Engineering (Data Science)**")
        st.caption("Kalam Technical University, Mar Athanasius College of Engineering")
        st.markdown("Kothamangalam, Kerala | Expected June 2027")
        st.markdown("Cumulative GPA: **7.52/10**")
        st.markdown('</div>', unsafe_allow_html=True) # End custom card
        
    with col2:
        st.subheader("🚀 Leadership")
        st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
        st.markdown("**Campus Director @ Hult Prize MACE (2023-2025)**")
        st.markdown("""
        - Led the Hult Prize On-Campus Program with 100+ participants.
        - Organized community events to foster social impact-driven innovation.
        """)
        st.markdown('</div>', unsafe_allow_html=True) # End custom card
        
        st.markdown('<div class="st-emotion-cache-1r6i0x">', unsafe_allow_html=True) # Start custom card
        st.markdown("**Campus Lead @ TinkerHub MACE (2024-2025)**")
        st.markdown("""
        - Organized Kerala's largest women-exclusive hackathon, **Tink-Her-Hack** (100 participants).
        - Secured **Best Venue Award** among 63 venues in Kerala.
        """)
        st.markdown('</div>', unsafe_allow_html=True) # End custom card
        
    st.markdown("---")

# --- FOOTER SECTION ---
def render_footer():
    """Renders a simple, elegant footer."""
    st.markdown('<div class="footer">Built with Streamlit & Python | Donita Lemek | &copy; 2025</div>', unsafe_allow_html=True)


# --- MAIN APP EXECUTION ---
if __name__ == "__main__":
    local_css() # Inject custom CSS first
    
    render_header()
    render_experience()
    render_projects()
    render_skills()
    render_education_leadership()
    
    # Optional: Resume Download Button is placed prominently
    st.markdown("<br>", unsafe_allow_html=True)
    try:
        with open(RESUME_FILE, "rb") as pdf_file:
            st.download_button(
                label="Download Full Resume (PDF)",
                data=pdf_file,
                file_name=RESUME_FILE,
                mime="application/octet-stream",
            )
    except FileNotFoundError:
        st.warning(f"Note: To enable the download button, please ensure a file named '{RESUME_FILE}' is in the same directory as this script.")
        
    render_footer()
