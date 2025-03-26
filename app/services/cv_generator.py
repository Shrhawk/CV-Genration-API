import os
from io import BytesIO
from typing import Any

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


class CVGenerator:
    DEFAULT_SECTIONS = [
        {"id": "summary", "title": "Professional Summary", "order": 1, "visible": True},
        {"id": "experience", "title": "Work Experience", "order": 2, "visible": True},
        {"id": "education", "title": "Education", "order": 3, "visible": True},
        {"id": "skills", "title": "Skills", "order": 4, "visible": True},
        {"id": "languages", "title": "Languages", "order": 5, "visible": True},
        {"id": "certifications", "title": "Certifications", "order": 6, "visible": True}
    ]

    def __init__(self):
        self.template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def prepare_cv_data(self, cv_data: dict[str, Any]) -> dict[str, Any]:
        """Prepare CV data by adding default configuration if not provided.

        Args:
            cv_data (dict[str, Any]): The raw CV data dictionary.

        Returns:
            dict[str, Any]: The prepared CV data with default configurations.
        """
        if "config" not in cv_data:
            cv_data["config"] = {}

        # Set default font family if not provided
        if "font_family" not in cv_data["config"]:
            cv_data["config"]["font_family"] = "Roboto"

        # Set default theme if not provided
        if "theme" not in cv_data["config"]:
            cv_data["config"]["theme"] = "default"

        # Handle sections configuration
        if "sections" not in cv_data["config"]:
            cv_data["config"]["sections"] = self.DEFAULT_SECTIONS
        else:
            # Merge user-provided sections with defaults
            user_sections = {s["id"]: s for s in cv_data["config"]["sections"]}
            merged_sections = []

            for default_section in self.DEFAULT_SECTIONS:
                section_id = default_section["id"]
                if section_id in user_sections:
                    # Use user's section but ensure all required fields exist
                    section = user_sections[section_id]
                    section.setdefault("title", default_section["title"])
                    section.setdefault("order", default_section["order"])
                    section.setdefault("visible", default_section["visible"])
                    merged_sections.append(section)
                else:
                    merged_sections.append(default_section)

            # Add any additional user sections not in defaults
            for section in cv_data["config"]["sections"]:
                if section["id"] not in {s["id"] for s in merged_sections}:
                    merged_sections.append(section)

            # Sort sections by order
            cv_data["config"]["sections"] = sorted(
                merged_sections, key=lambda x: x.get("order", 999)
            )

        return cv_data

    def generate_html(self, cv_data: dict[str, Any]) -> str:
        """
        Generate HTML content from CV data using Jinja2 template.

        Args:
            cv_data (dict[str, Any]): The CV data to generate HTML from.

        Returns:
            str: The generated HTML content.
        """
        # Prepare CV data with defaults and configuration
        cv_data = self.prepare_cv_data(cv_data)

        template = self.env.get_template('cv_template.html')
        return template.render(**cv_data)

    def generate_pdf(self, cv_data: dict[str, Any]) -> bytes:
        """
        Generate PDF from CV data.

        Args:
            cv_data (dict[str, Any]): The CV data to generate PDF from.

        Returns:
            bytes: The generated PDF content as bytes.
        """
        # Generate HTML content
        html_content = self.generate_html(cv_data)

        # Convert HTML to PDF
        pdf_bytes = BytesIO()
        HTML(string=html_content).write_pdf(pdf_bytes)
        pdf_bytes.seek(0)

        return pdf_bytes.read()

    def save_pdf(self, cv_id: str, pdf_content: bytes) -> str:
        """
        Save PDF content to file.

        Args:
            cv_id (str): The unique identifier for the CV.
            pdf_content (bytes): The PDF content to save.

        Returns:
            str: The path where the PDF was saved.
        """
        output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'output')
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"cv_{cv_id}.pdf")
        with open(output_path, 'wb') as f:
            f.write(pdf_content)

        return output_path
