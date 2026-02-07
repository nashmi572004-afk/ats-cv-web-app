import unittest
from models import PersonalInformation, Education, Experience, Skills, CVData
from cv_builder import generate_cv_content

class TestCvBuilder(unittest.TestCase):

    def test_generate_cv_content_empty(self):
        cv_data = CVData()
        content = generate_cv_content(cv_data)
        self.assertEqual(content, "")

    def test_generate_cv_content_personal_info_only(self):
        personal_info = PersonalInformation(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            linkedin="linkedin.com/johndoe",
            github="github.com/johndoe",
            summary="A passionate software engineer."
        )
        cv_data = CVData(personal_info=personal_info)
        content = generate_cv_content(cv_data)
        expected_content = (
            "# John Doe\n"
            "john.doe@example.com | 123-456-7890 | LinkedIn: linkedin.com/johndoe | GitHub: github.com/johndoe\n\n"
            "## Summary\n"
            "A passionate software engineer.\n\n"
        )
        self.assertEqual(content, expected_content)

    def test_generate_cv_content_full(self):
        personal_info = PersonalInformation(
            name="Jane Doe",
            email="jane.doe@example.com",
            phone="098-765-4321",
            linkedin="linkedin.com/janedoe",
            github="github.com/janedoe",
            summary="Experienced project manager."
        )
        education = [
            Education(
                degree="M.Sc.",
                major="Project Management",
                institution="Business School",
                location="Big City, Country",
                start_date="2018-09-01",
                end_date="2020-06-30",
                gpa="4.0"
            ),
            Education(
                degree="B.A.",
                major="Business Administration",
                institution="University College",
                location="Small Town, Country",
                start_date="2014-09-01",
                end_date="2018-06-30",
                gpa="3.5"
            )
        ]
        experience = [
            Experience(
                title="Senior Project Manager",
                company="Global Solutions",
                location="Big City",
                start_date="2020-07-01",
                end_date="Present",
                description="- Led multiple cross-functional teams.\n- Delivered projects on time and within budget."
            ),
            Experience(
                title="Junior Project Manager",
                company="Local Innovations",
                location="Big City",
                start_date="2018-07-01",
                end_date="2020-06-30",
                description="- Assisted in project planning.\n- Coordinated with stakeholders."
            )
        ]
        skills = Skills(
            technical=["Jira", "Confluence"],
            soft=["Leadership", "Negotiation"],
            languages=["English", "French"]
        )

        cv_data = CVData(
            personal_info=personal_info,
            education=education,
            experience=experience,
            skills=skills
        )
        content = generate_cv_content(cv_data)
        expected_content = (
            "# Jane Doe\n"
            "jane.doe@example.com | 098-765-4321 | LinkedIn: linkedin.com/janedoe | GitHub: github.com/janedoe\n\n"
            "## Summary\n"
            "Experienced project manager.\n\n"
            "## Education\n"
            "- **M.Sc.** in Project Management\n"
            "  Business School, Big City, Country\n"
            "  2018-09-01 - 2020-06-30\n"
            "  GPA: 4.0\n\n"
            "- **B.A.** in Business Administration\n"
            "  University College, Small Town, Country\n"
            "  2014-09-01 - 2018-06-30\n"
            "  GPA: 3.5\n\n"
            "## Experience\n"
            "- **Senior Project Manager** at Global Solutions, Big City\n"
            "  2020-07-01 - Present\n"
            "  - Led multiple cross-functional teams.\n"
            "  - Delivered projects on time and within budget.\n\n"
            "- **Junior Project Manager** at Local Innovations, Big City\n"
            "  2018-07-01 - 2020-06-30\n"
            "  - Assisted in project planning.\n"
            "  - Coordinated with stakeholders.\n\n"
            "## Skills\n"
            "**Technical Skills:** Jira, Confluence\n"
            "**Soft Skills:** Leadership, Negotiation\n"
            "**Languages:** English, French\n\n"
        )
        self.assertEqual(content, expected_content)

    def test_generate_cv_content_missing_sections(self):
        personal_info = PersonalInformation(name="Test User")
        skills = Skills(technical=["Python"])
        cv_data = CVData(
            personal_info=personal_info,
            skills=skills
        )
        content = generate_cv_content(cv_data)
        expected_content = (
            "# Test User\n\n"
            "## Skills\n"
            "**Technical Skills:** Python\n\n"
        )
        self.assertEqual(content, expected_content)

    def test_generate_cv_content_experience_with_multiline_description(self):
        experience = [
            Experience(
                title="Developer",
                company="Innovate Corp",
                location="Virtual",
                start_date="2021-01-01",
                end_date="2023-12-31",
                description="Line 1 of description.\nLine 2 of description.\n  Line 3 indented.\n\nLine 4 after empty line."
            )
        ]
        cv_data = CVData(experience=experience)
        content = generate_cv_content(cv_data)
        expected_content = (
            "## Experience\n"
            "- **Developer** at Innovate Corp, Virtual\n"
            "  2021-01-01 - 2023-12-31\n"
            "  - Line 1 of description.\n"
            "  - Line 2 of description.\n"
            "  - Line 3 indented.\n"
            "  - Line 4 after empty line.\n\n"
        )
        self.assertEqual(content, expected_content)

    def test_generate_cv_content_personal_info_partial_contact(self):
        personal_info = PersonalInformation(
            name="Minimal Contact",
            email="minimal@example.com"
        )
        cv_data = CVData(personal_info=personal_info)
        content = generate_cv_content(cv_data)
        expected_content = (
            "# Minimal Contact\n"
            "minimal@example.com\n\n"
        )
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
