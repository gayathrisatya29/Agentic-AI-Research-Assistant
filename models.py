from dataclasses import dataclass

@dataclass
class ResearchQuery:
    query: str
    max_sources: int = 5
    language: str = "en"