from nerajob.scrapers.sample import SampleScraper


def test_sample_scraper_filters_python_roles():
    jobs = SampleScraper().search(query="python", location="remote", limit=10)
    assert jobs
    assert all("python" in (" ".join(j.tags) + j.title).lower() or "python" in j.description.lower() for j in jobs)


def test_sample_scraper_ids_stable():
    a = SampleScraper().search(query="python", limit=5)
    b = SampleScraper().search(query="python", limit=5)
    assert [j.id for j in a] == [j.id for j in b]
