# 🌌 Agentic Research AI

Agentic Research AI is a fully automated, multi-agent pipeline built with Python and Streamlit. It orchestrates a swarm of specialized AI agents to autonomously research a given topic, extract deep insights, draft a comprehensive report, and critically review its own work.

## 🏗️ Architecture

The application follows a sequential, multi-agent pipeline architecture where the output of one agent serves as the context and input for the next:

```text
[User Input] 
     │
     ▼
 🕵️‍♂️ Search Agent  ────> Queries web & retrieves relevant URLs
     │
     ▼
 📖 Reader Agent  ────> Scrapes content & extracts deep context
     │
     ▼
 ✍️ Writer Agent  ────> Synthesizes data & drafts the research report
     │
     ▼
 🧐 Critic Agent  ────> Analyzes the draft for bias, accuracy, and flow
     │
     ▼
[Final Dashboard UI] ──> Displays Report, Critic Review, and Raw Context
```

## ✨ Features

* **Multi-Agent Architecture:** Utilizes four specialized agents working in a synchronized pipeline.
* **Modern Dashboard UI:** A beautiful, responsive Streamlit interface featuring glassmorphism cards, dynamic progress tracking, and toast notifications.
* **Real-time Execution Tracking:** Watch the agents work step-by-step with live status updates.
* **Dual-Pane View:** Read the final report side-by-side with the Critic Agent's review.
* **Downloadable Artifacts:** Export the generated research reports and critic reviews as Markdown (`.md`) files.
* **Under the Hood:** Inspect the raw web search data and scraped HTML/text context.

## 💻 Technologies Used

* **Frontend:** [Streamlit](https://streamlit.io/) (with custom CSS for modern styling)
* **Backend Framework:** [LangChain](https://www.langchain.com/) 
* **Programming Language:** Python 3.8+
* **Environment Management:** `python-dotenv`
* **Console Formatting:** `rich` (for backend terminal logging)
* **APIs:** 
  * LLM Provider (e.g., OpenAI, Anthropic, or local models)
  * Search API (e.g., Tavily, Google Search API)

## 📁 Project Structure

```text
├── app.py                  # Main Streamlit frontend application
├── src/
│   ├── Agents/             # Definitions for Search, Reader, Writer, and Critic agents
│   │   └── agents.py       
│   ├── Tools/
|   |   └── tools.py        # Custom tools utilized by the agents (e.g., web scraping, searching)
│   └── Pipeline/
|       └── pipeline.py     # Orchestration logic linking the agents together
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 🚀 Installation Process

Follow these steps to set up the project locally:

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/agentic-research-ai.git](https://github.com/yourusername/agentic-research-ai.git)
cd agentic-research-ai
```

**2. Create a Virtual Environment (Recommended)**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
Create a `.env` file in the root directory of the project and add your required API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
# Add any other required API keys based on your specific agents.py configuration
```

## 💡 Usage

**1. Run the Application**
Launch the Streamlit interface using the following command:
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at `http://localhost:8501`.

**2. Operating the Dashboard**
* In the main input box, type your research topic (e.g., "The History and Future of Large Language Models").
* Click the **Launch Swarm** button.
* Monitor the dynamic progress bar and status metrics as the agents execute their tasks sequentially.
* Review the **Final Drafted Report** and the **Critic's Review** side-by-side.
* Use the **Download** buttons to save the generated documents locally.
* Open the **Under the Hood** expander at the bottom to view the raw data collected by the Search and Reader agents.
