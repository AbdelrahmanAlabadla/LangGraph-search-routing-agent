from langgraph.graph import StateGraph, START, END
from nodes import search_node, llm_node, router

def build_graph(AgentState):
    graph=StateGraph(AgentState)
    graph.add_node("search_node", search_node)
    graph.add_node("llm_node", llm_node)

    graph.add_conditional_edges(
        START,
        router,
        {
            "search_node":"search_node",
            "llm_node":"llm_node"

        }
    )

    graph.add_edge("search_node","llm_node")
    graph.add_edge("llm_node",END)

    return graph.compile()

