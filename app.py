import streamlit as st

# --- CONFIGURATION ---
PAGE_TITLE = "Donita Lemek | Data Scientist & Developer"
PAGE_ICON = "📊"
NAME = "DONITA LEMEK"
DESCRIPTION = "Aspiring Data Scientist with a foundation in Data Analytics and Web Technologies. Interested in learning and exploring AI concepts."
EMAIL = "donitalemek@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/donita-lemek",
    "Portfolio (WIP)": "#", 
    "GitHub": "https://github.com/yourusername",
}
# Define the path to the resume (for a download link, if needed)
RESUME_FILE = "Resume .pdf" 

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


# --- CUSTOM STYLING (NEW SECTION) ---
def local_css():
    """Injects custom CSS for improved aesthetics."""
    # Define a clean primary color (e.g., a modern professional blue or teal)
    PRIMARY_COLOR = "#007BFF" # A professional blue
    
    # Custom CSS for a modern, elegant look
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        html, body, [class*="stApp"] {{
            font-family: 'Inter', sans-serif;
            background-color: #f7f7f7; /* Light background for contrast */
        }}
        
        /* Main Title Styling */
        h1 {{
            color: #333333;
            font-weight: 700;
            border-bottom: 3px solid {PRIMARY_COLOR};
            padding-bottom: 5px;
        }}
        
        /* Section Header Styling */
        h2 {{
            color: {PRIMARY_COLOR};
            font-weight: 600;
            padding-top: 10px;
        }}
        
        /* Sub-Header Styling */
        h3 {{
            color: #555555;
            font-weight: 600;
            margin-bottom: 0px !important;
        }}
        
        /* Markdown Separators */
        hr {{
            border-top: 2px solid #dddddd;
            margin: 20px 0;
        }}

        /* Enhance Expander Titles (Projects) */
        .streamlit-expanderHeader p {{
            font-size: 1.1em;
            font-weight: 600;
            color: #333333;
        }}
        
        /* Footer Styling */
        .footer {{
            text-align: center; 
            font-size: small; 
            color: #888888; 
            padding-top: 20px;
        }}
        
        /* Hide the default Streamlit menu/footer/header (redundant but safe) */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)
    
# --- HEADER SECTION ---
def render_header():
    """Renders the main header, contact info, and summary."""
    st.title(NAME)
    st.caption(DESCRIPTION)
    
    # Contact information in columns
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1]) # Adjusting column ratio slightly
    with col1:
        st.markdown(f"**Email:** {EMAIL}")
    with col2:
        st.markdown(f"**Phone:** +91 9400790480")
    with col3:
        st.markdown(f"**Location:** Wayanad, Kerala, India")

    # Social Media Links
    social_links = " | ".join([f"[{key}]({value})" for key, value in SOCIAL_MEDIA.items()])
    st.markdown(f"🌐 {social_links}")
    
    st.markdown("---")

# --- EXPERIENCE SECTION ---
def render_experience():
    """Renders Professional Experience details."""
    st.header("💼 Professional Experience")

    # --- ProductByDesign ---
    st.subheader("Associate Data Scientist (Remote Internship) @ ProductByDesign")
    st.caption("Melbourne, Australia | August 2025 - Present")
    st.markdown("""
    - Built a **predictive dashboard** in SAP Analytics Cloud using time series forecasting.
    - Modeled and wrangled data for analysis; applied **Smart Predict** to forecast trends.
    - Visualized insights with interactive charts and KPIs to support business decisions.
    """)
    st.markdown("---", help="") # Using a lighter separator within sections for flow

    # --- Kalkitech Ltd ---
    st.subheader("Software Development Engineer Intern (Hybrid Internship) @ Kalkitech Ltd")
    st.caption("Kochi, Kerala | December 2023 - August 2025")
    st.markdown("""
    - Developed a C-based **simulation tool** to improve substation safety protocols, reducing incidents through better risk management.
    - Built a **React UI** for enhanced accessibility and used data visualization for testing and performance validation.
    - Working on ML based projects to simulate phasor signals.
    """)
    st.markdown("---", help="")

    # --- AtithiGo ---
    st.subheader("Frontend Developer (Remote Internship) @ AtithiGo")
    st.caption("Kochi, Kerala | December 2024 - March 2025")
    st.markdown("""
    - Collaborated with a team of three developers to design and build the complete **front-end** for the AtithiGo hotel booking website.
    - Utilized modern front-end technologies to ensure a responsive and user-friendly design.
    - Focused on enhancing UI/UX for seamless navigation and booking experience.
    """)
    st.markdown("---")

# --- PROJECTS SECTION ---
def render_projects():
    """Renders key projects using expandable sections."""
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
        with st.expander(f"**{project['title']}** - *{project['tech']}*"):
            st.markdown(project['desc'])
            
    st.markdown("---")

# --- SKILLS SECTION ---
def render_skills():
    """Renders technical skills categorized."""
    st.header("🛠️ Skills & Technologies")
    
    # Update skills to include MERN stack components
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        st.markdown("Python, R, C, C++, Java, Javascript, HTML, CSS, SQL")
        
    with col2:
        st.subheader("Data Science / ML")
        st.markdown("Scikit-learn, NumPy, Pandas, Matplotlib, Machine Learning, Statistical Modelling")

    with col3:
        st.subheader("Tools / Frameworks")
        # Added Express and Node.js for completeness of MERN stack
        st.markdown("Tableau, React, Flask, MongoDB, **Express**, **Node.js**, Hadoop, SAP Analytics Cloud")

    st.markdown("---")

# --- EDUCATION & LEADERSHIP SECTION ---
def render_education_leadership():
    """Renders education and leadership experience side-by-side."""
    col1, col2 = st.columns(2)

    with col1:
        st.header("🎓 Education")
        st.subheader("BTech Computer Science & Engineering (Data Science)")
        st.markdown("**Kalam Technical University, Mar Athanasius College of Engineering**")
        st.markdown("Kothamangalam, Kerala | Expected June 2027")
        st.markdown("Cumulative GPA: **7.52/10**")
        st.markdown("Relevant Coursework: Object Oriented Programming, Data Structures & Algorithm, Database and Management System.")
        
    with col2:
        st.header("🚀 Leadership")
        st.subheader("Campus Director @ Hult Prize MACE (2023-2025)")
        st.markdown("""
        - Led the Hult Prize On-Campus Program with 100+ participants.
        - Organized community events to foster social impact-driven innovation.
        """)
        st.subheader("Campus Lead @ TinkerHub MACE (2024-2025)")
        st.markdown("""
        - Organized Kerala's largest women-exclusive hackathon, **Tink-Her-Hack** (100 participants).
        - Secured **Best Venue Award** among 63 venues in Kerala.
        - Fostered a hands-on, beginner-friendly space for women in tech.
        """)
        
    st.markdown("---")

# --- FOOTER SECTION ---
def render_footer():
    """Renders a simple footer."""
    st.markdown('<div class="footer">Built with Streamlit by Donita Lemek | &copy; 2025 All rights reserved.</div>', unsafe_allow_html=True)


# --- MAIN APP EXECUTION ---
if __name__ == "__main__":
    local_css() # Inject custom CSS first
    
    render_header()
    render_experience()
    render_projects()
    render_skills()
    render_education_leadership()
    
    # Optional: Resume Download Button
    try:
        with open(RESUME_FILE, "rb") as pdf_file:
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_file,
                file_name=RESUME_FILE,
                mime="application/octet-stream",
            )
    except FileNotFoundError:
        st.warning(f"Note: To enable the download button, please ensure a file named '{RESUME_FILE}' is in the same directory as this script.")
        
    render_footer() 
