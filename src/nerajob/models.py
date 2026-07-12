from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class Experience(BaseModel):
    title: str
    company: str
    start: str = ""
    end: str = "Present"
    highlights: list[str] = Field(default_factory=list)


class Education(BaseModel):
    school: str
    degree: str = ""
    year: str = ""


class Profile(BaseModel):
    full_name: str = "Your Name"
    email: str = "you@example.com"
    phone: str = ""
    location: str = "Remote"
    headline: str = "Software Engineer"
    summary: str = "Results-driven engineer building reliable products."
    skills: list[str] = Field(default_factory=lambda: ["Python", "APIs", "SQL"])
    experience: list[Experience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    links: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=lambda: ["English"])


class JobPosting(BaseModel):
    id: str
    source: str
    title: str
    company: str
    location: str = "Remote"
    url: str = ""
    description: str = ""
    tags: list[str] = Field(default_factory=list)
    salary: str = ""
    remote: bool = True
    scraped_at: str = Field(default_factory=utc_now_iso)
    raw: dict[str, Any] = Field(default_factory=dict)


class ApplicationPackage(BaseModel):
    job_id: str
    created_at: str = Field(default_factory=utc_now_iso)
    cover_note: str = ""
    checklist: list[str] = Field(default_factory=list)
    cv_markdown_path: str = ""
    notes: str = ""
