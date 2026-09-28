from flask import Flask, render_template, request, jsonify
from graph import research_graph

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API endpoint
@app.route("/research", methods=["POST"])
def research():
    try:
        # Get topic from frontend
        data = request.get_json()
        topic = data.get("topic", "").strip()

        if not topic:
            return jsonify({
                "error": "Please enter a research topic."
            }), 400

        print(f"Research request received: {topic}")

        # Run LangGraph workflow
        result = research_graph.invoke({
            "topic": topic,
            "research": "",
            "report": "",
            "validation": "",
            "revision_count": 0
        })

        # Get report from LangGraph
        report = result["report"]

        # Convert report into plain text
        if isinstance(report, list):
            text_parts = []

            for item in report:
                if isinstance(item, dict):
                    if "text" in item:
                        text_parts.append(str(item["text"]))
                    elif "content" in item:
                        text_parts.append(str(item["content"]))
                    else:
                        text_parts.append(str(item))
                else:
                    text_parts.append(str(item))

            report = "\n\n".join(text_parts)

        else:
            report = str(report)

        # Send result to frontend
        return jsonify({
            "success": True,
            "topic": topic,
            "report": report,
            "validation": result["validation"]
        })

    except Exception as e:
        print(f"Error: {e}")

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)