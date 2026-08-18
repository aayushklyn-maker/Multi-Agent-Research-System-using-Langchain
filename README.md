# Multi-Agent-Research-System-using-Langchain
# 🌌 Agentic Research AI

Agentic Research AI is a fully automated, multi-agent pipeline built with Python and Streamlit. It orchestrates a swarm of specialized AI agents to autonomously research a given topic, extract deep insights, draft a comprehensive report, and critically review its own work.

## ✨ Features

* **Multi-Agent Architecture:** Utilizes four specialized agents (Search, Reader, Writer, Critic) working in a synchronized pipeline.
* **Modern Dashboard UI:** A beautiful, responsive Streamlit interface featuring glassmorphism cards, dynamic progress tracking, and toast notifications.
* **Real-time Execution Tracking:** Watch the agents work step-by-step with live status updates.
* **Dual-Pane View:** Read the final report side-by-side with the Critic Agent's review.
* **Downloadable Artifacts:** Export the generated research reports and critic reviews as Markdown (`.md`) files.
* **Under the Hood:** Inspect the raw web search data and scraped HTML/text context.

## 🤖 The Agent Swarm

1. 🕵️‍♂️ **Search Agent:** Queries the web for the most recent, reliable information and identifies high-quality URLs.
2. 📖 **Reader Agent:** Visits the identified URLs to scrape and extract deep, contextual information.
3. ✍️ **Writer Agent:** Synthesizes the raw scraped data into a highly structured, readable, and comprehensive research report.
4. 🧐 **Critic Agent:** Evaluates the Writer's draft for accuracy, bias, structural flow, and completeness, offering a critical second opinion.

## 📁 Project Structure

```text
├── app.py                  # Main Streamlit application
├── src/
│   ├── Agents/             # Definitions for Search, Reader, Writer, and Critic agents
│   │   └── agents.py       
│   ├── Tools/              # Custom tools utilized by the agents (e.g., scraping, searching)
│   └── Pipeline/           # Orchestration logic linking the agents together
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
