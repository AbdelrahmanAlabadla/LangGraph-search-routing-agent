from langgraph.graph import StateGraph,END

from typing import TypedDict,List,Dict,Any

class AgentState(TypedDict):
    messages:List[Dict[str, str]]
    question:str
    answer:str
    search_results:List[Dict[str,Any]]
    mode: str
    trace: Dict[str, Any]


