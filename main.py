import asyncio

from models import ResearchQuery


async def fetch_research(rq: ResearchQuery) -> str:
    await asyncio.sleep(0)# placeholder for async API call

    return f"Results for: {rq.query}"


async def main():
    rq = ResearchQuery(
        query="quantum computing",
        max_sources=10,
        language="en"
    )

    result = await fetch_research(rq)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())