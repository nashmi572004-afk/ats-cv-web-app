import unittest
from datetime import datetime
from ats_cv_web_app.models import PersonalInformation, Education, Experience, Skills, CVData

class TestModels(unittest.TestCase):

    def test_personal_information_default(self):
        info = PersonalInformation()
        self.assertEqual(info.name, "")
        self.assertEqual(info.email, "")
        self.assertEqual(info.phone, "")
        self.assertEqual(info.linkedin, "")
        self.assertEqual(info.github, "")
        self.assertEqual(info.summary, "")

    def test_personal_information_custom(self):
        info = PersonalInformation(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            linkedin="linkedin.com/johndoe",
            github="github.com/johndoe",
            summary="A highly motivated individual."
        )
        self.assertEqual(info.name, "John Doe")
        self.assertEqual(info.email, "john.doe@example.com")
        self.assertEqual(info.phone, "123-456-7890")
        self.assertEqual(info.linkedin, "linkedin.com/johndoe")
        self.assertEqual(info.github, "github.com/johndoe")
        self.assertEqual(info.summary, "A highly motivated individual.")

    def test_education_default(self):
        edu = Education()
        self.assertEqual(edu.degree, "")
        self.assertEqual(edu.major, "")
        self.assertEqual(edu.institution, "")
        self.assertEqual(edu.location, "")
        self.assertEqual(edu.start_date, "")
        self.assertEqual(edu.end_date, "")
        self.assertIsNone(edu.gpa)

    def test_education_custom(self):
        edu = Education(
            degree="B.Sc.",
            major="Computer Science",
            institution="University of Tech",
            location="City, Country",
            start_date="2018-09-01",
            end_date="2022-06-30",
            gpa="3.8"
        )
        self.assertEqual(edu.degree, "B.Sc.")
        self.assertEqual(edu.major, "Computer Science")
        self.assertEqual(edu.institution, "University of Tech")
        self.assertEqual(edu.location, "City, Country")
        self.assertEqual(edu.start_date, "2018-09-01")
        self.assertEqual(edu.end_date, "2022-06-30")
        self.assertEqual(edu.gpa, "3.8")

    def test_experience_default(self):
        exp = Experience()
        self.assertEqual(exp.title, "")
        self.assertEqual(exp.company, "")
        self.assertEqual(exp.location, "")
        self.assertEqual(exp.start_date, "")
        self.assertEqual(exp.end_date, "")
        self.assertEqual(exp.description, "")

    def test_experience_custom(self):
        exp = Experience(
            title="Software Engineer",
            company="Tech Solutions Inc.",
            location="Remote",
            start_date="2022-07-01",
            end_date="Present",
            description="Developed and maintained web applications.\nCollaborated with cross-functional teams."
        )
        self.assertEqual(exp.title, "Software Engineer")
        self.assertEqual(exp.company, "Tech Solutions Inc.")
        self.assertEqual(exp.location, "Remote")
        self.assertEqual(exp.start_date, "2022-07-01")
        self.assertEqual(exp.end_date, "Present")
        self.assertEqual(exp.description, "Developed and maintained web applications.\nCollaborated with cross-functional teams.")

    def test_skills_default(self):
        skills = Skills()
        self.assertEqual(skills.technical, [])
        self.assertEqual(skills.soft, [])
        self.assertEqual(skills.languages, [])

    def test_skills_custom(self):
        skills = Skills(
            technical=["Python", "Flask"],
            soft=["Communication", "Teamwork"],
            languages=["English", "Spanish"]
        )
        self.assertEqual(skills.technical, ["Python", "Flask"])
        self.assertEqual(skills.soft, ["Communication", "Teamwork"])
        self.assertEqual(skills.languages, ["English", "Spanish"])

    def test_cv_data_default(self):
        cv_data = CVData()
        self.assertIsInstance(cv_data.personal_info, PersonalInformation)
        self.assertEqual(cv_data.education, [])
        self.assertEqual(cv_data.experience, [])
        self.assertIsInstance(cv_data.skills, Skills)

    def test_cv_data_custom(self):
        personal_info = PersonalInformation(name="Jane Doe")
        education = [Education(degree="M.Sc.")]
        experience = [Experience(title="Project Manager")]
        skills = Skills(technical=["Java"])

        cv_data = CVData(
            personal_info=personal_info,
            education=education,
            experience=experience,
            skills=skills
        )
        self.assertEqual(cv_data.personal_info.name, "Jane Doe")
        self.assertEqual(len(cv_data.education), 1)
        self.assertEqual(cv_data.education[0].degree, "M.Sc.")
        self.assertEqual(len(cv_data.experience), 1)
        self.assertEqual(cv_data.experience[0].title, "Project Manager")
        self.assertEqual(cv_data.skills.technical, ["Java"])

if __name__ == '__main__':
    unittest.main()
