# app/agents/supervisor.py

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory

from food_fashion_agent import food_expert,fashion_expert,transport_expert
from gemini import GeminiLLM

llm = GeminiLLM()

memory = ConversationBufferMemory(return_messages=True)

SYSTEM_PROMPT = """
You are a supervisor agent.

Responsibilities:
- Understand user intent
- Choose correct tool
- If no tool fits → answer yourself
- After tool response → refine it into a final answer

Tools:
- food_expert → food queries
- fashion_expert → clothes, skincare
- transport_expert → Uber, Ola, buses

Always think before acting.
"""

def build_agent():
    tools = [food_expert, fashion_expert, transport_expert]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        memory=memory,
        verbose=True,
        agent_kwargs={"system_message": SYSTEM_PROMPT}
    )

    return agent