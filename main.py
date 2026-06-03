
from graph import build_graph
from state import AgentState

user_input = input("what do u want to search for sir: ")
app = build_graph(AgentState)

print(app.get_graph())
results = app.invoke({
    "messages": [],
    "question": user_input,
    "answer": "",
    "search_results": [],
    "mode": "",
    "trace": {}
})
print("\n=== FINAL RESULT ===\n")


print(f"Question: {results['question']}")
print(f"\nAnswer:\n{results['answer']}")
print(f"\nMode: {results['mode']}")
print(f"\nTrace: {results['trace']}")