from pydantic import BaseModel


class ResearchPlan(BaseModel):
    topics: list[str]
    search_queries: list[str]
    estimated_time: int


plan = ResearchPlan(
    topics=[
        "Quantum computing basics",
        "Quantum algorithms",
        "Quantum computing applications"
    ],
    search_queries=[
        "quantum computing basics",
        "quantum algorithms",
        "quantum computing applications"
    ],
    estimated_time=30
)


print(plan)