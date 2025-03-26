from typing import Optional

from pydantic import BaseModel


class Experience(BaseModel):
    company: str
    role: str
    start_date: str
    end_date: str
    responsibilities: list[str]


class Education(BaseModel):
    institution: str
    degree: str
    major: str
    cgpa: Optional[float]
    year: str
    achievements: Optional[list[str]]


class Language(BaseModel):
    language: str
    level: str


class Certification(BaseModel):
    name: str
    year: str


class Contact(BaseModel):
    email: str
    phone: str


class SocialLink(BaseModel):
    platform: str
    url: str
    icon: Optional[str] = None


class Section(BaseModel):
    id: str
    title: str
    visible: bool = True
    order: int


class CVConfig(BaseModel):
    theme: str = "default"
    sections: list[Section] = []
    font_family: str = "Roboto"
    company_logo: Optional[str] = None


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
    link: Optional[str]
    highlights: list[str]


class CVData(BaseModel):
    full_name: str
    job_title: str
    summary: Optional[str]
    experience: Optional[list[Experience]]
    education: Optional[list[Education]]
    projects: Optional[list[Project]]
    skills: Optional[list[str]]
    languages: Optional[list[Language]]
    certifications: Optional[list[Certification]]
    contact: Contact
    social_links: Optional[list[SocialLink]]
    config: Optional[CVConfig]
