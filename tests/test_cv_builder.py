from nerajob.cv.builder import build_cv_markdown
from nerajob.storage import default_profile


def test_build_cv_contains_name_and_skills():
    profile = default_profile()
    md = build_cv_markdown(profile, target_role="Python Engineer")
    assert profile.full_name in md
    assert "Python" in md
    assert "Python Engineer" in md
