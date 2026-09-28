from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents import (
    research_agent,
    writer_agent,
    validator_agent,
)


class ResearchState(TypedDict):
    topic: str
    research: str
    report: str
    validation: str
    revision_count: int

    # RESEARCH NODE
def research_node(state: ResearchState):
    print("Research Agent is working...")

    research = research_agent(state["topic"])

    return {
        "research": research
    }


# WRITER NODE
def writer_node(state: ResearchState):
    print("Writer Agent is working...")

    report = writer_agent(
        state["topic"],
        state["research"]
    )

    return {
        "report": report
    }


# VALIDATOR NODE
def validator_node(state: ResearchState):
    print("Validator Agent is checking the report...")

    validation = validator_agent(
        state["topic"],
        state["report"]
    )

    return {
        "validation": validation
    }

# DECIDE WHETHER THE REPORT IS GOOD OR NEEDS REVISION
def validation_router(state: ResearchState):

    validation = state["validation"]

    # Gemini may return a list containing structured text
    if isinstance(validation, list):
        for item in validation:
            if isinstance(item, dict):
                text = item.get("text", "")
                if str(text).strip().upper() == "PASS":
                    print("Validation result: PASS")
                    return "complete"

    # Handle normal string response
    validation_text = str(validation).strip().upper()

    print(f"Validation result: {validation_text}")

    # If validator says PASS, finish
    if validation_text == "PASS":
        return "complete"

    # Stop after 2 revisions
    if state["revision_count"] >= 2:
        return "complete"

    # Otherwise revise the report
    return "revise"

# REVISION NODE
def revision_node(state: ResearchState):
    print("Writer Agent is revising the report...")

    report = writer_agent(
        state["topic"],
        state["research"]
    )

    return {
        "report": report,
        "revision_count": state["revision_count"] + 1
    }

# BUILD THE LANGGRAPH
builder = StateGraph(ResearchState)

# Add nodes
builder.add_node("researcher", research_node)
builder.add_node("writer", writer_node)
builder.add_node("validator", validator_node)
builder.add_node("revision", revision_node)

# Connect the workflow
builder.add_edge(START, "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "validator")

# Conditional decision after validation
builder.add_conditional_edges(
    "validator",
    validation_router,
    {
        "complete": END,
        "revise": "revision"
    }
)

# After revision, validate again
builder.add_edge("revision", "validator")

# Compile the graph
research_graph = builder.compile()