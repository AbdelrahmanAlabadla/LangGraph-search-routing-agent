
from typing_extensions import overload

from prompt import SYSTEM_PROMPT
from agent import call_llm
from state import AgentState
from tools import web_search

def format_results(results):
    if not results:
        return "No web results were found."

    text = ""
    for r in results:
        text += f"""
Title: {r.get('title', 'No title')}
Link: {r.get('link', 'No link')}
Snippet: {r.get('snippet', 'No snippet')}
"""
    return text

def router(state: AgentState):
    q = state["question"].lower()

    keywords = ["latest", "news", "price", "who is", "search", "current"]
    decision = "search_node" if any(k in q for k in keywords) else "llm_node"

    trace = state.get("trace", {})
    trace["router_decision"] = decision

    return decision




def llm_node(state:AgentState):
    question=state["question"]

    search_results = state.get("search_results", [])

    formatted_results = format_results(search_results)

    prompt = SYSTEM_PROMPT.format(
        question=question,
        search_results=formatted_results
    )

    response=call_llm(prompt)

    trace = state.get("trace", {})

    trace["llm_model_name"] = "google/gemma-4-e2b"
    mode = "web" if search_results else "llm"
    return {
        "messages": state["messages"] + [
            {"role": "user", "content": question},
            {"role": "assistant", "content": response}
        ],
        "answer": response,
        "mode": mode,
        "trace": trace
    }



def search_node(state:AgentState):
    query=state["question"]

    results=web_search(query)

    trace = state.get("trace", {})

    trace["router_decision"] = "search_node"
    trace["search_results_count"] = len(results)

    return {
            "search_results": results,
            "trace": trace
        }

