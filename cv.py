import streamlit as st
from st_social_media_links import SocialMediaIcons
from datetime import datetime
import json
import base64

st.set_page_config(page_title='CV' ,layout="wide",page_icon='📄')



# ------------------ some functions -----------------------#

def colored_header(label, color=None, description=None):
    """Shows a header with a colored underline and an optional description."""
    st.subheader(label)
    st.write(
        f'<hr style="background-color: {color}; margin-top: 0; margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    if description:
        st.caption(description)


def card(rgb_colour_box, rgb_colour_font, sline, i):
      """Displays a nice colored card"""
      fontsize = 38
      valign = "left"
      iconname = "fa-solid fa-check"
      lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

      htmlstr = f"""<p style='background-color: rgb({rgb_colour_box[0]}, 
                                                  {rgb_colour_box[1]}, 
                                                  {rgb_colour_box[2]}, 0.75); 
                            color: rgb({rgb_colour_font[0]}, 
                                      {rgb_colour_font[1]}, 
                                      {rgb_colour_font[2]}); 
                            font-size: {fontsize}px;
                            text-align: {valign};
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 0px; 
                            padding-bottom: 18px; 
                            line-height:40px;'>
                            <i class={iconname}></i>
                            <span style='font-size: 12px; color: white;
                            margin-top: 0;'>{sline}</style></span><BR>
                            {i}
                            </style></p>"""
      return lnk + htmlstr


def local_css(file_name):
  """Calls for a CSS file for general formatting"""
  with open(file_name, encoding="utf-8") as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def img_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
      
# -----------------  sidebar with intro  ----------------- #
with st.sidebar:

  local_css("CSS/style.css")
  
  st.image ('./media/sofia-portrait2.png', width="stretch")
  
  cvfile="./CV Sofia Matias 2026 (DE).pdf"
  c1, c2, c3 = st.columns([1, 3, 1])
  with open(cvfile, "rb") as file:
    with c2:
      btn = st.download_button(
              label="📄 Download CV",
              data=file,
              file_name=cvfile,
              width="stretch"
            )

  social_media_links = [
      "https://www.linkedin.com/in/sofia-matias/",
      "https://github.com/sofiammatias"
      ]
  social_media_icons = SocialMediaIcons(social_media_links)
  social_media_icons.render()
  
  st.markdown("""""")
  st.markdown("""**Data Engineer** | **Power BI Administrator**""")

st.subheader('Sofia Matias - Data Engineer')
#------- tabs -------------#  
aboutme, skills, experience, education, projects, certificates = st.tabs(["About Me", "Skills", "Professional Experience", "Education", "Projects", "Certificates"])
# -------------- tabs styling -------------------------#
st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 5px;
    }
  .stTabs [data-baseweb="tab-highlight"] {
        background-color:lightblue;
        font-color:black;    
    }
	.stTabs [data-baseweb="tab"] {
		height: 45px;
    width: 200px;
    white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    padding-left: 10px;
    padding-right: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)

#------------------ about me tab ---------------------#
with aboutme:
  st.write(""" """)
  col1, col2, col3 = st.columns(3)
  #----------------------- card for metrics -----------------#

    #--------------- metrics -----------#
  with col1:
    this_year = datetime.today().year
    exp = this_year - 2002  # Assuming the user started working in 2002
    st.markdown(card((153, 187, 240),(255,255,255),"Years of Experience", exp), unsafe_allow_html=True)

  with col2:
    st.markdown(card((114, 153, 214),(255,255,255),"Power BI Dashboards", "+20"), unsafe_allow_html=True)

  with col3:
    st.markdown(card((77, 125, 201),(255,255,255),"Data Science Projects", "4"), unsafe_allow_html=True)

  # --------------------- text ---------------------#  
  st.write(""" """)
  st.markdown("""**Data Engineer with strong experience in Power BI Report Server administration within the banking sector (on-premises environment).** 
              \n Skilled in platform governance, monitoring, troubleshooting, and BI infrastructure optimization.
              \n Brings **20+ years of multidisciplinary engineering experience** across software, research, and technical project management.
              \n Recognized for precision, autonomy, and the ability to quickly understand and optimize complex systems.""")

