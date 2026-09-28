import os
import time

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
def call_gemini_with_retry(prompt, max_retries=4):
    for attempt in range(max_retries):
        try:
            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            error_message = str(e)

            if "503" in error_message or "UNAVAILABLE" in error_message:
                wait_time = 2 ** attempt

                print(
                    f"Gemini is busy. Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)
            else:
                raise e

    raise Exception(
        "Gemini is temporarily unavailable after multiple retries."
    )


def research_agent(topic):
    prompt = f"""
    You are an AI research assistant.

    Research and explain the following topic:

    {topic}

    Provide:
    1. A simple introduction
    2. Important concepts
    3. Key benefits
    4. Challenges
    5. Real-world applications

    Keep the research factual, clear, and structured.
    """

    return call_gemini_with_retry(prompt)

def writer_agent(topic, research):
    prompt = f"""
    You are a professional content writer.

    Topic:
    {topic}

    Research:
    {research}

    Using the research above, create a well-structured report.

    The report should contain:

    Title
    Introduction
    Key Findings
    Benefits
    Challenges
    Real-World Applications
    Conclusion

    Make the report easy to understand.
    """

    return call_gemini_with_retry(prompt)


def validator_agent(topic, report):
    prompt = f"""
    You are a quality-control reviewer.

    Topic:
    {topic}

    Report:
    {report}

    Check the report for:

    - relevance to the topic
    - clear structure
    - grammar
    - completeness
    - logical consistency

    If the report is good enough, respond with:

    PASS

    Otherwise respond with:

    REVISE

    followed by a short explanation.
    """

    return call_gemini_with_retry(prompt)