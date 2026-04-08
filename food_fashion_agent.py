# app/agents/food_agent.py

from langchain.tools import tool
from gemini import GeminiLLM

llm = GeminiLLM()

@tool
def food_expert(query: str) -> str:
    """Handles food, recipes, restaurants, nutrition."""
    
    response = llm.generate(
        f"You are a professional chef and nutritionist. Answer:\n{query}"
    )

    return f"TOOL_RESPONSE: {response}"


@tool
def fashion_expert(query: str) -> str:
    """Handles clothing, styling, skincare."""
    
    response = llm.generate(
        f"You are a fashion stylist and skincare expert:\n{query}"
    )

    return f"TOOL_RESPONSE: {response}"

from playwright import search_redbus

llm = GeminiLLM()

@tool
def transport_expert(query: str) -> str:
    """Handles Uber, Ola, Rapido, buses, travel queries."""

    # naive extraction (can upgrade later)
    if "bus" in query.lower():
        data = search_redbus("Hyderabad", "Bangalore")
    else:
        data = "Live transport scraping limited, providing general guidance."

    response = llm.generate(
        f"""
        You are a transport assistant.

        User query: {query}
        Live data: {data}

        Provide helpful response.
        """
    )

    return f"TOOL_RESPONSE: {response}"
