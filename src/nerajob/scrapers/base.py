from __future__ import annotations

from abc import ABC, abstractmethod

from nerajob.models import JobPosting


class BaseScraper(ABC):
    """Interface for a single job source."""

    name: str = "base"

    @abstractmethod
    def search(self, query: str, location: str = "", limit: int = 20) -> list[JobPosting]:
        raise NotImplementedError
