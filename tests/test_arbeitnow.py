from nerajob.scrapers.registry import available_scrapers, get_scraper


def test_arbeitnow_registered() -> None:
    assert "arbeitnow" in available_scrapers()


def test_arbeitnow_offline(monkeypatch) -> None:
    monkeypatch.setenv("NERAJOB_ARBEITNOW_OFFLINE", "1")
    jobs = get_scraper("arbeitnow").search("python", limit=5)
    assert jobs
    assert all(j.source == "arbeitnow" for j in jobs)