#-------------------- skills tab ----------------------#
  with skills:
    html_skills = """
<div class="skills-grid">
  <div class="left-column">
    <div class="skill-card technical-highlight">
      <h3 class="tech-title">Technical Skills</h3>
        <p class="skill-subtitle">Programming & Data</p>
        <ul class="skill-list">
          <li>Python</li>
          <li>SQL (SQL Server, SQLite)</li>
        </ul>
        <p class="skill-subtitle">Machine Learning & Deep Learning</p>
        <ul class="skill-list">
          <li>Scikit-Learn</li>
          <li>TensorFlow / Keras</li>
          <li>Deep learning fundamentals</li>
          <li>Model training & evaluation</li>
          <li>MLflow (tracking & model management)</li>
        </ul>
      <p class="skill-subtitle">BI & Analytics</p>
      <ul class="skill-list">
        <li>Power BI DAX</li>
        <li>Power Query</li>
        <li>Power BI Report Server Admin</li>
      </ul>
      <p class="skill-subtitle">DevOps & Tools</p>
      <ul class="skill-list">
        <li>Docker</li>
        <li>FastAPI</li>
        <li>Prefect</li>
        <li>Git / GitHub</li>
        <li>Google Cloud Platform</li>
      </ul>
      <p class="skill-subtitle">Visualization</p>
      <ul class="skill-list">
        <li>Matplotlib / Seaborn</li>
        <li>Power BI</li>
      </ul>
    </div>
  </div>
  <div class="right-column"> 
    <div class="skill-card">
      <h3>Soft Skills</h3>
      <ul class="skill-list">
        <li>Detail-oriented</li>
        <li>Problem-solving</li>
        <li>Time management</li>
        <li>Adaptable & fast learner</li>
        <li>Self-driven & autonomous</li>
        <li>Strong communication skills</li>
        <li>Portuguese (native)</li>
        <li>English (fluent)</li>
        <li>French (basic)</li>
      </ul>
    </div>
    <div class="skill-card">
      <h3>Organisational Skills</h3>
      <ul class="skill-list">
        <li>Project & team management</li>
        <li>Cross-functional coordination</li>
        <li>Automotive industry experience</li>
        <li>Research & innovation</li>
        <li>Technical project leadership</li>
      </ul>
    </div>
  </div>
</div>
    """

    st.markdown(html_skills, unsafe_allow_html=True) 
  
