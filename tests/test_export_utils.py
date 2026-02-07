import unittest
from io import BytesIO
from models import PersonalInformation, Education, Experience, Skills, CVData
from export_utils import export_to_pdf, export_to_docx

class TestExportUtils(unittest.TestCase):

    def setUp(self):
        self.personal_info = PersonalInformation(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            linkedin="linkedin.com/johndoe",
            github="github.com/johndoe",
            summary="A highly motivated individual with experience in software development."
        )
        self.education = [
            Education(
                degree="M.Sc.",
                major="Computer Science",
                institution="University of Example",
                location="Example City",
                start_date="2020-09-01",
                end_date="2022-06-30",
                gpa="3.9"
            )
        ]
        self.experience = [
            Experience(
                title="Software Engineer",
                company="Tech Corp",
                location="Example Town",
                start_date="2022-07-01",
                end_date="Present",
                description="- Developed and maintained robust web applications.\n- Collaborated with cross-functional teams to deliver high-quality software."
            )
        ]
        self.skills = Skills(
            technical=["Python", "Flask", "SQL"],
            soft=["Teamwork", "Communication"],
            languages=["English", "Spanish"]
        )
        self.full_cv_data = CVData(
            personal_info=self.personal_info,
            education=self.education,
            experience=self.experience,
            skills=self.skills
        )
        self.empty_cv_data = CVData()
        self.partial_cv_data = CVData(
            personal_info=PersonalInformation(name="Partial User"),
            skills=Skills(technical=["JavaScript"])
        )

    def test_export_to_pdf_empty_cv_data(self):
        buffer = export_to_pdf(self.empty_cv_data, "empty_cv.pdf")
        self.assertIsInstance(buffer, BytesIO)
        # It should still produce a valid, albeit minimal, PDF file
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_export_to_pdf_full_cv_data(self):
        buffer = export_to_pdf(self.full_cv_data, "full_cv.pdf")
        self.assertIsInstance(buffer, BytesIO)
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_export_to_pdf_partial_cv_data(self):
        buffer = export_to_pdf(self.partial_cv_data, "partial_cv.pdf")
        self.assertIsInstance(buffer, BytesIO)
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_export_to_docx_empty_cv_data(self):
        buffer = export_to_docx(self.empty_cv_data, "empty_cv.docx")
        self.assertIsInstance(buffer, BytesIO)
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_export_to_docx_full_cv_data(self):
        buffer = export_to_docx(self.full_cv_data, "full_cv.docx")
        self.assertIsInstance(buffer, BytesIO)
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_export_to_docx_partial_cv_data(self):
        buffer = export_to_docx(self.partial_cv_data, "partial_cv.docx")
        self.assertIsInstance(buffer, BytesIO)
        self.assertGreater(buffer.getbuffer().nbytes, 0)

if __name__ == '__main__':
    unittest.main()
