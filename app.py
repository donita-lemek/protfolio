import streamlit as st

# --- CONFIGURATION ---
PAGE_TITLE = "Donita Lemek | Data Scientist & Developer"
PAGE_ICON = "" 
NAME = "DONITA LEMEK"
DESCRIPTION = "Aspiring Data Scientist and Full-Stack Developer with a foundation in Data Analytics, MERN Stack, and Web Technologies. Focused on AI concepts and practical application development."
EMAIL = "donitalemek@gmail.com"
RESUME_FILE = "Resume .pdf" 

# Social media links displayed below header
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/donita-lemek",
    "GitHub": "https://github.com/yourusername",
    "Portfolio (WIP)": "#", 
}

# Set page configuration with a dynamic, centered layout
st.set_page_config(page_title=PAGE_TITLE, layout="centered", initial_sidebar_state="collapsed") 

# --- CUSTOM STYLING OVERHAUL (Dynamic, Glassmorphism-Inspired Dark Mode) ---
def local_css():
    """Injects custom CSS for a modern, dynamic, and minimalist aesthetic with a dark theme."""
    ACCENT_COLOR = "#FFC300"  # Modern Gold/Orange accent
    SECONDARY_ACCENT = "#D4AC0D" # Darker gold
    TEXT_COLOR = "#F0F0F0"    # Near-white text for high readability
    BG_COLOR = "#121212"      # Deep dark gray base background
    CARD_BG = "#1C1C1C"       # Slightly Lighter Dark Gray for Content Cards
    
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        /* General App Theme - Dynamic Dark Mode with Gradient */
        html, body, [class*="stApp"] {{
            font-family: 'Poppins', sans-serif;
            background: radial-gradient(circle at top left, #1f2f47 0%, {BG_COLOR} 65%);
            color: {TEXT_COLOR};
            max-width: 800px; /* Slightly wider for better desktop presentation */
        }}
        
        /* Main Title Styling */
        h1 {{
            color: {ACCENT_COLOR}; /* Gold accent for the name */
            font-weight: 700;
            font-size: 3.5em; /* Larger name */
            margin-bottom: 0.1em;
            letter-spacing: 1px;
        }}
        
        /* Section Header Styling - Clean and Understated */
        h2 {{
            color: {TEXT_COLOR};
            font-weight: 700;
            font-size: 1.8em;
            border-bottom: 2px solid {SECONDARY_ACCENT}; /* Thinner, gold underline */
            padding-bottom: 8px;
            margin-top: 45px;
            margin-bottom: 25px;
        }}
        
        /* Sub-Header Styling (Titles) */
        h3 {{
            color: {ACCENT_COLOR};
            font-weight: 600;
            font-size: 1.3em;
            margin-bottom: 0.1em !important;
        }}
        
        /* Caption/Metadata (Dates/Location) */
        .stCaption {{
            color: #AAAAAA; 
            font-style: italic;
            margin-top: -5px;
            display: block;
        }}
        
        /* Content Card Styling (Floating/Glass effect) */
        .content-card, .stExpander {{
            background-color: {CARD_BG};
            border-radius: 8px; /* Softer rounded corners */
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); /* Stronger, modern shadow */
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle white border for depth */
        }}
        
        /* Footer Styling */
        .footer {{
            text-align: center; 
            font-size: small; 
            color: #777777; 
            padding-top: 20px;
            margin-top: 40px;
        }}
        
        /* Button Styling - Accent Color */
        .stDownloadButton > button {{
            background-color: {ACCENT_COLOR};
            color: {BG_COLOR}; 
            border-radius: 4px;
            padding: 12px 25px;
            font-weight: 700;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }}
        .stDownloadButton > button:hover {{
            background-color: {SECONDARY_ACCENT};
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        }}

        /* Hiding Streamlit chrome for minimal look */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)
    
# --- HEADER SECTION ---
def render_header():
    """Renders the main header, contact info, and summary."""
    st.title(NAME)
    # Using markdown for Description and contact info to leverage the CSS text color
    st.markdown(f"**{DESCRIPTION}**")
    
    st.markdown(f"*Email:* {EMAIL} | *Phone:* +91 9400790480 | *Location:* Wayanad, Kerala, India")

    # Social Media Links
    social_links = " | ".join([f"[{key}]({value})" for key, value in SOCIAL_MEDIA.items()])
    st.markdown(f"**Links:** {social_links}")
    
    st.markdown("---") # Simple markdown divider