#----------------------------- professional experience tab -------------------------------#
with experience:
  with st.container():
    st.markdown("""""")

    # load data
    with open("example.json", "r") as f:
      data = json.load(f)
    st.markdown("<div class='timeline'>", unsafe_allow_html=True)

    for event in data["events"]:
        start = f"{event['start_date']['month']}/{event['start_date']['year']}"
        end = event.get("end_date")
        if end:
            end = f"{end['month']}/{end['year']}"
            date = f"{start} – {end}"
        else:
            date = f"{start} – Present"

        title = event["text"]["headline"]
        text = event["text"]["text"]

        st.markdown(
            f"""
            <div class='timeline-item'>
                <div class='timeline-title'>{title}</div>
                <div class='timeline-date'>{date}</div>
                <div class='timeline-text'>{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

#---------------------- education tab -----------------------------#
with education:
      html_edu1 = """
        <div class="education-card">
          <div class="education-date">Oct 2022 - Dec 2022</div>
          <div class="education-title">Bootcamp in Data Science</div>
          <div class="education-school">Le Wagon</div>
          <p class="education-summary">
            Intensive 10-week program focused on Python, data analysis, machine learning, APIs, and deployment.
          </p>
          <ul class="education-list">
            <li>Python programming & data manipulation</li>
            <li>Exploratory data analysis (Jupyter)</li>
            <li>Machine learning & deep learning</li>
            <li>API development & deployment (FastAPI)</li>
            <li>ML engineering fundamentals</li>
            <li>SQL & database management</li>
            <li>Version control (Git/GitHub)</li>
          </ul>
          <p class="education-subtitle">Key Skills Acquired</p>
          <ul class="education-skills">
            <li>Pandas / Numpy</li>
            <li>Matplotlib / Seaborn</li>
            <li>Scikit-Learn</li>
            <li>SQL</li>
            <li>MLFlow</li>
            <li>FastAPI</li>
          </ul>
        </div>
      """
      st.markdown(html_edu1, unsafe_allow_html=True) 
      html_edu2 = """
      <div class="education-card">
        <div class="education-date">Sep 2010 - Jul 2011</div>
        <div class="education-title">Master Executive in Sustainable Energy Systems</div>
        <div class="education-school">IST / ISEG - Lisbon Technical University · MIT Portugal Program</div>
        <p class="education-summary">
          Advanced multidisciplinary program focused on energy systems, sustainability, economics, and leadership.  
          Developed strong analytical and strategic skills for designing, evaluating, and optimizing sustainable energy systems.
        </p>
        <ul class="education-list">
          <li>Renewable energy resources & integration</li>
          <li>Energy management & efficiency</li>
          <li>Sustainable development & environmental impact</li>
          <li>Energy systems economics & modeling</li>
          <li>Regulatory theory & policy frameworks</li>
          <li>Project evaluation, externalities & risk management</li>
          <li>Energy in transportation systems</li>
        </ul>
        <p class="education-subtitle">Key Skills Acquired</p>
        <ul class="education-skills">
          <li>Energy systems modeling</li>
          <li>Economic analysis & forecasting</li>
          <li>Sustainability assessment</li>
          <li>Regulatory frameworks</li>
          <li>Project evaluation</li>
          <li>Leadership & strategic thinking</li>
        </ul>
      </div>
      """
      st.markdown(html_edu2, unsafe_allow_html=True)
      html_edu3 = """
      <div class="education-card">

        <div class="education-date">Sep 1994 - Aug 2001</div>

        <div class="education-title">Graduation in Mechanical Engineering</div>
        <div class="education-school">IST - Technical Superior Institute, Lisbon Technical University</div>

        <p class="education-summary">
          Specialization in Systems Automation and Robotics, with strong foundations in control systems,  
          industrial automation, robotics, intelligent systems, and mechanical design.
        </p>

        <ul class="education-list">
          <li>Systems control & dynamic modeling</li>
          <li>Industrial automation & robotics</li>
          <li>Machine design & mechanical systems</li>
          <li>Sensors, actuators & industrial computing</li>
          <li>Energetic analysis of systems</li>
          <li>Project management & engineering processes</li>
        </ul>

        <p class="education-subtitle">Key Skills Acquired</p>
        <ul class="education-skills">
          <li>Control systems</li>
          <li>Automation & robotics</li>
          <li>Mechanical design</li>
          <li>Industrial computing</li>
          <li>Systems simulation</li>
          <li>Engineering project management</li>
        </ul>

      </div>
      """
      st.markdown(html_edu3, unsafe_allow_html=True)

#---------------------- projects tab -----------------------------#
with projects:

    # Convert images to base64
    img_etl = img_to_base64("./media/etl_app.jpg")
    img_biomassters = img_to_base64("./media/Biomassters_app.jpg")
    img_tick = img_to_base64("./media/ticktick-bloom.jpg")
    img_houses = img_to_base64("./media/Houses_app.jpg")
    img_icecube = img_to_base64("./media/icecube.jpg")
    img_eda = img_to_base64("./media/EDA_app.jpg")
    img_learning = img_to_base64("./media/learning-equality.jpg")

    projects_html = f"""
    <div class="project-grid">
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_etl}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Data Engineering</div>
                <div class="project-title">ETL Pipeline</div>
                <div class="project-title">Austin Crime DB</div>
                <div class="project-summary">
                    End-to-end ETL pipeline extracting data from Austin City API, transforming it and loading it into PostgreSQL. Includes monitoring dashboard and Prefect orchestration.
                </div>
                <div class="project-links">
                    <a href="https://etl-pipeline-austin-crime.streamlit.app/" target="_blank">View App</a>
                    <a href="https://github.com/sofiammatias/etl-pipeline-austin-crime/" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_biomassters}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Deep Learning</div>
                <div class="project-title">Biomassters</div>
                <div class="project-title">U-Net Deep Learning</div>
                <div class="project-summary">
                    Deep learning project using U-Net to predict satellite imagery. Ranked 61/911. Includes live API demo and MLflow tracking.
                </div>
                <div class="project-links">
                    <a href="https://sofiammatias-biomassters-website-app-zfuyub.streamlit.app/" target="_blank">View App</a>
                    <a href="https://github.com/sofiammatias/project-biomassters" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_tick}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Machine Learning</div>
                <div class="project-title">Tick Tick Bloom</div>
                <div class="project-title">LGBM</div>
                <div class="project-summary">
                    DrivenData challenge predicting algae bloom severity using satellite imagery. Ranked 62/1377 using LGBM classifier (Light Gradient Boosting Machine).
                </div>
                <div class="project-links">
                    <a href="https://colab.research.google.com/drive/1NniXg7vzMU7Yq9SLayaZHKKbm22e2bPK?usp=sharing" target="_blank">Colab Notebook</a>
                    <a href="https://github.com/sofiammatias/tick-tick-bloom" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_houses}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Data Engineering</div>
                <div class="project-title">Houses for Sale</div>
                <div class="project-title">loft.com.br</div>
                <div class="project-summary">
                    Web scraping + data visualization project using Python, Streamlit and Power BI. Includes interactive maps, price analysis and property metrics.
                </div>
                <div class="project-links">
                    <a href="https://data-visualization-houses-loft.streamlit.app/" target="_blank">View App</a>
                    <a href="https://github.com/sofiammatias/data-visualization-houses/blob/main/Data_Visualization_With_Streamlit.py" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_icecube}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Deep Learning</div>
                <div class="project-title">IceCube Neutrinos</div>
                <div class="project-title">GNN</div>
                <div class="project-summary">
                    Kaggle challenge predicting neutrino direction using GNN: Graph Neural Networks. Focus on handling very large datasets (6GB+).
                </div>
                <div class="project-links">
                    <a href="https://www.kaggle.com/code/sofiamatias/icecube-predictions-simple-nn" target="_blank">Kaggle Notebook</a>
                    <a href="https://github.com/sofiammatias/ice-cube-neutrinos" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_eda}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Data Analysis</div>
                <div class="project-title">Netflix Rotten Tomatoes</div>
                <div class="project-title">EDA</div>
                <div class="project-summary">
                    Exploratory data analysis of the Netflix Rotten Tomatoes dataset, including univariate, bivariate and correlation analysis. Built with Python and Streamlit.
                </div>
                <div class="project-links">
                    <a href="https://data-visualization-eda-netflix.streamlit.app/" target="_blank">View App</a>
                    <a href="https://github.com/sofiammatias/data-visualization-eda" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
        <div class="project-card">
            <img src="data:image/jpeg;base64,{img_learning}" class="project-image">
            <div class="project-content">
                <div class="project-badge">Natural Language Processing</div>
                <div class="project-title">Learning Equality</div>
                <div class="project-title">Sentence Transformers</div>
                <div class="project-summary">
                    Kaggle code competition using sentence transformers for semantic search and topic matching. Ranked 32/107 for Efficiency Prize.
                </div>
                <div class="project-links">
                    <a href="https://www.kaggle.com/code/sofiamatias/learning-equality-challenge-semanticsearch/" target="_blank">Kaggle Notebook</a>
                    <a href="https://github.com/sofiammatias/learning-equality#readme" target="_blank">GitHub Repo</a>
                </div>
            </div>
        </div>
    </div>
    """ 
    st.markdown(projects_html, unsafe_allow_html=True)

# ---------------------- certificates tab -----------------------------#
with certificates:

    certificates_html = """
    <div class="cert-card">
        <div class="cert-year">2023</div>
        <ul class="cert-list">
            <li><a href="https://1drv.ms/i/c/b8e277c8c16e4c5f/IQBLXPwbGaVHQZ7lufWrfII9AZi1N3I-PFE67zIJrdImQY0?e=j3eINF" target="_blank">Google Professional Data Engineer - A Cloud Guru</a></li>
            <li><a href="https://1drv.ms/i/c/b8e277c8c16e4c5f/IQBLXPwbGaVHQZ7lufWrfII9AZi1N3I-PFE67zIJrdImQY0?e=j3eINF" target="_blank">Introduction to Containers and Docker - A Cloud Guru</a></li>
            <li><a href="https://1drv.ms/i/c/b8e277c8c16e4c5f/IQBfTG7ByHfiIIC4bOcDAAAAAZx-pzJ2zFTDGIOxX-NWuGs?e=qUo10Y" target="_blank">Denodo Platform Installation</a></li>
            <li><a href="https://www.udemy.com/certificate/UC-e6c07e79-083b-440a-8215-7cf312ecf513/" target="_blank">Power BI: Deployment and Management – Udemy</a></li>
            <li><a href="https://www.coursera.org/account/accomplishments/certificate/9YV78UQRMDVN" target="_blank">Getting Started with Power BI Desktop – Coursera</a></li>
        </ul>
    </div>
    <div class="cert-card">
        <div class="cert-year">2022</div>
        <ul class="cert-list">
            <li><a href="https://www.coursera.org/account/accomplishments/certificate/W6FLS3DSNXFN" target="_blank">Introduction to Git and GitHub – Google</a></li>
            <li><a href="https://www.coursera.org/account/accomplishments/specialization/certificate/R6F3PN447EGP" target="_blank">Applied Data Science with Python – Univ. Michigan</a></li>
            <li><a href="https://www.coursera.org/account/accomplishments/specialization/certificate/7CV2778VXYBR" target="_blank">Python for Everybody – Univ. Michigan</a></li>
        </ul>
    </div>
    <div class="cert-card">
        <div class="cert-year">Before 2022</div>
        <div class="cert-subtitle">Aeronautical Certificates</div>
        <ul class="cert-list">
            <li>Category 4 Flight Test Training - 2019</li>
            <li>Quality Systems Audits in Aeronautical Field - SENASA - 2016</li>
            <li>STC’s, Major and Minor Modifications on CS-23, CS-25, CS-27, CS-29 - SENASA - 2015</li>
            <li>EASA Part 21 General - SENASA - 2013</li>
        </ul>
        <div class="cert-subtitle">Other Certificates</div>
        <ul class="cert-list">
            <li>Lean Manufacturing - Coursera</li>
            <li>First Certificate in English - British Council</li>
            <li>CATIA V5</li>
            <li>SPC Training - Visteon</li>
            <li>Workshop FMEA - Visteon</li>
        </ul>
    </div>
    """

    st.markdown(certificates_html, unsafe_allow_html=True)
