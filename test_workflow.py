import asyncio
from app.agent import CustomerSupportAgent

async def run_test(agent: CustomerSupportAgent, query: str):
    print(f"\nQuery: {repr(query)}")
    response = await agent.handle_query(query)
    print(f"Agent: {response}")

async def main():
    agent = CustomerSupportAgent()
    test_queries = [
        "Where is my package? The tracking number is 12345.",
        "How much does standard shipping cost?",
        "What is your return policy?",
        "Can you recommend a good Italian restaurant nearby?",
        "I need help with my taxes."
    ]
    for q in test_queries:
        await run_test(agent, q)

if __name__ == "__main__":
    asyncio.run(main())
