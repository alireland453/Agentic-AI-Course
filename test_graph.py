from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. Define the "State" (the shared clipboard passed between steps)
class AgentState(TypedDict):
    message: str

# 2. Define a "Node" (a Python function that does work)
def greeting_node(state: AgentState) -> AgentState:
    updated_text = f"{state['message']} -> Verified! LangGraph is up and running on Vector One."
    return {"message": updated_text}

# 3. Build and wire the Graph
builder = StateGraph(AgentState)
builder.add_node("greeter", greeting_node)
builder.add_edge(START, "greeter")
builder.add_edge("greeter", END)

# 4. Compile and run the Graph
graph = builder.compile()
result = graph.invoke({"message": "Hello Agentic AI"})

print("\n--- TEST OUTPUT ---")
print(result["message"])
print("-------------------\n")