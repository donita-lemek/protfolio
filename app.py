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
        /* FIX: Target the main container to ensure the background covers the entire screen width */
        .stApp {{
            font-family: 'Poppins', sans-serif;
            background: radial-gradient(circle at top left, #1f2f47 0%, {BG_COLOR} 65%);
            color: {TEXT_COLOR};
        }}

        /* Apply a fixed max-width to the centered content block only (Streamlit's main content wrapper) */
        .main .block-container {{
            max-width: 800px; 
            padding-left: 1rem;
            padding-right: 1rem;
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
            margin-top: 0 !important; /* Ensure H3 is flush with the top of the card */
            margin-bottom: 0.1em !important;
        }}
        
        /* New H4 styling is kept for reference but not strictly used in current structure */
        h4 {{
            color: {TEXT_COLOR};
            font-weight: 600;
            font-size: 1.1em;
            margin-top: 0;
            margin-bottom: 0.2em;
        }}
        
        /* Caption/Metadata (Dates/Location) */
        .stCaption {{
            color: #AAAAAA; 
            font-style: italic;
            margin-top: -5px;
            display: block;
        }}
        
        /* Content Card Styling (Floating/Glass effect) */
        /* Target the native Streamlit container/expander that we'll assign 'content-card' class to */
        .content-card {{
            background-color: {CARD_BG};
            border-radius: 8px; /* Softer rounded corners */
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); /* Stronger, modern shadow */
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle white border for depth */
        }}
        
        .content-card p, .content-card ul {{
            margin-top: 10px;
            margin-bottom: 10px;
            padding-left: 20px;
        }}

        .stExpander {{
            background-color: {CARD_BG};
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); 
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
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

    # Experience details are rendered inside a single large markdown block per job 
    # to ensure all content stays within the custom 'content-card' div.
    
    # --- ProductByDesign ---
    st.markdown(f"""
    <div class="content-card">
        <h3>Associate Data Scientist</h3>
        <p><strong>ProductByDesign (Remote Internship)</strong></p>
        <div class="stCaption">Melbourne, Australia | August 2025 - Present</div>
        <ul>
            <li>Built a <strong>predictive dashboard</strong> in SAP Analytics Cloud using time series forecasting.</li>
            <li>Modeled and wrangled data for analysis; applied <strong>Smart Predict</strong> to forecast trends.</li>
            <li>Visualized insights with interactive charts and KPIs to support business decisions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- Kalkitech Ltd ---
    st.markdown(f"""
    <div class="content-card">
        <h3>Software Development Engineer Intern</h3>
        <p><strong>Kalkitech Ltd (Hybrid Internship)</strong></p>
        <div class="stCaption">Kochi, Kerala | December 2023 - August 2025</div>
        <ul>
            <li>Developed a C-based <strong>simulation tool</strong> to improve substation safety protocols, reducing incidents through better risk management.</li>
            <li>Built a React UI for enhanced accessibility and used data visualization for testing and performance validation.</li>
            <li>Working on ML based projects to simulate phasor signals.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- AtithiGo ---
    st.markdown(f"""
    <div class="content-card">
        <h3>Frontend Developer</h3>
        <p><strong>AtithiGo (Remote Internship)</strong></p>
        <div class="stCaption">Kochi, Kerala | December 2024 - March 2025</div>
        <ul>
            <li>Collaborated with a team of three developers to design and build the complete <strong>front-end</strong> for the AtithiGo hotel booking website.</li>
            <li>Utilized modern front-end technologies to ensure a responsive and user-friendly design.</li>
            <li>Focused on enhancing UI/UX for seamless navigation and booking experience.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
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
        # st.expander is styled as a floating card via CSS targetting .stExpander
        with st.expander(f"**{project['title']}** - *{project['tech']}*"):
            st.markdown(project['desc'])
            
    st.markdown("---")

# --- SKILLS SECTION ---
def render_skills():
    """Renders technical skills categorized."""
    st.header("SKILLS & TECHNOLOGIES")
    
    # Using 3 columns for density and readability
    col1, col2, col3 = st.columns(3)
    
    # Using st.container with class to ensure proper column flex behavior.
    
    with col1:
        with st.container(border=True): # Use Streamlit's container for better column compliance
            st.subheader("Programming")
            st.markdown("Python, R, C, C++, Java, Javascript, HTML, CSS, SQL")
        
    with col2:
        with st.container(border=True):
            st.subheader("Data Science / ML")
            st.markdown("Scikit-learn, NumPy, Pandas, Matplotlib, Machine Learning, Statistical Modelling")

    with col3:
        with st.container(border=True):
            st.subheader("Tools / Frameworks")
            st.markdown("Tableau, React, Flask, MongoDB, Express, Node.js, Hadoop, SAP Analytics Cloud")

    st.markdown("---")

# --- EDUCATION & LEADERSHIP SECTION ---
def render_education_leadership():
    """Renders education and leadership experience side-by-side."""
    st.header("EDUCATION & LEADERSHIP")
    col1, col2 = st.columns(2)

    # Use raw HTML structure consistently inside columns to ensure better flow control 
    # and consistent application of content-card styling across the columns.
    
    with col1:
        # Education block - all content within a single markdown block for container integrity
        st.markdown(f"""
        <div class="content-card">
            <h3>Education</h3>
            <p><strong>BTech Computer Science & Engineering (Data Science)</strong></p>
            <div class="stCaption">Kalam Technical University, Mar Athanasius College of Engineering</div>
            <div class="stCaption">Kothamangalam, Kerala | Expected June 2027</div>
            <p>Cumulative GPA: <strong>7.52/10</strong></p>
        </div>
        """, unsafe_allow_html=True) 
        
    with col2:
        # Leadership block 1 - all content within a single markdown block
        st.markdown(f"""
        <div class="content-card"> 
            <h3>Leadership</h3>
            <p><strong>Campus Director @ Hult Prize MACE (2023-2025)</strong></p>
            <ul>
                <li>Led the Hult Prize On-Campus Program with 100+ participants.</li>
                <li>Organized community events to foster social impact-driven innovation.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Leadership block 2 - all content within a single markdown block
        st.markdown(f"""
        <div class="content-card"> 
            <p><strong>Campus Lead @ TinkerHub MACE (2024-2025)</strong></p>
            <ul>
                <li>Organized Kerala's largest women-exclusive hackathon, <strong>Tink-Her-Hack</strong> (100 participants).</li>
                <li>Secured <strong>Best Venue Award</strong> among 63 venues in Kerala for conducting the same.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
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
        # Note: In a live environment, you'd replace this with actual file reading
        # For this context, we just show the warning if the file is missing
        # with open(RESUME_FILE, "rb") as pdf_file:
        #     st.download_button(
        #         label="Download Full Resume (PDF)",
        #         data=pdf_file,
        #         file_name=RESUME_FILE,
        #         mime="application/octet-stream",
        #     )
        st.warning(f"Note: The download button is commented out. To use it, ensure '{RESUME_FILE}' exists.")
    except FileNotFoundError:
        st.warning(f"Note: To enable the download button, please ensure a file named '{RESUME_FILE}' is in the same directory as this script.")
        
    render_footer()
