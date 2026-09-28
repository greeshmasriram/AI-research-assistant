async function startResearch() {

    const topicInput = document.getElementById("topic");
    const topic = topicInput.value.trim();

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");
    const report = document.getElementById("report");
    const error = document.getElementById("error");
    const button = document.getElementById("researchButton");

    // Check if user entered a topic
    if (!topic) {
        error.textContent = "Please enter a research topic.";
        error.style.display = "block";
        return;
    }

    // Prepare the page
    error.style.display = "none";
    result.style.display = "none";
    loading.style.display = "block";

    button.disabled = true;
    button.textContent = "Generating...";

    try {

        // Send the topic to our Flask API
        const response = await fetch("/research", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                topic: topic
            })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(
                data.error || "Something went wrong."
            );
        }

        // Show the AI-generated report
        report.textContent = data.report;

        result.style.display = "block";

    } catch (err) {

        error.textContent = err.message;
        error.style.display = "block";

    } finally {

        loading.style.display = "none";

        button.disabled = false;
        button.textContent = "Generate Report";
    }
}