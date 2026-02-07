from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class PersonalInformation:
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    github: str = ""
    summary: str = ""

@dataclass
class Education:
    degree: str = ""
    major: str = ""
    institution: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    gpa: Optional[str] = None

@dataclass
class Experience:
    title: str = ""
    company: str = ""
    location: str = ""
    start_date: str = ""
    end_date: str = ""
    description: str = "" # This will be a multi-line string

@dataclass
class Skills:
    technical: List[str] = field(default_factory=list)
    soft: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)

@dataclass
class CVData:
    personal_info: PersonalInformation = field(default_factory=PersonalInformation)
    education: List[Education] = field(default_factory=list)
    experience: List[Experience] = field(default_factory=list)
    skills: Skills = field(default_factory=Skills)
