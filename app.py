import streamlit as st
from export_utils import export_to_pdf, export_to_docx
from models import PersonalInformation, Education, Experience, Skills, CVData
from cv_builder import generate_cv_content

st.set_page_config(layout="wide", page_title="ATS CV Creator")
st.title("ATS-Friendly CV Creator")

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to reset all CV data
def reset_cv_data():
    st.session_state.cv_data = CVData()
    st.success("All CV fields have been reset!")

if st.button("Reset All Fields", help="Clear all entered information and start fresh."):
    reset_cv_data()
    st.rerun() # Rerun to reflect the cleared state

# Initialize session state for data storage using dataclasses
if 'cv_data' not in st.session_state:
    st.session_state.cv_data = CVData()

# Main content area and live preview
input_column, preview_column = st.columns([2, 1])

with input_column:
    tabs = st.tabs(["Personal Information", "Education", "Experience", "Skills"])

    with tabs[0]: # Personal Information
        st.header("Personal Information")
        with st.expander("Contact Details", expanded=True):
            st.session_state.cv_data.personal_info.name = st.text_input("Full Name", value=st.session_state.cv_data.personal_info.name, help="Your full legal name.")
            
            email_input = st.text_input("Email", value=st.session_state.cv_data.personal_info.email, help="A professional email address.")
            if not email_input:
                st.warning("Email is required.")
            elif "@" not in email_input or "." not in email_input:
                st.error("Please enter a valid email address.")
            st.session_state.cv_data.personal_info.email = email_input

            phone_input = st.text_input("Phone (e.g., +1 123 456 7890)", value=st.session_state.cv_data.personal_info.phone, help="Include country code for international numbers.")
            if not phone_input:
                st.warning("Phone number is required.")
            st.session_state.cv_data.personal_info.phone = phone_input

            linkedin_input = st.text_input("LinkedIn Profile URL", value=st.session_state.cv_data.personal_info.linkedin, help="Full URL to your LinkedIn profile.")
            if linkedin_input and not linkedin_input.startswith("http"):
                st.error("Please enter a valid URL (e.g., https://linkedin.com/in/yourprofile).")
            st.session_state.cv_data.personal_info.linkedin = linkedin_input

            github_input = st.text_input("GitHub Profile URL", value=st.session_state.cv_data.personal_info.github, help="Full URL to your GitHub profile.")
            if github_input and not github_input.startswith("http"):
                st.error("Please enter a valid URL (e.g., https://github.com/yourusername).")
            st.session_state.cv_data.personal_info.github = github_input

        with st.expander("Professional Summary/Objective", expanded=True):
            st.session_state.cv_data.personal_info.summary = st.text_area("Summary", value=st.session_state.cv_data.personal_info.summary, help="A brief overview of your skills and career goals (max 3-5 sentences).")

    with tabs[1]: # Education
        st.header("Education")
        with st.expander("Add New Education", expanded=True):
            with st.form("education_form", clear_on_submit=True):
                common_degrees = ["Bachelor of Science", "Master of Arts", "PhD", "Associate Degree", "High School Diploma", "MBA", "Juris Doctor (J.D.)", "Doctor of Medicine (M.D.)", "Other"]
                selected_degree = st.selectbox("Degree", common_degrees, help="Select your degree or choose 'Other' to enter a custom one.")
                if selected_degree == "Other":
                    degree = st.text_input("Custom Degree", help="e.g., Bachelor of Engineering in Robotics")
                else:
                    degree = selected_degree
                major = st.text_input("Major (e.g., Computer Science)", help="e.g., Computer Science, Business Administration, English Literature.")
                institution = st.text_input("Institution Name", help="Name of the university or college.")
                location = st.text_input("Location (City, Country)", help="e.g., London, UK; New York, USA.")
                start_date = st.text_input("Start Date (e.g., YYYY-MM)", help="Format: YYYY-MM (e.g., 2018-09).")
                end_date = st.text_input("End Date (e.g., YYYY-MM or Present)", help="Format: YYYY-MM (e.g., 2022-06) or 'Present'.")
                gpa = st.text_input("GPA (Optional, e.g., 3.8/4.0 or 90%)", help="Your GPA or equivalent academic score.")
                
                submitted = st.form_submit_button("Add Education")
                if submitted:
                    if not all([degree, major, institution, location, start_date, end_date]):
                        st.error("Please fill in all required fields for education.")
                    else:
                        st.session_state.cv_data.education.append(Education(
                            degree=degree, major=major, institution=institution,
                            location=location, start_date=start_date, end_date=end_date, gpa=gpa
                        ))
                        st.success("Education added!")

        st.subheader("Your Education")
        if st.session_state.cv_data.education:
            for i, edu in enumerate(st.session_state.cv_data.education):
                st.write(f"**{edu.degree}** in {edu.major}")
                st.write(f"{edu.institution}, {edu.location}")
                st.write(f"{edu.start_date} - {edu.end_date}")
                if edu.gpa:
                    st.write(f"GPA: {edu.gpa}")
                if st.button(f"Remove Education {i+1}", key=f"remove_edu_{i}"):
                    st.session_state.cv_data.education.pop(i)
                    st.rerun()
                st.markdown("---")
        else:
            st.info("No education details added yet.")

    with tabs[2]: # Experience
        st.header("Work Experience")
        with st.expander("Add New Experience", expanded=True):
            with st.form("experience_form", clear_on_submit=True):
                common_titles = ["Software Engineer", "Data Scientist", "Project Manager", "Product Manager", "Marketing Specialist", 
                                 "Human Resources Manager", "Financial Analyst", "Graphic Designer", "Customer Service Representative", 
                                 "Operations Manager", "Business Analyst", "DevOps Engineer", "UI/UX Designer", "Consultant", "Sales Manager", 
                                 "Accountant", "Researcher", "Educator", "Other"]
                selected_title = st.selectbox("Job Title", common_titles, help="Select your job title or choose 'Other' to enter a custom one.")
                if selected_title == "Other":
                    title = st.text_input("Custom Job Title", help="e.g., Senior AI/ML Engineer")
                else:
                    title = selected_title
                company = st.text_input("Company Name", help="Name of the company you worked for.")
                location = st.text_input("Location (City, Country)", help="e.g., Berlin, Germany; Paris, France.")
                start_date = st.text_input("Start Date (e.g., YYYY-MM)", help="Format: YYYY-MM (e.g., 2022-07).")
                end_date = st.text_input("End Date (e.g., YYYY-MM or Present)", help="Format: YYYY-MM (e.g., 2024-01) or 'Present'.")
                description = st.text_area("Responsibilities and Achievements (use bullet points or new lines for each point)", help="Highlight your key duties and accomplishments using bullet points.")
                
                submitted = st.form_submit_button("Add Experience")
                if submitted:
                    if not all([title, company, location, start_date, end_date, description]):
                        st.error("Please fill in all required fields for experience.")
                    else:
                        st.session_state.cv_data.experience.append(Experience(
                            title=title, company=company, location=location,
                            start_date=start_date, end_date=end_date, description=description
                        ))
                        st.success("Experience added!")

        st.subheader("Your Experience")
        if st.session_state.cv_data.experience:
            for i, exp in enumerate(st.session_state.cv_data.experience):
                st.write(f"**{exp.title}** at {exp.company}, {exp.location}")
                st.write(f"{exp.start_date} - {exp.end_date}")
                st.markdown(exp.description.replace('\n', '  \n- ')) # Render description as bullet points
                if st.button(f"Remove Experience {i+1}", key=f"remove_exp_{i}"):
                    st.session_state.cv_data.experience.pop(i)
                    st.rerun()
                st.markdown("---")
        else:
            st.info("No work experience added yet.")

    with tabs[3]: # Skills
        st.header("Skills")

        def add_skill(skill_type, new_skill_input):
            if new_skill_input:
                getattr(st.session_state.cv_data.skills, skill_type).append(new_skill_input)
                # Clear the input box after adding the skill
                if skill_type == "technical":
                    st.session_state.new_technical_skill = ""
                elif skill_type == "soft":
                    st.session_state.new_soft_skill = ""
                elif skill_type == "languages":
                    st.session_state.new_languages_skill = ""


        def remove_skill(skill_type, index):
            getattr(st.session_state.cv_data.skills, skill_type).pop(index)

        # Technical Skills
        st.subheader("Technical Skills")
        new_tech_skill = st.text_input("Add Technical Skill", key="new_technical_skill", help="e.g., Python, SQL, AWS, Docker.")
        if st.button("Add Technical Skill", key="add_tech_button"):
            add_skill("technical", new_tech_skill)
            st.rerun()
        if st.session_state.cv_data.skills.technical:
            for i, skill in enumerate(st.session_state.cv_data.skills.technical):
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.write(f"- {skill}")
                with col2:
                    st.button("Remove", key=f"remove_tech_skill_{i}", on_click=remove_skill, args=("technical", i))
        else:
            st.info("No technical skills added yet.")

        # Soft Skills
        st.subheader("Soft Skills")
        new_soft_skill = st.text_input("Add Soft Skill", key="new_soft_skill", help="e.g., Communication, Teamwork, Problem-solving.")
        if st.button("Add Soft Skill", key="add_soft_button"):
            add_skill("soft", new_soft_skill)
            st.rerun()
        if st.session_state.cv_data.skills.soft:
            for i, skill in enumerate(st.session_state.cv_data.skills.soft):
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.write(f"- {skill}")
                with col2:
                    st.button("Remove", key=f"remove_soft_skill_{i}", on_click=remove_skill, args=("soft", i))
        else:
            st.info("No soft skills added yet.")

        # Languages
        st.subheader("Languages")
        new_lang_skill = st.text_input("Add Language", key="new_languages_skill", help="e.g., English, Spanish, French.")
        if st.button("Add Language", key="add_lang_button"):
            add_skill("languages", new_lang_skill)
            st.rerun()
        if st.session_state.cv_data.skills.languages:
            for i, skill in enumerate(st.session_state.cv_data.skills.languages):
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.write(f"- {skill}")
                with col2:
                    st.button("Remove", key=f"remove_lang_skill_{i}", on_click=remove_skill, args=("languages", i))
        else:
            st.info("No languages added yet.")

with preview_column:
    st.header("Live CV Preview")
    
    if st.session_state.cv_data.personal_info.name:
        cv_output = generate_cv_content(st.session_state.cv_data)
        st.markdown(f"<div class='a4-page'>{cv_output}</div>", unsafe_allow_html=True)

        st.download_button(
            label="Download CV as Markdown (.md)",
            data=cv_output,
            file_name=f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.md",
            mime="text/markdown"
        )
        st.download_button(
            label="Download CV as Plain Text (.txt)",
            data=cv_output,
            file_name=f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.txt",
            mime="text/plain"
        )
        
        pdf_buffer = export_to_pdf(st.session_state.cv_data, f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.pdf")
        st.download_button(
            label="Download CV as PDF (.pdf)",
            data=pdf_buffer.getvalue(),
            file_name=f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.pdf",
            mime="application/pdf"
        )

        docx_buffer = export_to_docx(st.session_state.cv_data, f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.docx")
        st.download_button(
            label="Download CV as DOCX (.docx)",
            data=docx_buffer.getvalue(),
            file_name=f"{st.session_state.cv_data.personal_info.name.replace(' ', '_')}_CV.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    else:
        st.info("Fill in your personal information to see the live preview.")