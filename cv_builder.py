from models import PersonalInformation, Education, Experience, Skills, CVData

def generate_cv_content(cv_data: CVData) -> str:
    """
    Generates the CV content in markdown format from structured CVData.
    """
    cv_content = ""

    # Personal Information
    if cv_data.personal_info.name:
        cv_content += f"# {cv_data.personal_info.name}\n"
        contact_details = []
        if cv_data.personal_info.email:
            contact_details.append(cv_data.personal_info.email)
        if cv_data.personal_info.phone:
            contact_details.append(cv_data.personal_info.phone)
        if cv_data.personal_info.linkedin:
            contact_details.append(f"LinkedIn: {cv_data.personal_info.linkedin}")
        if cv_data.personal_info.github:
            contact_details.append(f"GitHub: {cv_data.personal_info.github}")
        
        if contact_details:
            cv_content += " | ".join(contact_details) + "\n\n"

    # Summary/Objective (Optional)
    if cv_data.personal_info.summary:
        cv_content += f"## Summary\n{cv_data.personal_info.summary}\n\n"

    # Education
    if cv_data.education:
        cv_content += "## Education\n"
        for edu in cv_data.education:
            cv_content += f"- **{edu.degree}** in {edu.major}\n"
            cv_content += f"  {edu.institution}, {edu.location}\n"
            cv_content += f"  {edu.start_date} - {edu.end_date}\n"
            if edu.gpa:
                cv_content += f"  GPA: {edu.gpa}\n"
            cv_content += "\n"

    # Experience
    if cv_data.experience:
        cv_content += "## Experience\n"
        for exp in cv_data.experience:
            cv_content += f"- **{exp.title}** at {exp.company}, {exp.location}\n"
            cv_content += f"  {exp.start_date} - {exp.end_date}\n"
            # Format description as bullet points
            if exp.description:
                for line in exp.description.split('\n'):
                    if line.strip(): # Only add non-empty lines
                        cv_content += f"  - {line.strip()}\n"
            cv_content += "\n"

    # Skills
    if cv_data.skills.technical or cv_data.skills.soft or cv_data.skills.languages:
        cv_content += "## Skills\n"
        if cv_data.skills.technical:
            cv_content += f"**Technical Skills:** {', '.join(cv_data.skills.technical)}\n"
        if cv_data.skills.soft:
            cv_content += f"**Soft Skills:** {', '.join(cv_data.skills.soft)}\n"
        if cv_data.skills.languages:
            cv_content += f"**Languages:** {', '.join(cv_data.skills.languages)}\n"
        cv_content += "\n"

    return cv_content