# --- EXPERIENCE SECTION ---
def render_experience():
    """Renders Professional Experience details."""
    st.header("PROFESSIONAL EXPERIENCE")

    # Experience details are wrapped in content-card for the floating effect
    
    # --- ProductByDesign ---
    st.markdown('<div class="content-card">', unsafe_allow_html=True) 
    st.subheader("Associate Data Scientist (Remote Internship) @ ProductByDesign")
    st.caption("Melbourne, Australia | August 2025 - Present")
    st.markdown("""
    - Built a **predictive dashboard** in SAP Analytics Cloud using time series forecasting.
    - Modeled and wrangled data for analysis; applied **Smart Predict** to forecast trends.
    - Visualized insights with interactive charts and KPIs to support business decisions.
    """)
    st.markdown('</div>', unsafe_allow_html=True) 

    # --- Kalkitech Ltd ---
    st.markdown('<div class="content-card">', unsafe_allow_html=True) 
    st.subheader("Software Development Engineer Intern (Hybrid Internship) @ Kalkitech Ltd")
    st.caption("Kochi, Kerala | December 2023 - August 2025")
    st.markdown("""
    - Developed a C-based **simulation tool** to improve substation safety protocols, reducing incidents through better risk management.
    - Built a React UI for enhanced accessibility and used data visualization for testing and performance validation.
    - Working on ML based projects to simulate phasor signals.
    """)
    st.markdown('</div>', unsafe_allow_html=True) 

    # --- AtithiGo ---
    st.markdown('<div class="content-card">', unsafe_allow_html=True) 
    st.subheader("Frontend Developer (Remote Internship) @ AtithiGo")
    st.caption("Kochi, Kerala | December 2024 - March 2025")
    st.markdown("""
    - Collaborated with a team of three developers to design and build the complete **front-end** for the AtithiGo hotel booking website.
    - Utilized modern front-end technologies to ensure a responsive and user-friendly design.
    - Focused on enhancing UI/UX for seamless navigation and booking experience.
    """)
    st.markdown('</div>', unsafe_allow_html=True) 
    
    st.markdown("---")

# --- PROJECTS SECTION ---
def render_projects():
    """Renders key projects using expandable sections for a clean look."""
    st.header("KEY PROJECTS & ACHIEVEMENTS")

    PROJECTS = [
        {
            "title": "Pill Management System (Pill Tracker)",
            "tech": "MERN Stack, MongoDB, Scanning Technology (e.g., OpenCV/QR Code)",
            "desc": "Developed a full-stack MERN application for tracking medication inventory. Features included **scanning pills** to instantly record critical details like **expiry date**, dosage, usage instructions, and stock levels in a MongoDB backend. Designed for robust data management and user safety."
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
        # st.expander is styled as a floating card
        with st.expander(f"**{project['title']}** - *{project['tech']}*"):
            st.markdown(project['desc'])
            
    st.markdown("---")

# --- SKILLS SECTION ---
def render_skills():
    """Renders technical skills categorized."""
    st.header("SKILLS & TECHNOLOGIES")
    
    # Using 3 columns for density and readability
    col1, col2, col3 = st.columns(3)
    
    # FIX: Removed custom <div> tags inside columns to prevent flex layout conflicts.
    # We will rely on the natural layout of st.markdown inside the columns.
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
    st.header("EDUCATION & LEADERSHIP")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Education")
        # FIX: Ensure content-card is correctly wrapping the education block
        st.markdown('<div class="content-card">', unsafe_allow_html=True) 
        st.markdown("**BTech Computer Science & Engineering (Data Science)**")
        st.caption("Kalam Technical University, Mar Athanasius College of Engineering")
        st.markdown("Kothamangalam, Kerala | Expected June 2027")
        st.markdown("Cumulative GPA: **7.52/10**")
        st.markdown('</div>', unsafe_allow_html=True) 
        
    with col2:
        st.subheader("Leadership")
        # Leadership blocks remain inside content-card wrappers, but are contained within the st.column
        st.markdown('<div class="content-card">', unsafe_allow_html=True) 
        st.markdown("**Campus Director @ Hult Prize MACE (2023-2025)**")
        st.markdown("""
        - Led the Hult Prize On-Campus Program with 100+ participants.
        - Organized community events to foster social impact-driven innovation.
        """)
        st.markdown('</div>', unsafe_allow_html=True) 
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True) 
        st.markdown("**Campus Lead @ TinkerHub MACE (2024-2025)**")
        st.markdown("""
        - Organized Kerala's largest women-exclusive hackathon, **Tink-Her-Hack** (100 participants).
        - Secured **Best Venue Award** among 63 venues in Kerala.
        """)
        st.markdown('</div>', unsafe_allow_html=True) 
        
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
