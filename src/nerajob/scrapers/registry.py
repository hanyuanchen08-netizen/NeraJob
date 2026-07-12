from __future__ import annotations

from nerajob.scrapers.base import BaseScraper
from nerajob.scrapers.remoteok import RemoteOKScraper
from nerajob.scrapers.sample import SampleScraper


def available_scrapers() -> dict[str, BaseScraper]:
    scrapers: list[BaseScraper] = [
        SampleScraper(),
        RemoteOKScraper(),
    ]
    return {s.name: s for s in scrapers}


def get_scraper(name: str) -> BaseScraper:
    scrapers = available_scrapers()
    if name not in scrapers:
        known = ", ".join(sorted(scrapers))
        raise KeyError(f"Unknown scraper {name!r}. Known: {known}")
    return scrapers[name]
