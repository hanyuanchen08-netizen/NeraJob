from nerajob.apply.assistant import build_checklist, build_cover_note
from nerajob.models import JobPosting
from nerajob.storage import default_profile


def test_cover_note_mentions_company_and_role():
    profile = default_profile()
    job = JobPosting(
        id="job-1",
        source="sample",
        title="Backend Engineer",
        company="Acme",
        description="Python APIs",
        tags=["python"],
        url="https://example.com/j/1",
    )
    note = build_cover_note(profile, job)
    assert "Acme" in note
    assert "Backend Engineer" in note
    assert profile.full_name in note
    checklist = build_checklist(job)
    assert any("follow-up" in item.lower() for item in checklist)
