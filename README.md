# ATS CV Web Application - Professional & User-Friendly Builder

This is a Python-based web application designed to help users create highly professional, ATS (Applicant Tracking System)-friendly CVs with a focus on user experience and clean code architecture. The application provides a user-friendly interface to collect personal details, education, experience, and skills, then generates a visually appealing and robust CV in various formats.

## Key Features & Enhancements

*   **Clean Code Architecture:**
    *   **Modular Design:** The application now follows a cleaner architecture with distinct modules:
        *   `models.py`: Defines structured data models (dataclasses) for `PersonalInformation`, `Education`, `Experience`, `Skills`, and `CVData`, ensuring type safety and better data management.
        *   `cv_builder.py`: Contains the core logic for generating markdown-formatted CV content from the structured `CVData` object, promoting separation of concerns.
        *   `export_utils.py`: Refactored to directly consume `CVData` objects, allowing for precise and consistent professional formatting across all export types (PDF, DOCX).
    *   **Readability & Maintainability:** Code has been reviewed and refactored for improved clarity, adherence to Python best practices (PEP 8), and easier maintenance.

*   **Enhanced User Interface (UI) & User Experience (UX):**
    *   **Intuitive Navigation:** Redesigned with Streamlit tabs for structured input sections (Personal Information, Education, Experience, Skills) and expandable sections for better organization.
    *   **Real-time Input Validation:** Provides immediate feedback and helpful guidance messages for form fields to ensure accurate data entry.
    *   **Dynamic Skill Management:** Allows users to add and remove individual technical skills, soft skills, and languages on the fly with improved visual feedback.
    *   **"Reset All Fields" Button:** A prominent button to quickly clear all entered data and start fresh, enhancing user control.

*   **Professional & Robust CV Generation:**
    *   **Consistent Formatting:** PDF and DOCX exports are now generated directly from structured data, ensuring consistent, professional-grade formatting, typography, and layout across all document types. The PDF export specifically adheres to a professional template, replicating visual layout, font styles, line separators, and bullet points.
    *   **Improved Output Handling:** Better management of empty fields and sections in the generated CVs, leading to cleaner and more polished documents.
    *   **Live CV Preview:** A dedicated section that updates in real-time as you fill out the form, providing an instant look at your generated CV.
    *   **Multi-Format Export:** Allows users to download their generated CV in multiple ATS-friendly and professionally formatted options: Markdown (`.md`), Plain Text (`.txt`), PDF (`.pdf`), and DOCX (`.docx`).

## Technologies Used

*   **Python:** The core programming language.
*   **Streamlit:** For building the interactive web interface.
*   **python-docx:** For generating professionally formatted CVs in DOCX format.
*   **ReportLab:** For generating professionally formatted CVs in PDF format.
*   **dataclasses:** For creating structured, type-hinted data models.

## Setup and Installation

Follow these steps to set up and run the application locally:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/nashmi572004-afk/ats-cv-web-app.git
    cd ats-cv-web-app
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your default web browser at `http://localhost:8501`.

## Running Tests

To run the unit and integration tests for this application, navigate to the project's root directory and execute the following command:

```bash
python -m unittest discover tests
```

This command will discover and run all test files within the `tests/` directory.

## Usage

1.  Navigate through the different sections using the tabs: "Personal Information", "Education", "Experience", and "Skills".
2.  Fill in your details in each section. Utilize the expanders to organize your input. Pay attention to the real-time validation messages.
3.  Use the "Reset All Fields" button at the top to clear all data and start fresh at any time.
4.  In the "Skills" section, add your technical skills, soft skills, and languages dynamically using the input fields and "Add" buttons. You can remove skills individually.
5.  Observe the "Live CV Preview" on the right side of the screen, which updates instantly as you input your information.
6.  Once satisfied, use the download buttons in the live preview section to get your professionally formatted CV in Markdown (`.md`), plain text (`.txt`), PDF (`.pdf`), or DOCX (`.docx`) format.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Ensure all tests pass (`python -m unittest discover tests`).
6.  Push to the branch (`git push origin feature/your-feature-name`).
7.  Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
