from graph import research_graph


print("Starting AI Research Assistant...")


result = research_graph.invoke(
    {
        "topic": "Artificial Intelligence in Healthcare",
        "research": "",
        "report": "",
        "validation": "",
        "revision_count": 0
    }
)


print("\n========== FINAL REPORT ==========\n")
print(result["report"])

print("\n========== VALIDATION ==========\n")
print(result["validation"])