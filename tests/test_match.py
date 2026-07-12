from nerajob.match import match_score, rank_jobs
from nerajob.models import JobPosting, Profile
from nerajob.storage import default_profile


def test_match_score_hits_python() -> None:
    profile = default_profile()
    profile.skills = ["Python", "FastAPI", "SQL"]
    job = JobPosting(
        id="j1",
        source="sample",
        title="Senior Python Backend Engineer",
        company="Acme",
        description="Build FastAPI services with SQL databases",
        tags=["python", "api"],
        remote=True,
    )
    m = match_score(profile, job)
    assert m["score"] >= 40
    assert "python" in m["skill_hits"]


def test_rank_jobs() -> None:
    profile = Profile(skills=["python", "kubernetes"])
    jobs = [
        JobPosting(id="a", source="s", title="K8s Platform", company="X", description="kubernetes", tags=["k8s"]),
        JobPosting(id="b", source="s", title="Sales", company="Y", description="crm", tags=["sales"]),
    ]
    ranked = rank_jobs(profile, jobs, top_k=2)
    assert ranked[0]["job_id"] == "a"
